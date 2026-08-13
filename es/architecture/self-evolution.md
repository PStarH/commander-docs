# Auto-evolución

Documentación en español de **Auto-evolución**, alineada con el monorepo y la guía inglesa.

Commander mejora por sí mismo mediante **meta-aprendizaje**: un selector de estrategias por Thompson Sampling aprende qué estrategia de orquestación funciona mejor por tipo de tarea, mientras un analizador de trayectorias clasifica los fallos y un agente evolutivo propone mutaciones de configuración. Todo el estado es inspeccionable a través de la fachada `MetaLearner`.

## Arquitectura

```
Execution completes
  → recordExperience(exp)       ← MetaLearner facade
      ├─ TrajectoryAnalyzer     ← classify failure category (heuristic / LLM)
      ├─ StrategySelector       ← Thompson Sampling per task type
      ├─ Reflexion              ← generateReflection(exp)
      └─ persist()              ← .commander_memory/meta-learner.json

  → EvolverAgent.evolve(insights, config)
      └─ propose mutations (quality gates, thinking budget, model tier…)
```

## Tipos

```typescript
// 14 failure categories the trajectory analyzer can emit
type FailureCategory =
  | 'tool_misuse'        // wrong tool called or tool error
  | 'context_overflow'   // token/context budget exceeded
  | 'timeout'            // execution took too long
  | 'model_refusal'      // model refused to comply
  | 'missing_capability' // required capability/command/file not found
  | 'planning_error'     // wrong approach or misunderstanding
  | 'hallucination'      // made-up content or references
  | 'dependency_failure' // a subtask or dependency failed
  | 'quality_gate'       // quality/verification gate rejected output
  | 'rate_limit'         // API rate limiting or throttling
  | 'authentication'     // auth/permission failures
  | 'resource_exhaustion'// memory/disk/CPU limits hit
  | 'data_validation'    // invalid input/output format or schema
  | 'unclassified';      // does not fit any above category

type AnalysisMode = 'light' | 'balanced' | 'thorough';

interface ExecutionExperience {
  id: string;
  runId?: string;
  agentId: string;
  taskType: string;
  modelUsed: string;
  strategyUsed: string;      // one of STRATEGY_NAMES
  success: boolean;
  durationMs: number;
  tokenCost: number;
  errorPattern?: string;
  lessons: string[];
  toolsUsed?: string[];
  topology?: string;
  timestamp: number;
}

interface EvolutionInsight {
  runId: string;
  taskType: string;
  modelUsed: string;
  strategyUsed: string;
  success: boolean;
  errorPattern?: string;
  failureCategory: FailureCategory;
  confidence: number;        // 0-1
  evidence: string[];        // matched keywords / LLM evidence
  suggestion?: string;
  analysisTokens: number;
}

interface EvolverMutation {
  id: string;
  domain: 'quality_gate' | 'thinking_budget' | 'model_tier' | 'synthesis' | 'runtime';
  description: string;
  triggeredBy: FailureCategory;
  confidence: number;
  configPath: string;        // dot path into UltimateOrchestratorConfig
  oldValue: unknown;
  newValue: unknown;
}

interface EvolutionCycle {
  mutations: EvolverMutation[];
  applied: number;
  reverted: number;
  cycleId: string;
}
```

## MetaLearner

El meta-aprendiz es una fachada sobre cinco submódulos: `StrategySelector` (Thompson Sampling), `CrossModelMemory` (priors por modelo), `PredictionLoop` (predicciones falseables), `RegressionGate` (detección de caídas en tasa de éxito), `StrategyPerformanceTracker`, más el motor de reflexión y un motor de sugerencias.

```typescript
import {
  getMetaLearner,
  resetMetaLearner,
  DEFAULT_META_LEARNER_CONFIG,
} from '@commander/core';

const learner = getMetaLearner(); // singleton, persists to .commander_memory/meta-learner.json

learner.recordExperience(exp);    // learn from a completed run
const strategy = learner.selectStrategy('code-refactor', 'gpt-4o');
// → 'SEQUENTIAL' | 'PARALLEL' | 'HANDOFF' | 'MAGENTIC' | 'CONSENSUS'
```

`selectStrategy` devuelve `'SEQUENTIAL'` mientras el aprendiz está deshabilitado o tiene menos de `minRunsBeforeLearning` (50 por defecto) experiencias; después delega en el selector por Thompson Sampling.

### Introspección

