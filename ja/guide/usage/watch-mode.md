# Watch モード (SSE ストリーム)

Watch モードは Server-Sent Events (SSE) で実行イベントをリアルタイム配信します。長時間タスクの監視、エージェント挙動のデバッグ、カスタム UI 連携に向きます。

## 使い方

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
# または run --stream
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## ストリームされるイベント

| 型 | 説明 |
|----|------|
| `task.start` | 開始 |
| `deliberation` | 複雑度分析 |
| `topology.select` | トポロジ選択 |
| `agent.spawn` | エージェント生成 |
| `tool.call` / `tool.result` | ツール実行 |
| `subtask.complete` | サブタスク完了 |
| `verification` | 品質ゲート |
| `checkpoint` | チェックポイント |
| `task.complete` / `task.error` | 完了 / エラー |

## イベント形式

```json
{
  "type": "tool.call",
  "data": {
    "tool": "grep",
    "args": { "pattern": "deprecated", "path": "./src" },
    "agentId": "agent-3",
    "timestamp": "2026-05-23T10:30:00Z"
  }
}
```

## 消費

CLI の `watch` / `run --stream`、Web Console、SDK の `onEvent`、HTTP SSE で同じイベント流を受け取れます。

## 関連

- [Plan モード](/ja/guide/usage/plan-mode)  
- [Web コンソール](/ja/guide/web-console)  
- [Agent SDK](/ja/guide/sdk)  
