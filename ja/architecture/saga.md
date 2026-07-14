# Saga トランザクション

Commander は多段操作の一貫性のため **サガ・パターン**（ステップごとの補償ロールバック）を実装します。

## 構造

```
SagaBuilder.define()
  │
  ├─ Step 1 → Compensation 1
  ├─ Step 2 → Compensation 2
  └─ Coordinator.execute
       ├─ 成功: 順次
       └─ 失敗: 逆順で補償
```

## SagaBuilder

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
  .build();
```

## Coordinator

順序実行 · 失敗時は逆順補償 · 状態 PENDING/COMPLETED/COMPENSATING/FAILED · 回復不能時は DLQ。

## WorkerPool

独立ステップは並列化可能:

```typescript
const pool = new WorkerPool({ maxConcurrency: 5 });
pool.execute(steps);
```

## ツール連携

mutation ツールは Compensation Registry に登録。CLI: `saga` / `compensation` / `undo`。

```bash
npx tsx packages/core/src/cliEntry.ts doctor
```

## 関連

- [本番準備](/ja/architecture/production-readiness)  
- [Resilience](/ja/architecture/resilience)  
- [ツール](/ja/architecture/tools)  