```typescript
learner.getStats();
// → { totalExperiences, trackedStrategies, avgSuccessRate, topStrategies,
//     totalReflections, learningActive, runsUntilLearning }

learner.getConvergenceMetrics();
// → { taskTypes, strategiesPerType, avgSamplesPerStrategy, converged,
//     learningCurve: [{ taskType, improvementRate }] }
//   converged = avgSamplesPerStrategy >= 50 && |improvementRate| < 0.1 per type

learner.getSuggestions();
// → OptimizationSuggestion[] (model_tier_change, strategy_change,
//     prompt_template_change, tool_change) with confidence + evidence

learner.getStrategyScores(taskType);
// → [{ strategy, score, trials, avgDurationMs?, p95DurationMs? }]

learner.getRegressionEvents();    // success-rate drops ≥ regressionThreshold (0.15)
learner.getPredictions();         // falsifiable predictions (editId, target/source strategy)
learner.getVerdicts();            // fixesConfirmed / regressionsObserved / netImpact
learner.getReflections();         // last N reflexion blocks
learner.getShadowComparisons();   // shadow-mode strategy A/B results
learner.getExperiences(taskType?);
learner.getStrategyScoresForModel(modelId);
learner.setConfig({ analysisMode: 'balanced' });
```

### Configuración

```typescript
// DEFAULT_META_LEARNER_CONFIG
{
  analysisMode: 'light',          // light | balanced | thorough
  enablePredictionLoop: true,
  enableRegressionGate: true,
  enableCrossModelMemory: true,
  regressionThreshold: 0.15,
  enabled: true,
  minRunsBeforeLearning: 50,
  reflectionFrequency: 10,        // a reflexion is generated every N runs
}
```

## Selección de estrategia (Thompson Sampling)

Cada tipo de tarea mantiene un prior `BetaDistribution` por estrategia. La selección muestrea cada prior y lo multiplica por una bonificación de exploración, un factor de velocidad y un factor de coste.

```typescript
class BetaDistribution {
  constructor(alpha = 1, beta = 1);
  sample(): number;                                   // Gamma-based (Marsaglia & Tsang)
  update(success: boolean, taskDifficulty = 0.5);     // harder tasks update less
  mean(): number;
  totalTrials(): number;
  explorationBonus(totalTrials: number, explorationWeight: number): number; // UCB1
}

class StrategySelector {
  selectStrategy(taskType, strategyPerformance, modelId?): string;
  computeAdjustmentFactors(taskType, strategyPerformance);
  // → { samples, explorationBonuses, speedFactors, costFactors, explorationWeight }
  recordExperience(exp): void;
}
```

- `update(success, taskDifficulty)` pondera la actualización Beta por `0.5 + (1 − difficulty) × 0.5`, de modo que las tareas más difíciles aportan menos señal.
- La exploración usa UCB1: peso `0.5` mientras una estrategia tiene menos de 20 muestras, `0.2` después.
- Los factores de velocidad están limitados a `[0.7, 1.3]` y solo se aplican cuando cada estrategia tiene ≥ 3 ejecuciones y ≥ 2 estrategias exponen latencia p95; los de coste están limitados a `[0.8, 1.2]`.
- Los priors Thompson están acotados por `MAX_THOMPSON_PRIORS = 200` por clave modelo/tipo-de-tarea (se expulsa primero el más antiguo).

`STRATEGY_NAMES` (el vocabulario del meta-aprendiz) es distinto de `OrchestrationTopology`: se mantiene fijo en `['SEQUENTIAL', 'PARALLEL', 'HANDOFF', 'MAGENTIC', 'CONSENSUS']`.

## TrajectoryAnalyzer

Clasifica ejecuciones completadas en categorías de fallo sin coste de runtime por defecto. El modo decide cuándo interviene un LLM.

```typescript
import { TrajectoryAnalyzer } from '@commander/core';

// light:      heuristic-only, zero LLM calls (default)
// balanced:   heuristic first, LLM fallback for unclassified failures
// thorough:   LLM for every failure; successes always heuristic
const analyzer = new TrajectoryAnalyzer('light', provider?, model?);

const insights: EvolutionInsight[] = await analyzer.analyze(experiences);
```

- **Clasificador heurístico**: recorre `errorPattern + lessons + toolsUsed + topology + taskType` contra 13 reglas de palabras clave (p. ej. `timeout` → `timeout`, `429`/`rate limit` → `rate_limit`, `out of memory` → `resource_exhaustion`). La confianza base por regla es 0.55–0.85, con un incremento de `+0.05` por palabra clave que coincida (tope `+0.2`, total máximo `0.95`).
- **Clasificador LLM**: un prompt solo-JSON (temperatura 0.1, maxTokens 300) devuelve `{ category, confidence, evidence, suggestion }`; las respuestas que fallan la validación de forma se descartan y los errores del LLM caen a `unclassified / 0.3`.
- Las ejecuciones con éxito siempre producen un insight con `failureCategory: 'unclassified'`, `confidence: 1`, `evidence: []`.

