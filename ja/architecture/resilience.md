# レジリエンス (Resilience)

Commander は可用性・データ安全・復旧性のための **多層レジリエンス** を持ちます。

## Circuit Breaker

プロバイダーごとに 3 状態:

| 状態 | 動作 |
|------|------|
| **CLOSED** | 通常通過 |
| **OPEN** | 連続 5 失敗後。即拒否。クールダウン 30s |
| **HALF-OPEN** | 試験 1 回。成功→CLOSED、失敗→OPEN |

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();
breaker.onFailure();
breaker.isAvailable();
```

`CircuitBreakerRegistry` が全プロバイダーを管理。

## Provider Fallback Chain

```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
```

`llmRetry.ts` が再試行可能 / 永続エラーを分類。

## Crash-safe Checkpoints

`StateCheckpointer` が各ステップを SQLite WAL で保存。テナント別ディレクトリ。

```typescript
const checkpointer = new StateCheckpointer({ basePath: '/data/checkpoints' });
await checkpointer.checkpoint({ runId, phase, stepNumber, messages, tokenUsage });
```

## Dead Letter Queue

**7 カテゴリ · 15 失敗モード**: `llm` · `tool` · `execution` · `verification` · `circuit_breaker` · `compensation` · `semantic_drift`。

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## 関連

- [イベントソーシング](/ja/architecture/event-sourcing)  
- [本番準備](/ja/architecture/production-readiness)  
- [Saga](/ja/architecture/saga)  
