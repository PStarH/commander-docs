# Task Complexity Analyzer

**Task Complexity Analyzer.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Condition | Topology |
|-----------|----------|
| Complexity > 80 | REVIEW |
| Complexity > 60 + no dependencies | DISPATCH |
| Complexity > 50 | ORCHESTRATOR |
| Has dependencies + complexity > 30 | CHAIN |
| No dependencies + complexity < 30 | DISPATCH |
| Default | CHAIN |


## 주요 내용

### Types

운영 시 **Types** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/task-complexity-analyzer)를 보세요.

### API

운영 시 **API** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/task-complexity-analyzer)를 보세요.

### Topology Selection Rules

운영 시 **Topology Selection Rules** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/task-complexity-analyzer)를 보세요.

## 예제 (코드는 영어 유지)

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

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
