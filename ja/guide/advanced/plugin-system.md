# Plugin System

**Plugin System.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentStart` | Agent begins work |
| `onAgentComplete` | Agent finishes work |
| `onSubtaskCreate` | New subtask created |
| `onSubtaskComplete` | Subtask finished |
| `onCheckpoint` | State checkpoint saved |
| `onError` | Error occurred (non-fatal) |
| `onRetry` | Retry attempt starting |
| `beforeVerification` | Before quality gate check |
| `afterVerification` | After quality gate check |
| `onTokenUsage` | Token budget updated |
| `onMetricsEmit` | Metrics collected |
| `beforeRun` | Execution run starts |
| `afterRun` | Execution run completes |
| `onHandoff` | Agent-to-agent handoff |
| `onStreamEvent` | SSE event emitted |


## 主な節

### Hook Points

**Hook Points** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Creating a Plugin

**Creating a Plugin** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Registering a Plugin

**Registering a Plugin** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Plugin Security

**Plugin Security** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Use Cases

**Use Cases** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```typescript
import { CommanderPlugin } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';

  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] Calling ${params.provider} with ${params.messages.length} messages`);
      return params; // Return modified params, or throw to block
    },

    afterToolCall: async (result) => {
      console.log(`[Tool] ${result.tool} completed in ${result.durationMs}ms`);
      return result; // Return modified result, or throw to block
    },

    onError: async (error) => {
      console.error(`[Error] ${error.message}`);
      // Don't return — errors are fire-and-forget
    },

    onMetricsEmit: async (metrics) => {
      // Forward metrics to external monitoring
      await fetch('https://monitor.example.com/metrics', {
        method: 'POST',
        body: JSON.stringify(metrics),
      });
    },
  };
}
```
```typescript
import { getHookManager } from '@commander/core';

const hookManager = getHookManager();
hookManager.register(new LoggingPlugin());
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
