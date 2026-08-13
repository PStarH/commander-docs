# 自进化

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/self-evolution)



Commander improves itself through **meta-learning**: a Thompson-Sampling strategy selector learns which orchestration strategy works per task type, while a trajectory analyzer classifies failures and an evolver agent proposes configuration mutations. All state is introspectable through a `MetaLearner` facade.

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


The meta-learner is a facade over five sub-modules: `StrategySelector` (Thompson Sampling), `CrossModelMemory` (per-model priors), `PredictionLoop` (falsifiable predictions), `RegressionGate` (success-rate drop detection), `StrategyPerformanceTracker`, plus the reflexion engine and a suggestion engine.

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

`selectStrategy` returns `'SEQUENTIAL'` while the learner is disabled or has fewer than `minRunsBeforeLearning` (default 50) experiences; after that it delegates to the Thompson-Sampling selector.

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

### Config


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

## Strategy Selection (Thompson Sampling)


Each task type keeps a `BetaDistribution` prior per strategy. Selection samples each prior, then multiplies by an exploration bonus, speed factor and cost factor.

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

- `update(success, taskDifficulty)` weights the Beta update by `0.5 + (1 − difficulty) × 0.5`, so harder tasks contribute less signal.
- Exploration uses UCB1: weight `0.5` while a strategy has fewer than 20 samples, `0.2` afterwards.
- Speed factors are capped to `[0.7, 1.3]` and only apply once each strategy has ≥ 3 runs and ≥ 2 strategies expose p95 latency; cost factors are capped to `[0.8, 1.2]`.
- Thompson priors are bounded by `MAX_THOMPSON_PRIORS = 200` per model/task-type key (oldest evicted first).

`STRATEGY_NAMES` (the meta-learner vocabulary) is distinct from `OrchestrationTopology`: it is fixed at `['SEQUENTIAL', 'PARALLEL', 'HANDOFF', 'MAGENTIC', 'CONSENSUS']`.

## TrajectoryAnalyzer


Classifies completed executions into failure categories at zero runtime cost by default. The mode decides when an LLM is involved.

```typescript
import { TrajectoryAnalyzer } from '@commander/core';

// light:      heuristic-only, zero LLM calls (default)
// balanced:   heuristic first, LLM fallback for unclassified failures
// thorough:   LLM for every failure; successes always heuristic
const analyzer = new TrajectoryAnalyzer('light', provider?, model?);

const insights: EvolutionInsight[] = await analyzer.analyze(experiences);
```

- **Heuristic classifier**: scans `errorPattern + lessons + toolsUsed + topology + taskType` against 13 keyword rules (e.g. `timeout` → `timeout`, `429`/`rate limit` → `rate_limit`, `out of memory` → `resource_exhaustion`). Base confidence per rule is 0.55–0.85, boosted `+0.05` per matching keyword (capped `+0.2`, total capped `0.95`).
- **LLM classifier**: a JSON-only prompt (temperature 0.1, maxTokens 300) returns `{ category, confidence, evidence, suggestion }`; responses failing shape validation are dropped, and LLM errors fall back to `unclassified / 0.3`.
- Successful runs always produce an insight with `failureCategory: 'unclassified'`, `confidence: 1`, `evidence: []`.

## EvolverAgent


Proposes configuration mutations from analyzed insights. The evolver only *plans* mutations — `evolve` never mutates config; call `applyMutations` explicitly.

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

`applyMutations` is idempotent (skips mutations whose `oldValue` no longer matches) and publishes a `system.alert` `evolver-agent` event per mutation; `runCycle` publishes an `evolution_cycle` event. Every mutation can be reverted as long as the config still holds its `newValue`.

### Mutation rules by failure category


| FailureCategory | Mutation (domain: configPath) |
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

Mutations carry `minConfidence` guards and clamp target values into safe ranges, so the evolver can never push a threshold outside its operating envelope.

## Reflexion


Every `reflectionFrequency` runs the learner stores a reflexion block produced by `generateReflection(exp)`:

```text
[Reflection: SUCCESS]
Task: code-refactor · Strategy: PARALLEL · Model: gpt-4o
Duration: 12.4s · Cost: 1850 tokens
Lessons: split by file ownership, verify imports before parallel dispatch
Summary: ...
```

Failures produce `[Reflection: FAILURE]` blocks with an `errorHint` derived from the error pattern and analysis lines that suggest concrete mitigations (tool access, model tier, orchestration mode); a pattern seen repeatedly is marked for deprioritization.

## Self-Optimization Loop


`EvolutionRunner` (internal to the ultimate orchestrator) closes the loop: it reads `getMetaLearner().getSuggestions()` and, for suggestions with confidence ≥ 0.3, rewrites the live orchestrator config — switching `modelTierMapping` entries and nudging the `consistency` quality-gate threshold toward the suggested strategy — while publishing `system.alert` `self_optimization` events.

## See also


- [Intelligence](/zh/architecture/intelligence)
- [Multi-agent](/zh/architecture/multi-agent)
- [Reflection engine](/zh/api/reflection-engine)
- [Task complexity analyzer](/zh/api/task-complexity-analyzer)
