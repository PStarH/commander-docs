# Token Budget Allocator

Splits a run's token budget between a lead agent (large model, decision-making) and specialist agents (small model, execution), then reports the resulting tokens, cost, and savings versus running everything on the lead model alone.

> **Source:** `packages/core/src/ultimateFramework.ts` (Ultimate Framework module).
> The `@commander/core` package root re-exports the supporting types (`TokenBudgetAllocation`, `ModelTierConfig`, `AllocatedBudget`) and `DEFAULT_MODEL_CONFIG`, but **not** the `TokenBudgetAllocator` class itself. The runtime manages budgets through the token budget manager (`getTokenBudgetManager()`) in `packages/core/src/runtime/tokenBudgetManager.ts`.

## Core idea

- Lead (large) model makes decisions: **40%** of tokens
- Specialist (small) models do execution: **50%** of tokens
- Coordination overhead: **10%** of tokens

This split achieves **70–90% cost savings** with no measurable quality drop.

## Types

```typescript
interface TokenBudgetAllocation {
  leadAgent: number;        // fraction for the lead model (e.g. 0.4)
  specialistAgents: number; // fraction for specialist models (e.g. 0.5)
  overhead: number;         // coordination overhead (e.g. 0.1)
}

interface ModelTierConfig {
  leadModel: {
    name: string;
    minTokens: number;
    maxTokens: number;
    costPerToken: number;
  };
  specialistModel: {
    name: string;
    minTokens: number;
    maxTokens: number;
    costPerToken: number;
  };
}

const DEFAULT_MODEL_CONFIG: ModelTierConfig = {
  leadModel: {
    name: 'claude-opus-4',
    minTokens: 1000,
    maxTokens: 32000,
    costPerToken: 0.000015, // $15 / 1M tokens
  },
  specialistModel: {
    name: 'claude-sonnet-4',
    minTokens: 500,
    maxTokens: 16000,
    costPerToken: 0.000003, // $3 / 1M tokens
  },
};

interface AllocatedBudget {
  leadAgent: { model: string; tokens: number; cost: number };
  specialistAgents: { model: string; tokens: number; cost: number };
  overhead: { tokens: number };
  total: { tokens: number; cost: number };
  savings: {
    pureLeadCost: number;
    actualCost: number;
    savingsPercent: number;
  };
}
```

## API

```typescript
class TokenBudgetAllocator {
  constructor(totalBudget?: number, config?: ModelTierConfig);
  // totalBudget defaults to 100_000; config defaults to DEFAULT_MODEL_CONFIG

  allocate(allocation: TokenBudgetAllocation): AllocatedBudget;
  // Splits the budget by fraction, clamps each tier to its model's
  // minTokens..maxTokens range, computes per-model cost and savings.

  getRecommendedBudget(complexity: TaskComplexity): number;
  // base 50_000 × { LOW: 1, MEDIUM: 2, HIGH: 4, CRITICAL: 8 }
}
```

### Import

Inside the monorepo, the class is imported from its source module:

```typescript
import { TokenBudgetAllocator } from 'packages/core/src/ultimateFramework';
```

Applications should not rely on the class directly. The runtime exposes budget management through `getTokenBudgetManager()` (`packages/core/src/runtime/tokenBudgetManager.ts`), which the orchestrator and sub-agent executor use at run time.

## Example

```typescript
import { TokenBudgetAllocator } from 'packages/core/src/ultimateFramework';
import type { TaskComplexity } from 'packages/core/src/models/taskComplexity';

const allocator = new TokenBudgetAllocator(); // 100_000 tokens, default config

const budget = allocator.allocate({
  leadAgent: 0.4,
  specialistAgents: 0.5,
  overhead: 0.1,
});

// budget.leadAgent        → { model: 'claude-opus-4',  tokens: 40_000, cost: 0.60 }
// budget.specialistAgents → { model: 'claude-sonnet-4', tokens: 50_000, cost: 0.15 }
// budget.total.cost       → 0.75
// budget.savings.savingsPercent → ~75% vs. pure lead model

const complexity: TaskComplexity = { level: 'HIGH' };
const recommended = allocator.getRecommendedBudget(complexity); // 50_000 × 4 = 200_000
```

**Clamping:** each tier's token count is clamped into the model's `minTokens..maxTokens` range (lead: 1000–32000, specialist: 500–16000). `savingsPercent` is floored at 0.

## See also

- [Task Complexity Analyzer](/api/task-complexity-analyzer)
- [API overview](/api/overview)
- [Agent runtime](/architecture/agent-runtime)
