# ウォッチモード（SSE）

実行中の **全イベント** を Server-Sent Events でリアルタイム配信します。

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## イベント

| 種別 | 内容 |
|------|------|
| `task.start` | 開始 |
| `deliberation` | 複雑度分析 |
| `topology.select` | トポロジ |
| `agent.spawn` | エージェント生成 |
| `tool.call` / `tool.result` | ツール |
| `verification` | 品質ゲート |
| `checkpoint` | チェックポイント |
| `task.complete` / `task.error` | 終了 |

## 消費例

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

```typescript
const unsub = client.onEvent((e) => console.log(e.type, e.data));
await client.run('debug the failing test');
```

```bash
curl -N -H "Accept: text/event-stream" -H "Authorization: Bearer $TOKEN" \
  -d '{"task":"debug","stream":true}' http://localhost:4000/execute
```

用途: CI ダッシュボード、カスタム UI、デバッグ、監査ログ。

[SDK](/ja/guide/sdk) · [Runtime](/ja/architecture/agent-runtime)
