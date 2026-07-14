# Multi-Tenant Architecture

**Multi-Tenant Architecture.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Layer | Mechanism |
|-------|-----------|
| Rate limits | Per-tenant: requests/minute |
| Concurrency | Per-tenant: max concurrent runs |
| Storage | Per-tenant directory paths |
| Memory | Per-instance ThreeLayerMemory |
| Cache | SHA-256 key includes tenantId |
| Metrics | Every counter/gauge/histogram has `tenant` label |


## Contenu principal

### Request Flow

En pratique, **Request Flow** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/multi-tenancy) pour le détail exhaustif.

### Isolation Layers

En pratique, **Isolation Layers** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/multi-tenancy) pour le détail exhaustif.

### Providers

En pratique, **Providers** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/multi-tenancy) pour le détail exhaustif.

### Tenant Config

En pratique, **Tenant Config** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/multi-tenancy) pour le détail exhaustif.

## Exemples (code inchangé)

```
Request → HttpServer
           │
           ├─ authenticate()           ← Bearer token → tenant mapping
           ├─ resolveTenantFromAuth()  ← API key → tenantId
           │
           └─ execute({ tenantId }) → AgentRuntime
                                        │
                                        ├─ TenantProvider.getTenantConfig(tenantId)
                                        │   → per-tenant: tokenBudget, maxConcurrency, maxRunsPerMinute
                                        │
                                        ├─ Rate limit check     → TENANT_RATE_LIMIT
                                        ├─ Concurrency check    → TENANT_CONCURRENCY_LIMIT
                                        │
                                        └─ Tenant-scoped instances:
                                            ├─ SamplesStore(path/tenant_{id}/)
                                            ├─ TraceStore(path/tenant_{id}/)
                                            ├─ StateCheckpointer(path/tenant_{id}/)
                                            ├─ ThreeLayerMemory(per-instance)
                                            └─ ToolResultCache(key = SHA256(tenantId + tool + args))
```

```typescript
interface TenantConfig {
  tenantId: string;
  tokenBudget: number;
  maxConcurrency: number;
  maxRunsPerMinute: number;
  enabled: boolean;
  workspacePath?: string;
}
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
