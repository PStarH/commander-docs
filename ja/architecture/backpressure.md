# Backpressure Controller

The backpressure controller implements **unified admission control** for the Commander runtime, preventing overload when demand exceeds capacity. It uses a three-stage pipeline: Token Bucket → Ring Buffer → Circuit Breaker. 1. **Token Bucket** — Requests consume a token. When the bucket is empty, requests spill to the ring buffer.

本ページは Commander における **Backpressure Controller** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
              rate-limit       absorb bursts     protect when overwhelmed
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
