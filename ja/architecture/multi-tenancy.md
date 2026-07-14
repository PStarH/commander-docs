# Multi-Tenant Architecture

**Multi-Tenant Architecture.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Layer | Mechanism |
|-------|-----------|
| Rate limits | Per-tenant: requests/minute |
| Concurrency | Per-tenant: max concurrent runs |
| Storage | Per-tenant directory paths |
| Memory | Per-instance ThreeLayerMemory |
| Cache | SHA-256 key includes tenantId |
| Metrics | Every counter/gauge/histogram has `tenant` label |


## 主な節

### Request Flow

**Request Flow** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Isolation Layers

**Isolation Layers** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Providers

**Providers** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Tenant Config

**Tenant Config** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

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

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
