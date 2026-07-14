# 本番準備

Commander は初日から本番を想定しています。観測・安全・信頼性の機能が各コンポーネントに組み込まれています。

## 機能マトリクス

| 能力                         | Commander の状態                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------- |
| **型安全**                   | TypeScript strict、**`as any` / `@ts-ignore` ゼロ**（ESLint error）              |
| **エラー処理**               | 100+ モジュールで **空 catch ゼロ**                                              |
| **メトリクス**               | Prometheus/OpenMetrics の counter・gauge・histogram + テナントラベル             |
| **トレーシング**             | 永続 TraceStore、OpenTelemetry export                                            |
| **クラッシュ安全**           | 各ステップの atomic SQLite WAL チェックポイント + イベントソーシングハッシュ鎖   |
| **サーキットブレーカー**     | 5 失敗 → 30s open → half-open、プロバイダー別レジストリ                          |
| **DLQ**                      | 7 カテゴリ、15 失敗モード、永続 + 再実行                                         |
| **マルチテナント**           | テナント別 rate limit、同時実行クォータ、ストレージ/キャッシュ隔離               |
| **セキュリティ**             | 7 層 EnterpriseSecurityGateway、DLP、capability tokens、Bearer、CORS、rate limit |
| **観測**                     | health、readiness、OpenAPI、SSE、Grafana                                         |
| **イベントソーシング**       | SHA-256 ハッシュ鎖 WAL、スナップショット復旧、決定的再生                         |
| **プラグインサンドボックス** | サードパーティのロード文脈を制限；権限はメインを超えない                         |

## 安全機構

### Circuit Breaker

連続 5 失敗で 30 秒 open、その後 half-open。`CircuitBreakerRegistry` がアクティブプロバイダーを管理。

### Dead Letter Queue

復旧不能エラーを 7 カテゴリ（llm, tool, execution, verification, circuit_breaker, compensation, semantic_drift）と 15 標準失敗モードで永続化。原因修正後の replay をサポート。

### Compensation Registry

失敗した mutation ツールは登録済み補償でロールバック。Saga コーディネータと連携。

### State Checkpointer

毎ステップ SQLite WAL（synchronous=NORMAL, busy_timeout=5000）で atomic チェックポイント。

### Event Sourcing Engine

SHA-256 ハッシュ鎖 WAL による改ざん耐性ログ。タイムスタンプ・乱数・LLM 応答・ツール結果など非決定入力を記録し決定的再生。

### Recovery Bootstrapper

起動時に zombie run（EXECUTING/VERIFYING/PAUSED）を走査、fencing lease を取り、チェックポイント再開または補償付き abort。

## 観測

### メトリクス

```typescript
getMetricsCollector().exportOpenMetrics();
```

### Tracing

`TraceStore` 永続の span トレース。OpenTelemetry 時に PII を自動マスク。

### Health

- `/health` · `/ready` · `/metrics` · `/health/detailed`

### Grafana

開発者ビュー（成功率、P95、トークン、アクティブ run）とメカニズムビュー（WAL、DLQ、ブレーカー、ロック競合など）。

## テスト

**失敗ゼロ志向:** 6700+ テスト、カオス注入、マルチテナント隔離、プラグイン権限、ストレステスト。

```
npx tsx --test tests/*.test.ts
npx tsc --noEmit
```

## 関連

- [エージェントランタイム](/ja/architecture/agent-runtime)
- [検証パイプライン](/ja/architecture/verification)
- [デプロイ](/ja/deployment)
