# 토큰 예산 할당기

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/api/token-budget-allocator)



Allocates token budgets across agents based on topology and task complexity.

## Types


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

## API


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

## Allocation by Topology


| Topology | Lead | Specialists | Evaluation | Overhead |
|----------|------|-------------|------------|----------|
| SINGLE | 95% | 0% | 5% | 0% |
| CHAIN | 30% | 50% | 15% | 5% |
| DISPATCH | 15% | 65% | 15% | 5% |
| ORCHESTRATOR | 35% | 45% | 15% | 5% |
| REVIEW | 25% | 30% | 40% | 5% |
