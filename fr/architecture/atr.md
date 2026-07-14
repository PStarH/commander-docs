# Agent Transaction Runtime (ATR)

**Agent Transaction Runtime (ATR).** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Setting | Default | Description |
|---------|---------|-------------|
| `idempotency.ttlSeconds` | `3600` | How long to retain idempotency records |
| `lease.ttlMs` | `30000` | Lease time-to-live |
| `lease.heartbeatMs` | `5000` | Heartbeat interval |
| `compensation.timeoutMs` | `10000` | Max time per compensation handler |


## Contenu principal

### Why ATR

En pratique, **Why ATR** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

### Core Concepts

En pratique, **Core Concepts** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

### GitHub Adapter

En pratique, **GitHub Adapter** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

### HTTP API

En pratique, **HTTP API** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/atr) pour le détail exhaustif.

## Exemples (code inchangé)

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
