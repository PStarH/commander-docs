# Transactions Saga

Commander implémente le **pattern saga** (compensation par étape) pour la cohérence multi-étapes.

## Architecture

```
SagaBuilder.define()
  │
  ├─ Step 1 → Compensation 1
  ├─ Step 2 → Compensation 2
  └─ Coordinator.execute
       ├─ succès : séquentiel
       └─ échec : compensations en ordre inverse
```

## SagaBuilder

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
  .build();
```

## Coordinator

Exécute dans l’ordre · compense à l’envers · états PENDING / COMPLETED / COMPENSATING / FAILED · DLQ si irrécupérable.

## WorkerPool

Étapes indépendantes en parallèle :

```typescript
const pool = new WorkerPool({ maxConcurrency: 5 });
pool.execute(steps);
```

## Tools

Les tools de mutation s’enregistrent dans le Compensation Registry. CLI : `saga` / `compensation` / `undo`.

```bash
npx tsx packages/core/src/cliEntry.ts doctor
```

## Voir aussi

- [Production readiness](/fr/architecture/production-readiness)  
- [Resilience](/fr/architecture/resilience)  
- [Tools](/fr/architecture/tools)  
