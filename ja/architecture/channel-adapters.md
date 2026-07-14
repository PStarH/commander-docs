# チャネル・アダプタ

Commander はアダプタ経由で複数の通信チャネルをサポートします。エージェントが Telegram など各プラットフォームでユーザーと対話できます。

## インターフェース

```typescript
interface ChannelAdapter {
  readonly name: string;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: InboundMessage) => void): void;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}
```

## Telegram アダプタ

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

## カスタム・アダプタ

`ChannelAdapter` を実装して Discord 等を追加できます。`connect` / `send` / `onMessage` / `disconnect` を満たせばランタイムに載せられます。

## 運用

- 公開ボットは `allowedChatIds` でホワイトリスト  
- トークンは env のみ  
- 本番はゲートウェイ認証と揃える  

monorepo `packages/core`。CLI: `npx tsx packages/core/src/cliEntry.ts`。

## 関連

- [Web コンソール](/ja/guide/web-console)  
- [セキュリティ](/ja/guide/security)  
- [MCP](/ja/architecture/mcp)  
