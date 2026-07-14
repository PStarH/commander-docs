# 本番準備

Commander is designed for production from day one. Every component includes observability, safety, and reliability features. After 5 consecutive failures, the circuit opens for 30 seconds, then transitions to half-open for recovery. The `CircuitBreakerRegistry` manages breakers for all active providers.

本ページは Commander における **本番準備** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
getMetricsCollector().exportOpenMetrics()
// Exports: counters, gauges, histograms with tenant labels
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
