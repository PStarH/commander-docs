# Extension Points

**Extension Points.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentComplete` | Agent run finished |
| `onError` | Run failed |


## 主な内容

### Plugin System (19 Hook Points)

運用では **Plugin System (19 Hook Points)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/extension-points)を参照してください。

### Extension Interfaces

運用では **Extension Interfaces** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/extension-points)を参照してください。

### Meta-Learner

運用では **Meta-Learner** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/extension-points)を参照してください。

## 例（コードは英語のまま）

```typescript
class MyProvider implements LLMProvider {
  async call(messages: Message[], options: CallOptions): Promise<LLMResponse> {
    // Your implementation
  }
}
runtime.registerProvider('my-provider', new MyProvider());
```

```typescript
class MyTool implements Tool {
  name = 'my-tool';
  async execute(ctx: ToolContext, args: any): Promise<ToolResult> {
    // Your implementation
  }
}
runtime.registerTool('my-tool', new MyTool());
```

```typescript
class TelegramAdapter implements ChannelAdapter {
  // Telegram integration
}
```

## 運用

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
