# Saga Transactions

**Saga Transactions.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Policy | Behavior |
|--------|----------|
| No retry | Fail immediately, begin compensation |
| Fixed retries | Retry N times with fixed delay |
| Exponential backoff | Retry with doubling delay, up to max |
| Circuit breaker | Use shared circuit breaker state |


## 主な節

### Architecture

**Architecture** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### SagaBuilder

**SagaBuilder** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Coordinator

**Coordinator** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### WorkerPool

**WorkerPool** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Checkpointer

**Checkpointer** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### ApprovalManager

**ApprovalManager** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### RetryController

**RetryController** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Stores

**Stores** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```
SagaBuilder.define()
  │
  ├─ Step 1: Create resource   → Compensation: Delete resource
  ├─ Step 2: Update resource   → Compensation: Revert update
  ├─ Step 3: Send notification → Compensation: Void notification
  │
  └─ Coordinator.execute(saga)
       │
       ├─ Step 1 → success
       ├─ Step 2 → success
       ├─ Step 3 → FAILURE
       │
       └─ Compensate
            ├─ Undo Step 2 (revert update)
            └─ Undo Step 1 (delete resource)
```
```typescript
const saga = new SagaBuilder('deploy-service')
  .step('create-dir', async (ctx) => {
    await fs.mkdir(ctx.path);
  }, {
    compensate: async (ctx) => {
      await fs.rmdir(ctx.path);
    },
  })
  .step('write-config', async (ctx) => {
    await fs.writeFile(ctx.path, ctx.config);
  }, {
    compensate: async (ctx) => {
      await fs.unlink(ctx.path);
    },
  })
  .step('restart-service', async (ctx) => {
    await service.restart();
  }, {
    compensate: async (ctx) => {
      await service.restore(ctx.prevVersion);
    },
  })
  .build();
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
