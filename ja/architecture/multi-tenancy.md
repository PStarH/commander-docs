# マルチテナント・アーキテクチャ

Commander は **すべての層** でマルチテナント隔離をサポートします。

## リクエストフロー

```
Request → HttpServer
           │
           ├─ authenticate()           ← Bearer → テナント対応
           ├─ resolveTenantFromAuth()  ← API key → tenantId
           │
           └─ execute({ tenantId }) → AgentRuntime
                                        │
                                        ├─ TenantProvider.getTenantConfig(tenantId)
                                        │   → tokenBudget, maxConcurrency, maxRunsPerMinute
                                        │
                                        ├─ Rate limit / Concurrency チェック
                                        │
                                        └─ テナントスコープ:
                                            SamplesStore / TraceStore / StateCheckpointer
                                            ThreeLayerMemory / ToolResultCache(tenantId 込み)
```

## 隔離レイヤ

| 層 | 仕組み |
|----|--------|
| Rate limits | テナントごとの分あたりリクエスト |
| Concurrency | テナントごとの最大同時 run |
| Storage | テナント別ディレクトリ |
| Memory | インスタンス別 ThreeLayerMemory |
| Cache | キーに tenantId（SHA-256） |
| Metrics | すべてに `tenant` ラベル |

## プロバイダー

| プロバイダー | 動作 |
|--------------|------|
| `NullTenantProvider` | 隔離なし（単一テナント互換） |
| `SimpleTenantProvider` | tenant → config の静的マップ |

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

## 運用

```bash
export COMMANDER_API_KEY="long-random-secret"
npx tsx packages/core/src/cliEntry.ts doctor
curl -s http://localhost:4000/health/detailed
```

ローカル単機 CLI は多くの場合 `NullTenantProvider` で十分。本番の共有クラスタでは Simple（またはカスタム）とクォータを有効にしてください。

## 関連

- [セキュリティゲートウェイ](/ja/architecture/security-gateway)  
- [キャッシュ](/ja/architecture/caching)  
- [本番準備](/ja/architecture/production-readiness)  
- [セキュリティ](/ja/guide/security)  
