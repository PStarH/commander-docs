# Channel Adapters

**Channel Adapters.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Adapter | Status | Features |
|---------|--------|----------|
| Terminal | ✅ Built-in | Full interaction, streaming, plan mode |
| HTTP (REST) | ✅ Built-in | Execute, plan, watch endpoints |
| SSE | ✅ Built-in | Real-time event streaming |
| Telegram | ✅ Built-in | Async agent interaction via chat |
| Discord | 🔲 Planned | Server/channel-based interaction |
| Slack | 🔲 Planned | Workspace integration |
| WebSocket | 🔲 Planned | Bidirectional real-time communication |


## 主な節

### Architecture

**Architecture** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Telegram Adapter

**Telegram Adapter** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Creating Custom Adapters

**Creating Custom Adapters** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Built-in Adapters

**Built-in Adapters** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```typescript
interface ChannelAdapter {
  readonly name: string;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: InboundMessage) => void): void;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}
```
```typescript
import { TelegramAdapter } from '@commander/core';

const adapter = new TelegramAdapter({
  botToken: process.env.TELEGRAM_BOT_TOKEN,
  allowedChatIds: ['chat-1', 'chat-2'],
});

adapter.onMessage(async (msg) => {
  const result = await runtime.execute(msg.text);
  await adapter.send({
    chatId: msg.chatId,
    text: result.summary,
  });
});

await adapter.connect();
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
