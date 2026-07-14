# 채널 어댑터

Commander는 어댑터 시스템으로 여러 커뮤니케이션 채널을 지원합니다. 에이전트가 Telegram 등 다양한 플랫폼에서 사용자와 대화할 수 있습니다.

## 인터페이스

```typescript
interface ChannelAdapter {
  readonly name: string;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: InboundMessage) => void): void;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}
```

## Telegram 어댑터

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

## 커스텀 어댑터

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
    // Wire inbound events
  }

  async disconnect(): Promise<void> {
    // Cleanup
  }
}
```

## 운영 메모

- 공개 봇은 `allowedChatIds` 로 화이트리스트  
- 시크릿 토큰은 env에만 두고 git에 넣지 않기  
- 프로덕션에서는 `COMMANDER_API_KEY` 와 동일하게 게이트웨이 인증을 맞출 것  

패키지는 monorepo `packages/core`. CLI: `npx tsx packages/core/src/cliEntry.ts`.

## 관련

- [웹 콘솔](/ko/guide/web-console)  
- [보안](/ko/guide/security)  
- [MCP](/ko/architecture/mcp)  
