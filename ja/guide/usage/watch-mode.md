# Watch Mode (SSE Streaming)

**Watch Mode (SSE Streaming).** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Event Type | Description |
|------------|-------------|
| `task.start` | Task started |
| `deliberation` | Complexity analysis |
| `topology.select` | Topology selected |
| `agent.spawn` | Agent created |
| `tool.call` | Tool execution started |
| `tool.result` | Tool execution completed |
| `subtask.complete` | Subtask finished |
| `verification` | Quality gate check |
| `checkpoint` | State checkpoint saved |
| `task.complete` | Task finished |
| `task.error` | Error occurred |


## 主な節

### Usage

**Usage** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Streamed Events

**Streamed Events** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Event Format

**Event Format** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Consuming Events

**Consuming Events** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Use Cases

**Use Cases** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```bash
# From monorepo source (or: commander watch "...")
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```
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