## EvolverAgent

Propone mutaciones de configuración a partir de los insights analizados. El evolucionador solo *planifica* mutaciones — `evolve` nunca muta la configuración; llama a `applyMutations` explícitamente.

```typescript
import { getEvolverAgent, resetEvolverAgent } from '@commander/core';

const evolver = getEvolverAgent(); // singleton

const mutations: EvolverMutation[] = evolver.evolve(insights, config);
const applied = evolver.applyMutations(config, mutations);   // idempotent, oldValue must match
const reverted = evolver.revertMutations(config, mutations); // only if current === newValue
evolver.createPredictions(mutations, exp, taskTypes);        // falsifiable predictions

// One-shot loop with a 60s cooldown (EVOLVER_COOLDOWN_MS)
const cycle: EvolutionCycle = evolver.runCycle(insights, config, exp, taskTypes);
```

`applyMutations` es idempotente (omite mutaciones cuyo `oldValue` ya no coincide) y publica un evento `system.alert` `evolver-agent` por mutación; `runCycle` publica un evento `evolution_cycle`. Toda mutación puede revertirse mientras la configuración mantenga su `newValue`.

### Reglas de mutación por categoría de fallo

| FailureCategory | Mutación (dominio: configPath) |
|-----------------|-------------------------------|
| `hallucination` | `quality_gate: qualityGates.hallucination.threshold` × 0.9 |
| `context_overflow` | `thinking_budget: defaultThinkingBudget.maxThinkingTokens` × 0.75 · `subAgentThinkingTokens` × 0.75 |
| `timeout` | `runtime: maxParallelSubAgents` × 0.8 |
| `model_refusal` | `model_tier: modelTierMapping.MODERATE` = `power` |
| `missing_capability` | `model_tier: modelTierMapping.COMPLEX` = `consensus` |
| `planning_error` | `synthesis: defaultSynthesisConfig.maxRounds` × 1.5 (cap < 5) · `qualityGates.consistency.threshold` × 1.05 (cap < 0.95) |
| `dependency_failure` | `runtime: maxParallelSubAgents` × 0.75 (min > 1) |
| `quality_gate` | `quality_gate: qualityGates.accuracy.threshold` × 0.95 (must stay > 0.3) |
| `tool_misuse` | `runtime: maxParallelSubAgents` × 0.8 (min > 2) |
| `rate_limit` | `runtime` domain rule (cooldown/backoff) |
| `authentication` | `model_tier: modelTierMapping.MODERATE` = `power` |
| `resource_exhaustion` | `thinking_budget: defaultThinkingBudget.maxThinkingTokens` × 0.6 · `runtime: maxParallelSubAgents` × 0.5 |
| `data_validation` | `quality_gate: qualityGates.accuracy.threshold` × 1.05 |
| `unclassified` | no mutation |

Las mutaciones llevan guardas `minConfidence` y acotan los valores objetivo en rangos seguros, de modo que el evolucionador nunca puede llevar un umbral fuera de su envolvente operativa.

## Reflexión

Cada `reflectionFrequency` ejecuciones el aprendiz guarda un bloque de reflexión producido por `generateReflection(exp)`:

```text
[Reflection: SUCCESS]
Task: code-refactor · Strategy: PARALLEL · Model: gpt-4o
Duration: 12.4s · Cost: 1850 tokens
Lessons: split by file ownership, verify imports before parallel dispatch
Summary: ...
```

Los fallos producen bloques `[Reflection: FAILURE]` con un `errorHint` derivado del patrón de error y líneas de análisis que sugieren mitigaciones concretas (acceso a herramientas, nivel de modelo, modo de orquestación); un patrón repetido se marca para deprioritización.

## Bucle de auto-optimización

`EvolutionRunner` (interno al orquestador definitivo) cierra el bucle: lee `getMetaLearner().getSuggestions()` y, para sugerencias con confianza ≥ 0.3, reescribe la configuración viva del orquestador —cambiando entradas de `modelTierMapping` y ajustando el umbral de la puerta de calidad `consistency` hacia la estrategia sugerida— mientras publica eventos `system.alert` `self_optimization`.

## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests
- Firmas API exactas: monorepo / [API overview](/es/api/overview)

## Relacionado

- [Inteligencia](/es/architecture/intelligence)
- [Multi-agente](/es/architecture/multi-agent)
- [Reflection engine](/es/api/reflection-engine)
- [Analizador de complejidad de tareas](/es/api/task-complexity-analyzer)