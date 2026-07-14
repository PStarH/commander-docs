# Resilience

**Resilience.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| State | Behavior |
|-------|----------|
| **CLOSED** | Normal operation. Requests pass through. |
| **OPEN** | After 5 consecutive failures. All requests are rejected immediately. Cooldown: 30 seconds. |
| **HALF-OPEN** | After cooldown. One test request is allowed. Success → CLOSED, failure → OPEN again. |


## 主な節

### Circuit Breaker

**Circuit Breaker** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Provider Fallback Chain

**Provider Fallback Chain** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Crash-Safe Checkpoints

**Crash-Safe Checkpoints** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Dead Letter Queue

**Dead Letter Queue** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Compensation Registry

**Compensation Registry** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Event Sourcing Recovery

**Event Sourcing Recovery** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Recovery Bootstrapper

**Recovery Bootstrapper** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### ATR System

**ATR System** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();    // Resets failure count
breaker.onFailure();    // Increments; opens circuit at threshold
breaker.isAvailable();  // false when OPEN
```
```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
// Tries OpenAI → Anthropic → DeepSeek → Groq
// Throws FallbackChainExhaustedError if all fail
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
