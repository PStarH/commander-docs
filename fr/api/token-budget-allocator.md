# Allocateur de budget tokens

Répartit le budget de tokens d'une exécution entre un agent principal (grand modèle, prise de décision) et des agents spécialistes (petit modèle, exécution), puis rapporte les tokens, coûts et économies obtenus par rapport à une exécution entièrement sur le modèle principal.

> **Source :** `packages/core/src/ultimateFramework.ts` (module Ultimate Framework).
> La racine du paquet `@commander/core` ré-exporte les types de support (`TokenBudgetAllocation`, `ModelTierConfig`, `AllocatedBudget`) et `DEFAULT_MODEL_CONFIG`, mais **pas** la classe `TokenBudgetAllocator` elle-même. Le runtime gère les budgets via le gestionnaire de budget de tokens (`getTokenBudgetManager()`) dans `packages/core/src/runtime/tokenBudgetManager.ts`.

## Idée centrale

- Le modèle principal (grand) prend les décisions : **40 %** des tokens
- Les modèles spécialistes (petits) exécutent : **50 %** des tokens
- Overhead de coordination : **10 %** des tokens

Cette répartition permet une **économie de 70 à 90 %** sans baisse de qualité mesurable.

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

Dans le monorepo, la classe s'importe depuis son module source :

```typescript
import { TokenBudgetAllocator } from 'packages/core/src/ultimateFramework';
```

Les applications ne devraient pas dépendre directement de la classe. Le runtime expose la gestion des budgets via `getTokenBudgetManager()` (`packages/core/src/runtime/tokenBudgetManager.ts`), utilisé par l'orchestrateur et l'exécuteur de sous-agents au moment de l'exécution.

## Exemple

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

**Clamping :** les tokens de chaque niveau sont bornés à la plage `minTokens..maxTokens` de son modèle (principal : 1000–32000, spécialiste : 500–16000). `savingsPercent` est plafonné à 0.

## Lié

- [Analyseur de complexité des tâches](/fr/api/task-complexity-analyzer)
- [Vue d'ensemble API](/fr/api/overview)
- [Runtime d'agents](/fr/architecture/agent-runtime)
