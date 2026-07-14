# 멀티 테넌트 아키텍처

Commander는 **모든 계층**에서 멀티 테넌트 격리를 지원합니다.

## 요청 흐름

```
Request → HttpServer
           │
           ├─ authenticate()           ← Bearer → 테넌트 매핑
           ├─ resolveTenantFromAuth()  ← API key → tenantId
           │
           └─ execute({ tenantId }) → AgentRuntime
                                        │
                                        ├─ TenantProvider.getTenantConfig(tenantId)
                                        │   → tokenBudget, maxConcurrency, maxRunsPerMinute
                                        │
                                        ├─ Rate limit check     → TENANT_RATE_LIMIT
                                        ├─ Concurrency check    → TENANT_CONCURRENCY_LIMIT
                                        │
                                        └─ 테넌트 스코프 인스턴스:
                                            ├─ SamplesStore(path/tenant_{id}/)
                                            ├─ TraceStore(path/tenant_{id}/)
                                            ├─ StateCheckpointer(path/tenant_{id}/)
                                            ├─ ThreeLayerMemory(per-instance)
                                            └─ ToolResultCache(key = SHA256(tenantId + tool + args))
```

## 격리 계층

| 계층 | 메커니즘 |
|------|----------|
| Rate limits | 테넌트별 분당 요청 |
| Concurrency | 테넌트별 최대 동시 런 |
| Storage | 테넌트별 디렉터리 |
| Memory | 인스턴스별 ThreeLayerMemory |
| Cache | 키에 tenantId 포함 (SHA-256) |
| Metrics | 모든 카운터/게이지/히스토그램에 `tenant` 라벨 |

## 프로바이더

| 프로바이더 | 동작 |
|------------|------|
| `NullTenantProvider` | 격리 없음, 단일 테넌트 호환 |
| `SimpleTenantProvider` | tenant → config 정적 맵 |

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

## 운영 팁

```bash
export COMMANDER_API_KEY="long-random-secret"
# 테넌트 매핑은 서버 설정 / TENANT_PROVIDER 에 따름
npx tsx packages/core/src/cliEntry.ts doctor
curl -s http://localhost:4000/health/detailed
```

로컬 CLI 단일 머신 개발은 보통 `NullTenantProvider`로 충분합니다. 프로덕션 SaaS·공유 클러스터에서는 Simple(또는 커스텀) 프로바이더와 쿼터를 켜세요.

## 관련

- [보안 게이트웨이](/ko/architecture/security-gateway)  
- [캐싱](/ko/architecture/caching)  
- [프로덕션 준비](/ko/architecture/production-readiness)  
- [보안 가이드](/ko/guide/security)  
