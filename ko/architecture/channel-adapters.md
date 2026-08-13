# 채널 어댑터

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/channel-adapters)



Commander supports multiple communication channels through its adapter system, allowing agents to interact with users across different platforms.

## Architecture


Channel adapters implement the `ChannelAdapter` interface:

```typescript
interface ChannelAdapter {
  readonly name: string;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: InboundMessage) => void): void;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}
```

## Telegram Adapter


Built-in Telegram support for interacting with Commander agents via chat:

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

## Creating Custom Adapters


```typescript
import { ChannelAdapter, InboundMessage, OutboundMessage } from '@commander/core';

class DiscordAdapter implements ChannelAdapter {
  readonly name = 'discord';

  async connect(): Promise<void> {
    // Initialize Discord client
  }

  async send(message: OutboundMessage): Promise<void> {
    // Send message to Discord channel
  }

  onMessage(handler: (msg: InboundMessage) => void): void {
    // Register Discord message handler
  }

  async disconnect(): Promise<void> {
    // Cleanup
  }
}

runtime.registerChannelAdapter('discord', new DiscordAdapter());
```

## Built-in Adapters


| Adapter | Status | Features |
|---------|--------|----------|
| Terminal | ✅ Built-in | Full interaction, streaming, plan mode |
| HTTP (REST) | ✅ Built-in | Execute, plan, watch endpoints |
| SSE | ✅ Built-in | Real-time event streaming |
| Telegram | ✅ Built-in | Async agent interaction via chat |
| Discord | 🔲 Planned | Server/channel-based interaction |
| Slack | 🔲 Planned | Workspace integration |
| WebSocket | 🔲 Planned | Bidirectional real-time communication |
