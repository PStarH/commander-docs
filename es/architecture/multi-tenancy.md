# Multi-tenant

Documentación en español de **Multi-tenant**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Layer | Mechanism |
|-------|-----------|
| Rate limits | Per-tenant: requests/minute |
| Concurrency | Per-tenant: max concurrent runs |
| Storage | Per-tenant directory paths |
| Memory | Per-instance ThreeLayerMemory |
| Cache | SHA-256 key includes tenantId |
| Metrics | Every counter/gauge/histogram has `tenant` label |


| Provider | Behavior |
|----------|----------|
| `NullTenantProvider` | No isolation, backward compatible (single-tenant) |
| `SimpleTenantProvider` | Static config map of tenant → config |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
