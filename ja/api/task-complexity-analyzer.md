# タスク複雑度アナライザー

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/api/task-complexity-analyzer)



Analyzes task complexity and selects the optimal orchestration topology.

## Types


```typescript
type ComplexityLevel = 'trivial' | 'simple' | 'moderate' | 'complex' | 'extreme';
type Topology = 'SINGLE' | 'CHAIN' | 'DISPATCH' | 'ORCHESTRATOR' | 'REVIEW';

interface ComplexityScore {
  level: ComplexityLevel;
  score: number;           // 0-100
  factors: ComplexityFactors;
  recommendedTopology: Topology;
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
  topology: Topology;
  totalBudget: number;
  parallelGroups: number;
};
```

## Topology Selection Rules


| Condition | Topology |
|-----------|----------|
| Complexity > 80 | REVIEW |
| Complexity > 60 + no dependencies | DISPATCH |
| Complexity > 50 | ORCHESTRATOR |
| Has dependencies + complexity > 30 | CHAIN |
| No dependencies + complexity < 30 | DISPATCH |
| Default | CHAIN |
