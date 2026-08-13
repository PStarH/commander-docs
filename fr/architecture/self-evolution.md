# Auto-évolution (Self-Evolution)

Commander s'améliore tout seul grâce au **méta-apprentissage** : un sélecteur de stratégies fondé sur l'échantillonnage de Thompson apprend quelle stratégie d'orchestration fonctionne le mieux par type de tâche, tandis qu'un analyseur de trajectoires classe les échecs et qu'un agent évolutif propose des mutations de configuration. Tout l'état est inspectable via la façade `MetaLearner`.

## Architecture

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

## Types

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

Le méta-apprenant est une façade sur cinq sous-modules : `StrategySelector` (échantillonnage de Thompson), `CrossModelMemory` (a priori par modèle), `PredictionLoop` (prédictions falsifiables), `RegressionGate` (détection de chutes du taux de succès), `StrategyPerformanceTracker`, plus le moteur de réflexion et un moteur de suggestions.

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

`selectStrategy` renvoie `'SEQUENTIAL'` tant que l'apprenant est désactivé ou qu'il a moins de `minRunsBeforeLearning` (50 par défaut) expériences ; ensuite il délègue au sélecteur par échantillonnage de Thompson.

### Introspection

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

### Configuration

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

## Sélection de stratégie (échantillonnage de Thompson)

Chaque type de tâche maintient un a priori `BetaDistribution` par stratégie. La sélection échantillonne chaque a priori et le multiplie par un bonus d'exploration, un facteur de vitesse et un facteur de coût.

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

- `update(success, taskDifficulty)` pondère la mise à jour Beta par `0.5 + (1 − difficulty) × 0.5`, de sorte que les tâches plus difficiles apportent moins de signal.
- L'exploration utilise UCB1 : poids `0.5` tant qu'une stratégie a moins de 20 échantillons, `0.2` ensuite.
- Les facteurs de vitesse sont plafonnés à `[0.7, 1.3]` et ne s'appliquent que lorsque chaque stratégie a ≥ 3 exécutions et qu'au moins 2 stratégies exposent une latence p95 ; les facteurs de coût sont plafonnés à `[0.8, 1.2]`.
- Les a priori Thompson sont bornés par `MAX_THOMPSON_PRIORS = 200` par clé modèle/type-de-tâche (le plus ancien est expulsé en premier).

`STRATEGY_NAMES` (le vocabulaire du méta-apprenant) est distinct de `OrchestrationTopology` : il reste fixé à `['SEQUENTIAL', 'PARALLEL', 'HANDOFF', 'MAGENTIC', 'CONSENSUS']`.

## TrajectoryAnalyzer

Classe les exécutions terminées en catégories d'échec sans coût d'exécution par défaut. Le mode décide quand un LLM intervient.

```typescript
import { TrajectoryAnalyzer } from '@commander/core';

// light:      heuristic-only, zero LLM calls (default)
// balanced:   heuristic first, LLM fallback for unclassified failures
// thorough:   LLM for every failure; successes always heuristic
const analyzer = new TrajectoryAnalyzer('light', provider?, model?);

const insights: EvolutionInsight[] = await analyzer.analyze(experiences);
```

- **Classifieur heuristique** : balaye `errorPattern + lessons + toolsUsed + topology + taskType` contre 13 règles de mots-clés (p. ex. `timeout` → `timeout`, `429`/`rate limit` → `rate_limit`, `out of memory` → `resource_exhaustion`). La confiance de base par règle est de 0.55–0.85, avec un incrément de `+0.05` par mot-clé correspondant (plafond `+0.2`, total maximal `0.95`).
- **Classifieur LLM** : un prompt en JSON seul (température 0.1, maxTokens 300) renvoie `{ category, confidence, evidence, suggestion }` ; les réponses qui échouent à la validation de forme sont ignorées et les erreurs du LLM retombent sur `unclassified / 0.3`.
- Les exécutions réussies produisent toujours un insight avec `failureCategory: 'unclassified'`, `confidence: 1`, `evidence: []`.

## EvolverAgent

Propose des mutations de configuration à partir des insights analysés. L'évolueur ne fait que *planifier* des mutations — `evolve` ne mute jamais la configuration ; appelez `applyMutations` explicitement.

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

`applyMutations` est idempotent (il saute les mutations dont le `oldValue` ne correspond plus) et publie un événement `system.alert` `evolver-agent` par mutation ; `runCycle` publie un événement `evolution_cycle`. Toute mutation peut être annulée tant que la configuration conserve son `newValue`.

### Règles de mutation par catégorie d'échec

| FailureCategory | Mutation (domaine : configPath) |
|-----------------|--------------------------------|
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

Les mutations portent des gardes `minConfidence` et bornent les valeurs cibles dans des plages sûres, de sorte que l'évolueur ne peut jamais sortir un seuil de son enveloppe opérationnelle.

## Réflexion

Toutes les `reflectionFrequency` exécutions, l'apprenant enregistre un bloc de réflexion produit par `generateReflection(exp)` :

```text
[Reflection: SUCCESS]
Task: code-refactor · Strategy: PARALLEL · Model: gpt-4o
Duration: 12.4s · Cost: 1850 tokens
Lessons: split by file ownership, verify imports before parallel dispatch
Summary: ...
```

Les échecs produisent des blocs `[Reflection: FAILURE]` avec un `errorHint` dérivé du motif d'erreur et des lignes d'analyse suggérant des mitigations concrètes (accès aux outils, niveau de modèle, mode d'orchestration) ; un motif répété est marqué pour dépriorisation.

## Boucle d'auto-optimisation

`EvolutionRunner` (interne à l'orchestrateur ultime) ferme la boucle : il lit `getMetaLearner().getSuggestions()` et, pour les suggestions de confiance ≥ 0.3, réécrit la configuration vivante de l'orchestrateur — en changeant les entrées de `modelTierMapping` et en ajustant le seuil de la porte de qualité `consistency` vers la stratégie suggérée — tout en publiant des événements `system.alert` `self_optimization`.

## Voir aussi

- [Intelligence](/fr/architecture/intelligence)
- [Multi-agents](/fr/architecture/multi-agent)
- [Moteur de réflexion](/fr/api/reflection-engine)
- [Analyseur de complexité des tâches](/fr/api/task-complexity-analyzer)