# Task Complexity Analyzer

Analyzes task complexity and selects the optimal orchestration mode.

## Types

```typescript
type ComplexityLevel = 'trivial' | 'simple' | 'moderate' | 'complex' | 'extreme';
type OrchestrationMode = 'SEQUENTIAL' | 'PARALLEL' | 'HANDOFF' | 'MAGENTIC' | 'CONSENSUS';

interface ComplexityScore {
  level: ComplexityLevel;
  score: number;           // 0-100
  factors: ComplexityFactors;
  recommendedMode: OrchestrationMode;
  tokenBudget: TokenBudget;
  confidence: number;      // 0-1
}

interface ComplexityFactors {
  treewidth: number;       // Dependency complexity (0-100)
  dependencyDepth: number; // How deep dependencies go (0-100)
  inputSize: number;       // Token count of input
  outputComplexity: number;// Expected output structure (0-100)
  domainKnowledge: number; // Need for specialized knowledge (0-100)
  riskLevel: number;       // Failure impact (0-100)
  uncertaintyLevel: number;// Ambiguity in requirements (0-100)
  timeConstraints: number; // Deadline pressure (0-100)
}
```

## API

```typescript
const analyzer = new TaskComplexityAnalyzer();

// Analyze single task
const score = analyzer.analyze(task: Task): ComplexityScore;

// Batch analysis
const scores = batchAnalyzer.analyzeBatch(tasks: Task[]): ComplexityScore[];

// Get orchestration recommendation
const orch = batchAnalyzer.getBatchOrchestration(scores): {
  mode: OrchestrationMode;
  totalBudget: number;
  parallelGroups: number;
};
```

## Mode Selection Rules

| Condition | Mode |
|-----------|------|
| Complexity > 80 | CONSENSUS |
| Complexity > 60 + no dependencies | MAGENTIC |
| Complexity > 50 | HANDOFF |
| Has dependencies + complexity > 30 | HANDOFF |
| No dependencies + complexity < 30 | PARALLEL |
| Default | SEQUENTIAL |
