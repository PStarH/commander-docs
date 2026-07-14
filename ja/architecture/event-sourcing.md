# イベントソーシング & リカバリ

Commander のイベントソーシングは **クラッシュ安全な実行**、改ざん耐性の監査証跡、決定的リプレイ、ゾンビ run の自動復旧を提供します。

## EventSourcingEngine

`EventSourcingEngine` は WAL（Write-Ahead Log）と SHA-256 ハッシュ鎖で IEventSourcingEngine（Pillar I）を実装します。

### Write-Ahead Log

イベントは `.commander_state/event-sourcing.wal` に原子的に追記されます（`COMMANDER_EVENT_SOURCING_WAL` で変更可）。

```
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

書き込みロックが append を直列化し、ハッシュ鎖の破損を防ぎます。

### ハッシュ鎖の完全性

各イベントは前のハッシュを取り込みます。`verifyIntegrity()` が全再計算で改ざんを検出します。

### 非決定入力の記録

リプレイ時は再計算せずログを使います。

- タイムスタンプ · 乱数 · LLM 応答 · ツール結果  

制約 IF-05: ログ再生で同一の状態遷移。

### スナップショット & 圧縮

- `snapshot()` — フル再生なしの高速復旧  
- `compact()` — スナップショット以前を削除し WAL を書き換え  
- `readFrom(snapshotId)` — 以降のイベントストリーム  

### ヘルス

| メトリクス | Degraded | Unhealthy |
|------------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | 断絶があれば |

`/health/detailed` で公開。

### EventSourcingSubscriber

MessageBus 購読でメインループを侵さず非同期 WAL 書き込み。WAL 不可時は graceful degrade。

## RecoveryBootstrapper

起動時にゾンビ run を走査します。

1. **RunLedger** — EXECUTING / VERIFYING / PAUSED  
2. **Lease** — 期限切れ  
3. **Fencing lease** — `recovery-{pid}`, TTL 30s  
4. **判定**  
   - PAUSED + 回復可能チェックポイント → resume  
   - EXECUTING/VERIFYING → abort + compensate  
   - 処理済み → skip  
5. **DLQ** · MessageBus へイベント  

### 冪等性

同時起動の 2 プロセス目は lease を見て skip。CI では `forceAbort` 可。

```typescript
interface RecoveryResult {
  scanned: number;
  recovered: number;
  aborted: number;
  skipped: number;
  details: RecoveryDetail[];
}
```

## 復旧優先度

1. **イベントリプレイ**（最正確）  
2. **チェックポイント**（速いが直近欠落の可能性）  
3. **Abort + compensate**（安全フォールバック）  

## 連携

| コンポーネント | 役割 |
|----------------|------|
| `RunLedger` | run 状態の真実源 |
| `LeaseManager` | 排他所有の fencing |
| `CheckpointStore` | SQLite チェックポイント |
| `DeadLetterQueue` | 復旧/中断の記録 |
| `MessageBus` | 復旧イベント |
| `CompensationBridge` | 中断時ロールバック |

## 関連

- [本番準備](/ja/architecture/production-readiness)  
- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [V2 移行](/ja/guide/migration-v2)  
