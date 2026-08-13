# Multi-Tenant Architecture

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/multi-tenancy)



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

## 프로바이더


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
