# Task Complexity Analyzer

Analyzes task complexity and selects the optimal orchestration mode.

## Types

```typescript
type ComplexityLevel = 'trivial' | 'simple' | 'moderate' | 'complex' | 'extreme';

type OrchestrationMode =
  | 'SEQUENTIAL'  // Low complexity, single thread
  | 'PARALLEL'    // Independent subtasks
  | 'HANDOFF'     // Needs expert
  | 'MAGENTIC'    // Open exploration
  | 'CONSENSUS';  // High-risk decision

interface ComplexityScore {
  level: ComplexityLevel;
  score: number;              // 0-100
  factors: ComplexityFactors;
  recommendedMode: OrchestrationMode;
  tokenBudget: TokenBudget;
  confidence: number;         // 0-1
}

interface ComplexityFactors {
  treewidth: number;          // Dependency complexity (0-100)
  dependencyDepth: number;    // How deep dependencies go (0-100)
  inputSize: number;          // Token count of input
  outputComplexity: number;   // Expected output structure (0-100)
  domainKnowledge: number;    // Need for specialized knowledge (0-100)
  riskLevel: number;          // Failure impact (0-100)
  uncertaintyLevel: number;   // Ambiguity in requirements (0-100)
  timeConstraints: number;    // Deadline pressure (0-100)
}

interface TokenBudget {
  leadAgent: number;          // Percentage for lead agent
  specialistAgents: number;   // Percentage for specialists
  evaluation: number;         // Percentage for evaluation
  overhead: number;           // Percentage for orchestration
  total: number;              // Total budget
}

interface Task {
  id: string;
  description: string;
  input?: string;
  context?: string;
  constraints?: string[];
  deadline?: Date;
  riskLevel?: 'low' | 'medium' | 'high' | 'critical';
}
```

## API

```typescript
import { TaskComplexityAnalyzer } from '@commander/core';
// BatchComplexityAnalyzer lives in packages/core/src/taskComplexityAnalyzer.ts
// and is not re-exported from the '@commander/core' package root.
import { BatchComplexityAnalyzer } from 'packages/core/src/taskComplexityAnalyzer';

// Analyze a single task
const analyzer = new TaskComplexityAnalyzer();
const score = analyzer.analyze(task); // → ComplexityScore

// Batch analysis
const batchAnalyzer = new BatchComplexityAnalyzer();
const scores = batchAnalyzer.analyzeBatch(tasks); // → ComplexityScore[]

// Get orchestration recommendation
const orch = batchAnalyzer.getBatchOrchestration(scores);
// → { mode: OrchestrationMode; totalBudget: number; parallelGroups: number }
```

Factor weights (weighted sum → 0-100 score): treewidth 0.2 · dependencyDepth 0.15 · inputSize 0.1 · outputComplexity 0.15 · domainKnowledge 0.15 · riskLevel 0.1 · uncertaintyLevel 0.1 · timeConstraints 0.05.

`scoreToLevel` thresholds: `< 15` trivial · `< 30` simple · `< 50` moderate · `< 75` complex · else extreme.

## Mode Selection Rules

High-priority factors win over the level-based default (checked in order):

| Condition | Orchestration Mode |
|-----------|--------------------|
| `riskLevel >= 75` | CONSENSUS |
| `uncertaintyLevel >= 60` | MAGENTIC |
| `domainKnowledge >= 70` | HANDOFF |
| Level `trivial` / `simple` | SEQUENTIAL |
| Level `moderate` + `treewidth < 30` | PARALLEL |
| Level `moderate` (otherwise) | SEQUENTIAL |
| Level `complex` + `dependencyDepth > 50` | HANDOFF |
| Level `complex` (otherwise) | PARALLEL |
| Level `extreme` | MAGENTIC |

## Token Budgets

Base total by complexity level:

| Level | Base total |
|-------|-----------|
| trivial | 1000 |
| simple | 3000 |
| moderate | 10000 |
| complex | 30000 |
| extreme | 100000 |

Mode multiplier and split (lead / specialists / evaluation / overhead):

| Mode | Multiplier | Split |
|------|-----------|-------|
| SEQUENTIAL | ×1 | 70 / 10 / 15 / 5 |
| PARALLEL | ×1.5 | 30 / 50 / 15 / 5 |
| HANDOFF | ×1.3 | 35 / 45 / 15 / 5 |
| MAGENTIC | ×2 | 40 / 35 / 15 / 10 |
| CONSENSUS | ×1.5 | 30 / 30 / 35 / 5 |

Confidence starts at 1.0 and loses 0.05 per mid-range factor (30-70), floored at 0.5.

## Batch Orchestration

`getBatchOrchestration(scores)`:

- Any task recommending `CONSENSUS` → whole batch runs `CONSENSUS`, `parallelGroups: 1`
- All tasks `trivial`/`simple` → `PARALLEL`, total budget ×0.8 (parallel efficiency), `parallelGroups: scores.length`
- Otherwise → highest-score task's mode, `parallelGroups: scores.length` when `PARALLEL` else `1`