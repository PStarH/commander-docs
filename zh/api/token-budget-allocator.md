# Token 预算分配器

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/api/token-budget-allocator)



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
