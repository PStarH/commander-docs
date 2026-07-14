# Multi-Tenant Architecture

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/multi-tenancy)



Commander supports multi-tenant isolation at every layer.

## Request Flow


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

## Isolation Layers


| Layer | Mechanism |
|-------|-----------|
| Rate limits | Per-tenant: requests/minute |
| Concurrency | Per-tenant: max concurrent runs |
| Storage | Per-tenant directory paths |
| Memory | Per-instance ThreeLayerMemory |
| Cache | SHA-256 key includes tenantId |
| Metrics | Every counter/gauge/histogram has `tenant` label |

## 提供商


| Provider | Behavior |
|----------|----------|
| `NullTenantProvider` | No isolation, backward compatible (single-tenant) |
| `SimpleTenantProvider` | Static config map of tenant → config |

## Tenant Config


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
