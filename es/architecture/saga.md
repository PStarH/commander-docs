# Transacciones Saga

Documentación en español de **Transacciones Saga**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
SagaBuilder.define()
  │
  ├─ Step 1: Create resource   → Compensation: Delete resource
  ├─ Step 2: Update resource   → Compensation: Revert update
  ├─ Step 3: Send notification → Compensation: Void notification
  │
  └─ Coordinator.execute(saga)
       │
       ├─ Step 1 → success
       ├─ Step 2 → success
       ├─ Step 3 → FAILURE
       │
       └─ Compensate
            ├─ Undo Step 2 (revert update)
            └─ Undo Step 1 (delete resource)
```

```typescript
const saga = new SagaBuilder('deploy-service')
  .step('create-dir', async (ctx) => {
    await fs.mkdir(ctx.path);
  }, {
    compensate: async (ctx) => {
      await fs.rmdir(ctx.path);
    },
  })
  .step('write-config', async (ctx) => {
    await fs.writeFile(ctx.path, ctx.config);
  }, {
    compensate: async (ctx) => {
      await fs.unlink(ctx.path);
    },
  })
  .step('restart-service', async (ctx) => {
    await service.restart();
  }, {
    compensate: async (ctx) => {
      await service.restore(ctx.prevVersion);
    },
  })
  .build();
```

```typescript
const pool = new WorkerPool({ maxConcurrency: 5 });
pool.execute(steps);  // Independent steps run in parallel
```

| Policy | Behavior |
|--------|----------|
| No retry | Fail immediately, begin compensation |
| Fixed retries | Retry N times with fixed delay |
| Exponential backoff | Retry with doubling delay, up to max |
| Circuit breaker | Use shared circuit breaker state |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
