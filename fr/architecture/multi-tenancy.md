# Architecture multi-tenant

Commander isole les tenants **à chaque couche**.

## Flux de requête

```
Request → HttpServer
           │
           ├─ authenticate()           ← Bearer → mapping tenant
           ├─ resolveTenantFromAuth()  ← API key → tenantId
           │
           └─ execute({ tenantId }) → AgentRuntime
                                        │
                                        ├─ TenantProvider.getTenantConfig(tenantId)
                                        │   → tokenBudget, maxConcurrency, maxRunsPerMinute
                                        │
                                        ├─ Rate limit / Concurrency
                                        │
                                        └─ Instances scopées tenant :
                                            SamplesStore / TraceStore / StateCheckpointer
                                            ThreeLayerMemory / ToolResultCache(tenantId inclus)
```

## Couches d’isolation

| Couche | Mécanisme |
|--------|-----------|
| Rate limits | Req/min par tenant |
| Concurrency | Runs concurrent max par tenant |
| Storage | Répertoires par tenant |
| Memory | ThreeLayerMemory par instance |
| Cache | Clé SHA-256 avec tenantId |
| Metrics | Label `tenant` partout |

## Providers

| Provider | Comportement |
|----------|--------------|
| `NullTenantProvider` | Pas d’isolation (mono-tenant) |
| `SimpleTenantProvider` | Map statique tenant → config |

## TenantConfig

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

## Ops

```bash
export COMMANDER_API_KEY="long-random-secret"
npx tsx packages/core/src/cliEntry.ts doctor
curl -s http://localhost:4000/health/detailed
```

CLI local mono-machine : souvent `NullTenantProvider`. Prod partagée : Simple (ou custom) + quotas.

## Voir aussi

- [Security Gateway](/fr/architecture/security-gateway)  
- [Cache](/fr/architecture/caching)  
- [Production readiness](/fr/architecture/production-readiness)  
- [Sécurité](/fr/guide/security)  
