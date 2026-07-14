# Supervision Tree

**Supervision Tree.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Strategy | Behavior | Use when |
|----------|----------|----------|
| `one_for_one` | Restart only the crashed child | Children are independent |
| `one_for_all` | Restart ALL children | Children are co-dependent |
| `rest_for_one` | Restart crashed child + all children started after it | Children have startup order dependencies |


## Contenu principal

### Why Supervision Trees

En pratique, **Why Supervision Trees** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Restart Strategies

En pratique, **Restart Strategies** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Adding Children

En pratique, **Adding Children** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Restart Intensity

En pratique, **Restart Intensity** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Supervision Events

En pratique, **Supervision Events** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### Health Checks

En pratique, **Health Checks** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

### API Reference

En pratique, **API Reference** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/supervision-tree) pour le détail exhaustif.

## Exemples (code inchangé)

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
