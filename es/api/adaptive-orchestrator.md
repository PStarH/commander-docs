# Orquestador adaptativo

Documentación en español de **Orquestador adaptativo**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```typescript
interface Agent {
  id: string;
  name: string;
  role: string;
  capabilities: string[];
  load: number;         // 0-1
  successRate: number;  // 0-1
  isAvailable: boolean;
}

interface OrchestrationPlan {
  id: string;
  mode: OrchestrationMode;
  tasks: Task[];
  agents: Agent[];
  resourceAllocation: ResourceAllocation;
  estimatedDuration: number;
}

interface ResourceAllocation {
  leadAgentId?: string;
  specialistAgentIds: string[];
  maxConcurrent: number;
  tokenBudget: {
    lead: number;
    specialists: number;
    evaluation: number;
    overhead: number;
  };
}
```

```typescript
const orchestrator = new AdaptiveOrchestrator();

// Register agents
const agentId = orchestrator.registerAgent(
  agent: Omit<Agent, 'load' | 'successRate' | 'isAvailable'>
): string;

// Create plan
const plan = orchestrator.createPlan(
  tasks: Task[],
  suggestedMode?: OrchestrationMode
): OrchestrationPlan;

// Execute plan
const results = await orchestrator.execute(plan): Map<string, Task>;

// Get metrics
const metrics = orchestrator.getMetrics(): ExecutionMetrics;

// Adapt plan based on metrics
const adaptedPlan = orchestrator.adapt(plan: OrchestrationPlan): OrchestrationPlan;
```



## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
