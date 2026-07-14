# Árbol de supervisión

Documentación en español de **Árbol de supervisión**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
                    ┌──────────────────┐
                    │  Root Supervisor │
                    │  (strategy: one_for_one) │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Agent 1  │  │ Agent 2  │  │ Agent N  │
        │ (child)  │  │ (child)  │  │ (child)  │
        └──────────┘  └──────────┘  └──────────┘
```

```typescript
import { Supervisor } from '@commander/core';

const supervisor = new Supervisor({
  id: 'agent-pool',
  strategy: 'one_for_one',
  maxRestarts: 10,           // Max restarts across ALL children
  maxRestartIntervalMs: 60000, // Within this time window
  defaultShutdownMs: 5000,    // Graceful shutdown timeout
  publishEvents: true,        // Publish to message bus
});
```

```typescript
const handle = await supervisor.startChild({
  id: 'agent-1',
  start: async () => {
    const runtime = await createAgentRuntime({ /* config */ });
    return {
      id: 'agent-1',
      isAlive: () => runtime.isRunning(),
      healthCheck: async () => runtime.healthCheck(),
    };
  },
  stop: async (handle) => {
    await runtime.shutdown();
  },
  shutdownMs: 10000,
  maxRestarts: 5,
  maxRestartIntervalMs: 30000,
});
```

| Strategy | Behavior | Use when |
|----------|----------|----------|
| `one_for_one` | Restart only the crashed child | Children are independent |
| `one_for_all` | Restart ALL children | Children are co-dependent |
| `rest_for_one` | Restart crashed child + all children started after it | Children have startup order dependencies |


| Event | Description |
|-------|-------------|
| `child_started` | Child successfully started |
| `child_crashed` | Child process crashed |
| `child_restarted` | Child restarted after crash |
| `child_stopped` | Child gracefully stopped |
| `supervisor_crashed` | Supervisor exceeded restart limit |
| `supervisor_recovered` | Supervisor recovered from crash |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
