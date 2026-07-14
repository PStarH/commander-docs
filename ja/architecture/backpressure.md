# バックプレッシャー・コントローラ

バックプレッシャー・コントローラは Commander ランタイムの **統合入場制御（admission control）** です。需要が容量を超えたときの過負荷を防ぎ、**Token Bucket → Ring Buffer → Circuit Breaker** の 3 段パイプラインを使います。

## 構造

```
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
               rate-limit       absorb bursts     protect when overwhelmed
```

| 段                  | 役割                             | パターン        |
| ------------------- | -------------------------------- | --------------- |
| **Token Bucket**    | 秒あたりトークンで入場速度を制限 | Leaky bucket    |
| **Ring Buffer**     | バースト吸収（固定サイズ、O(1)） | LMAX Disruptor  |
| **Circuit Breaker** | 消費者過負荷時の保護             | Hystrix 3-state |

## 動作

1. **Token Bucket** — リクエストがトークンを消費。空なら ring buffer へ spill。
2. **Ring Buffer** — 固定サイズでバーストを吸収。満杯なら最古を破棄（spill 集計）。
3. **Circuit Breaker** — spill 率が閾値を超えると open、half-open まで drop。

## 設定

```typescript
import { BackpressureController } from "@commander/core";

const controller = new BackpressureController({
  tokenBucket: {
    maxTokens: 100,
    refillRatePerSecond: 50,
  },
  ringBuffer: {
    capacity: 200,
  },
  circuitBreaker: {
    failureThreshold: 0.5,
    recoveryTimeoutMs: 30000,
    halfOpenMaxRequests: 10,
  },
});
```

> パッケージは monorepo の `packages/core` から。npm 公開が主経路になるまでは workspace を使ってください。

## 使い方

```typescript
const admission = controller.tryAdmit();

if (admission.allowed) {
  const result = await processRequest(request);
  controller.recordSuccess();
} else {
  return { status: 429, reason: admission.reason };
}
```

## Lock-free

CAS ベースの原子カウンタで、同時読みが書きをブロックしません（NFR-PERF-05）。

## メトリクス

| メトリクス                             | 説明                            |
| -------------------------------------- | ------------------------------- |
| `backpressure_tokens_available`        | バケット残トークン              |
| `backpressure_ring_buffer_occupancy`   | リング占有率                    |
| `backpressure_circuit_breaker_state`   | `CLOSED` / `OPEN` / `HALF_OPEN` |
| `backpressure_requests_admitted_total` | 許可                            |
| `backpressure_requests_rejected_total` | 拒否                            |
| `backpressure_requests_spilled_total`  | spill                           |

## チューニング

| 症状           | 調整                                         |
| -------------- | -------------------------------------------- |
| 429 が多すぎる | `maxTokens` / `refillRatePerSecond` を上げる |
| メモリ圧       | ring `capacity` を下げる                     |
| 連鎖障害       | `failureThreshold` を下げ早期 open           |
| 回復が遅い     | `recoveryTimeoutMs` を延ばす                 |

## 関連

- [本番準備](/ja/architecture/production-readiness)
- [エージェントランタイム](/ja/architecture/agent-runtime)
- [トラブルシューティング](/ja/guide/troubleshooting)
