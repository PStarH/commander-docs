# Agent SDK

Embed Commander in your own applications using the `@commander/sdk` package.

## Installation

```bash
pnpm add @commander/sdk
```

## Quick Start

```typescript
import { CommanderClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();

const result = await client.run('analyze this repository structure');
console.log(result.summary, result.status);

await client.disconnect();
```

## Real-Time Events

Subscribe to execution events with the SSE-compatible event system:

```typescript
const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
});

// Later: unsubscribe
unsub();
```

## HTTP API

Commander also exposes a REST API:

```
POST /execute
Authorization: Bearer <token>
Content-Type: application/json

{
  "task": "analyze this repository",
  "mode": "plan"
}
```

See the [deployment guide](/deployment) for server configuration.
