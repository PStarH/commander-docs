# Saga Transactions

**Saga Transactions.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Policy | Behavior |
|--------|----------|
| No retry | Fail immediately, begin compensation |
| Fixed retries | Retry N times with fixed delay |
| Exponential backoff | Retry with doubling delay, up to max |
| Circuit breaker | Use shared circuit breaker state |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### SagaBuilder

En pratique, **SagaBuilder** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### Coordinator

En pratique, **Coordinator** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### WorkerPool

En pratique, **WorkerPool** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### Checkpointer

En pratique, **Checkpointer** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### ApprovalManager

En pratique, **ApprovalManager** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### RetryController

En pratique, **RetryController** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

### Stores

En pratique, **Stores** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/saga) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
