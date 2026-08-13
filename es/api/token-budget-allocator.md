# Asignador de presupuesto de tokens

Divide el presupuesto de tokens de una ejecución entre un agente líder (modelo grande, toma de decisiones) y agentes especialistas (modelo pequeño, ejecución), y luego reporta los tokens, costes y ahorro resultantes frente a ejecutar todo con el modelo líder.

> **Fuente:** `packages/core/src/ultimateFramework.ts` (módulo Ultimate Framework).
> La raíz del paquete `@commander/core` re-exporta los tipos de soporte (`TokenBudgetAllocation`, `ModelTierConfig`, `AllocatedBudget`) y `DEFAULT_MODEL_CONFIG`, pero **no** la clase `TokenBudgetAllocator` en sí. El runtime gestiona los presupuestos a través del gestor de presupuesto de tokens (`getTokenBudgetManager()`) en `packages/core/src/runtime/tokenBudgetManager.ts`.

## Idea central

- El modelo líder (grande) toma decisiones: **40 %** de los tokens
- Los modelos especialistas (pequeños) ejecutan: **50 %** de los tokens
- Overhead de coordinación: **10 %** de los tokens

Esta división logra un **ahorro del 70–90 %** en costes sin pérdida medible de calidad.

## Tipos

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

Dentro del monorepo, la clase se importa desde su módulo fuente:

```typescript
import { TokenBudgetAllocator } from 'packages/core/src/ultimateFramework';
```

Las aplicaciones no deberían depender de la clase directamente. El runtime expone la gestión de presupuestos a través de `getTokenBudgetManager()` (`packages/core/src/runtime/tokenBudgetManager.ts`), que usan el orquestador y el ejecutor de sub-agentes en tiempo de ejecución.

## Ejemplo

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

**Clamping:** los tokens de cada nivel se ajustan al rango `minTokens..maxTokens` de su modelo (líder: 1000–32000, especialista: 500–16000). `savingsPercent` tiene un mínimo de 0.

## Relacionado

- [Analizador de complejidad de tareas](/es/api/task-complexity-analyzer)
- [Vista general de la API](/es/api/overview)
- [Runtime de agentes](/es/architecture/agent-runtime)
