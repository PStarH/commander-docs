# Architecture V2 Migration

**Architecture V2 Migration.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Plane | Responsibility |
|-------|----------------|
| **Gateway (control)** | Accept runs, schedule WorkGraphs, lifecycle (pause/resume/cancel) — **does not** execute agents in pure V2 |
| **Worker (execution)** | Claim steps, run agents/tools, report results |
| **Kernel storage** | PostgreSQL tables for runs, steps, events |


## Contenu principal

### Mental model

En pratique, **Mental model** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Feature flags / env

En pratique, **Feature flags / env** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Route mapping

En pratique, **Route mapping** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Storage migration

En pratique, **Storage migration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Worker sketch

En pratique, **Worker sketch** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Rollout strategy

En pratique, **Rollout strategy** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### When you can stay on V1-style local CLI

En pratique, **When you can stay on V1-style local CLI** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

### Voir aussi

En pratique, **Related** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/migration-v2) pour le détail exhaustif.

## Exemples (code inchangé)

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# start worker process — see monorepo worker-plane package
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
