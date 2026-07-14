# スーパービジョン・ツリー

Commander は **Erlang/OTP 風スーパービジョン・ツリー** で障害を隔離します。すべてのエラーをエージェント内で捕まえるより、クラッシュさせてスーパーバイザが再起動する — “Let It Crash”。

## なぜか

- **障害隔離** — 1 エージェントのクラッシュが全体を殺さない  
- **自動復旧** — 人手なし再起動  
- **エスカレーション** — 子が繰り返し落ちる場合は親へ  
- **優雅な停止** — 開始の逆順で子を止める  

## 構造

```
Root Supervisor (one_for_one)
   ├── Agent 1
   ├── Agent 2
   └── Agent N
```

## 再起動戦略

| 戦略 | 動作 | いつ |
|------|------|------|
| `one_for_one` | 落ちた子だけ | 独立 |
| `one_for_all` | 全子を再起動 | 相互依存 |
| `rest_for_one` | 落ちた子 + その後に起動した子 | 起動順依存 |

## 設定

```typescript
import { Supervisor } from '@commander/core';

const supervisor = new Supervisor({
  id: 'agent-pool',
  strategy: 'one_for_one',
  maxRestarts: 10,
  maxRestartIntervalMs: 60000,
  defaultShutdownMs: 5000,
  publishEvents: true,
});
```

## 子の追加

```typescript
const handle = await supervisor.startChild({
  id: 'agent-1',
  start: async () => {
    const runtime = await createAgentRuntime({ /* config */ });
    return runtime;
  },
});
```

再起動上限超過で親へエスカレーションまたはプール停止。MessageBus へイベント発行可。

## 関連

- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [Resilience](/ja/architecture/resilience)  
- [マルチエージェント](/ja/architecture/multi-agent)  
