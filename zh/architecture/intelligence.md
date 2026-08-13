# 智能层

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/intelligence)



The Intelligence Layer provides internal agent capabilities that make Commander smarter over time. These are automatic systems — users see the results, not the mechanism.

## Components


| Component | Purpose | User sees |
|-----------|---------|-----------|
| **Cost Predictor** | Estimates task cost before execution | "Estimated $0.09, continue?" |
| **Failure Pattern Learner** | Learns from past failures | "You've hit this issue before" |
| **Impact Analyzer** | Predicts change side effects | "Changing this affects 3 files" |
| **Skill Extractor** | Extracts reusable patterns from successes | "Solution saved for reuse" |

## Cost Predictor


Estimates the cost of a task before execution using historical data from MetaLearner and deliberation estimates.

```typescript
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();

const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
  agentCount: 4,
});

console.log(`Estimated cost: $${estimate.estimatedCostUsd}`);
console.log(`Estimated duration: ${estimate.estimatedDurationMs}ms`);
console.log(`Confidence: ${estimate.confidence}`);
```

### Cost Breakdown


```
┌─────────────────────────────────┐
│         Total Estimate          │
├─────────────────────────────────┤
│  Deliberation:  $0.002         │
│  Execution:     $0.06          │
│  Synthesis:     $0.02          │
│  Quality Gates: $0.008         │
├─────────────────────────────────┤
│  Total:         $0.09          │
└─────────────────────────────────┘
```

## Failure Pattern Learner


Tracks failure patterns and provides proactive warnings about repeated mistakes.

```typescript
import { getFailurePatternLearner } from '@commander/core';

const learner = getFailurePatternLearner();

// Check for warnings before executing
const warnings = learner.checkPatterns({
  task: 'deploy to production',
  context: 'after database migration',
});

for (const warning of warnings) {
  console.log(`[${warning.severity}] ${warning.suggestion}`);
  // "You've deployed without running migrations 3 times before"
}
```

### Pattern Categories


| Category | Examples |
|----------|---------|
| `deploy` | Deploy without migration, missing env vars |
| `test` | Skipping tests, flaky test ignored |
| `config` | Wrong config format, missing required field |
| `dependency` | Breaking change in upgrade, missing peer dep |
| `security` | Hardcoded secret, exposed endpoint |

## Impact Analyzer


Analyzes code change impact before execution using AST analysis and dependency tracking.

```typescript
import { getImpactAnalyzer } from '@commander/core';

const analyzer = getImpactAnalyzer();

const impact = await analyzer.analyze('src/auth/login.ts');

console.log(`Direct dependencies: ${impact.directDependencies.length}`);
console.log(`Indirect dependencies: ${impact.indirectDependencies.length}`);
console.log(`Affected tests: ${impact.affectedTests.length}`);
console.log(`Risk level: ${impact.riskLevel}`);
// "Changing this affects 3 files, 2 test suites, risk: medium"
```

### Risk Levels


| Level | Criteria |
|-------|----------|
| `low` | No dependencies, no tests affected |
| `medium` | Few direct dependencies or tests affected |
| `high` | Many indirect dependencies or critical path |
| `critical` | Core module, many dependents, security-sensitive |

## Skill Extractor


Automatically extracts reusable skills from successful executions.

```typescript
import { getSkillExtractor } from '@commander/core';

const extractor = getSkillExtractor();

// After a successful run, extract skills
const result = await extractor.extract({
  runId: 'run-123',
  task: 'fix the failing test',
  success: true,
});

if (result.extracted) {
  console.log(`Skill extracted: ${result.skill.name}`);
  // "fix-failing-test: Analyze error → check imports → run test → fix"
}
```

### Skill Lifecycle


```
Successful execution → Pattern extraction → Skill created
                                                    │
                                    ┌───────────────┘
                                    ▼
                            Used in future tasks
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
              High usage      Low usage       30 days unused
              (confidence↑)   (confidence→)   (decay starts)
```

### Skill Decay


Skills decay over time if unused:
- **30 days** without use → decay starts
- **0.05 confidence/day** reduction
- **Below 0.2 confidence** → auto-pruned

## 配置


| Module | Setting | Default | Description |
|--------|---------|---------|-------------|
| Cost Predictor | `historySize` | `100` | Max historical records per task type |
| Failure Patterns | `patternsPath` | `.commander/intelligence/failure-patterns.json` | Persistence path |
| Impact Analyzer | `scanIntervalMs` | `60000` | Re-scan dependency graph interval |
| Skill Extractor | `decayDays` | `30` | Days before skill starts decaying |
| Skill Extractor | `minConfidence` | `0.2` | Below this, skill is pruned |
