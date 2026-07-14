# Agent Transaction Runtime (ATR)

ATR はエージェント決定ループと **すべての外部システム呼び出しの間** にある決済（settlement）層です。アクションを冪等・回復可能・リース付き・フェンシング保護にします。

## なぜ ATR か

ATR なしでは fire-and-forget です。ツールは成功したが結果記録前にクラッシュすると失われ、再試行で二重実行になります。ATR はトランザクション保証でこれを防ぎます。

```
Agent Decision → ATR Settlement → External System
                     ├── Idempotency
                     ├── Recovery
                     ├── Leasing
                     └── Fencing
```

## ラン・ライフサイクル

```
PENDING → EXECUTING → VERIFYING → COMMITTED
               │            │
               └────────────┴──→ ABORTED → COMPENSATED
```

PAUSED は HITL/予算停止（再開可）。

## 冪等性

```typescript
import { IdempotencyStore } from '@commander/core';

const store = new IdempotencyStore({ ttlSeconds: 3600 });
const result = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});
```

## リース & フェンシング

単一オーナーが run を所有。期限切れ lease と fencing でゾンビ実行を遮断。[イベントソーシング](/ja/architecture/event-sourcing) の RecoveryBootstrapper と連携。

## 関連

- [イベントソーシング](/ja/architecture/event-sourcing)  
- [Saga](/ja/architecture/saga)  
- [Resilience](/ja/architecture/resilience)  
- [V2 移行](/ja/guide/migration-v2)  
