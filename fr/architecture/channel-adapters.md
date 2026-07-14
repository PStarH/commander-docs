# Channel Adapters

**Channel Adapters.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Adapter | Status | Features |
|---------|--------|----------|
| Terminal | ✅ Built-in | Full interaction, streaming, plan mode |
| HTTP (REST) | ✅ Built-in | Execute, plan, watch endpoints |
| SSE | ✅ Built-in | Real-time event streaming |
| Telegram | ✅ Built-in | Async agent interaction via chat |
| Discord | 🔲 Planned | Server/channel-based interaction |
| Slack | 🔲 Planned | Workspace integration |
| WebSocket | 🔲 Planned | Bidirectional real-time communication |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/channel-adapters) pour le détail exhaustif.

### Telegram Adapter

En pratique, **Telegram Adapter** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/channel-adapters) pour le détail exhaustif.

### Creating Custom Adapters

En pratique, **Creating Custom Adapters** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/channel-adapters) pour le détail exhaustif.

### Built-in Adapters

En pratique, **Built-in Adapters** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/channel-adapters) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
