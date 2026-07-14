# レジリエンス

Commander includes a multi-layer resilience infrastructure that ensures availability, data safety, and recoverability in production. Each LLM provider has its own circuit breaker with three states:

本ページは Commander における **レジリエンス** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();    // Resets failure count
breaker.onFailure();    // Increments; opens circuit at threshold
breaker.isAvailable();  // false when OPEN
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
