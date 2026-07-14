# Token Budget Allocator

**Token Budget Allocator.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Topology | Lead | Specialists | Evaluation | Overhead |
|----------|------|-------------|------------|----------|
| SINGLE | 95% | 0% | 5% | 0% |
| CHAIN | 30% | 50% | 15% | 5% |
| DISPATCH | 15% | 65% | 15% | 5% |
| ORCHESTRATOR | 35% | 45% | 15% | 5% |
| REVIEW | 25% | 30% | 40% | 5% |


## 주요 내용

### Types

운영 시 **Types** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/token-budget-allocator)를 보세요.

### API

운영 시 **API** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/token-budget-allocator)를 보세요.

### Allocation by Topology

운영 시 **Allocation by Topology** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/token-budget-allocator)를 보세요.

## 예제 (코드는 영어 유지)

```typescript
interface TokenBudget {
  totalBudget: number;
  perAgentBudget: number;
  reservedForTools: number;
  reservedForVerification: number;
}

interface AllocationResult {
  lead: number;
  specialists: number;
  evaluation: number;
  overhead: number;
}
```

```typescript
const allocator = new TokenBudgetAllocator({ baseBudget: 100000 });

// Allocate based on topology
const budget = allocator.allocate(
  topology: Topology,
  complexity: number,
  agentCount: number
): TokenBudget;

// Get allocation breakdown
const allocation = allocator.getAllocation(
  topology: OrchestrationTopology,
  totalBudget: number
): AllocationResult;
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
