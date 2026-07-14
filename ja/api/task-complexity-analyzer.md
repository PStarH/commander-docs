# Task Complexity Analyzer

**Task Complexity Analyzer.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Condition | Topology |
|-----------|----------|
| Complexity > 80 | REVIEW |
| Complexity > 60 + no dependencies | DISPATCH |
| Complexity > 50 | ORCHESTRATOR |
| Has dependencies + complexity > 30 | CHAIN |
| No dependencies + complexity < 30 | DISPATCH |
| Default | CHAIN |


## 主な節

### Types

**Types** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### API

**API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Topology Selection Rules

**Topology Selection Rules** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

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

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
