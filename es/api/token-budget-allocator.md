# Asignador de presupuesto de tokens

Documentación en español de **Asignador de presupuesto de tokens**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Topology | Lead | Specialists | Evaluation | Overhead |
|----------|------|-------------|------------|----------|
| SINGLE | 95% | 0% | 5% | 0% |
| CHAIN | 30% | 50% | 15% | 5% |
| DISPATCH | 15% | 65% | 15% | 5% |
| ORCHESTRATOR | 35% | 45% | 15% | 5% |
| REVIEW | 25% | 30% | 40% | 5% |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
