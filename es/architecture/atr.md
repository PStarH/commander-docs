# Agent Transaction Runtime

Documentación en español de **Agent Transaction Runtime**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
Agent Decision → ATR Settlement Layer → External System
                    ├── Idempotency (no duplicates)
                    ├── Recovery (compensable rollback)
                    ├── Leasing (single-owner runs)
                    └── Fencing (zombie process protection)
```

```
PENDING → EXECUTING → VERIFYING → COMMITTED
               │            │
               │            └──→ ABORTED → COMPENSATED
               └───────────────────→ ABORTED → COMPENSATED
```

```typescript
import { IdempotencyStore } from '@commander/core';

const store = new IdempotencyStore({ ttlSeconds: 3600 });

// First execution — runs the action
const result = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});

// Retry with same key — returns cached result, no side effect
const cached = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});
```

| Setting | Default | Description |
|---------|---------|-------------|
| `idempotency.ttlSeconds` | `3600` | How long to retain idempotency records |
| `lease.ttlMs` | `30000` | Lease time-to-live |
| `lease.heartbeatMs` | `5000` | Heartbeat interval |
| `compensation.timeoutMs` | `10000` | Max time per compensation handler |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
