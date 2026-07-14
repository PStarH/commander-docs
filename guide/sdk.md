# Agent SDK (TypeScript)

Embed Commander in your own applications with `@commander/sdk`.

> **Status:** Packages live under `packages/sdk` in the monorepo. **npm publication is not the primary install path yet** — clone the monorepo and build the workspace package.

## Installation

### From the monorepo (recommended today)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

Then depend on the workspace package from your app (`"@commander/sdk": "workspace:*"`), or import from `packages/sdk` during development.

### When published to npm (upcoming)

```bash
# Not the quick-start path yet — only after public publish:
pnpm add @commander/sdk
# peer: @commander/core
```

## Quick Start

```typescript
import { CommanderClient } from "@commander/sdk";

const client = new CommanderClient({ provider: "openai" });
await client.connect();

const result = await client.run("analyze this repository structure");
console.log(result.status, result.summary);

await client.disconnect();
```

Zero-config (auto-detect provider from environment):

```typescript
import { createClient } from "@commander/sdk";

const client = await createClient(); // connects for you
const result = await client.run("audit this repo for security vulnerabilities");
await client.disconnect();
```

## Plan without executing

```typescript
const plan = await client.plan("refactor the auth module");
// Deliberation only — topology, agents, budget (no full execution)
console.log(plan);
```

## Real-time events

```typescript
const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
});

await client.run("debug the failing test");
unsub();
```

## Configuration

```typescript
const client = new CommanderClient({
  provider: "anthropic", // optional — auto-detect from env if omitted
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: "claude-sonnet-4-20250514",
  tokenBudget: 64_000,
  defaultTopology: "SINGLE",
  persistSessions: true,
});
```

| Option            | Default          | Description                                      |
| ----------------- | ---------------- | ------------------------------------------------ |
| `provider`        | auto             | Provider id (`openai`, `anthropic`, `ollama`, …) |
| `apiKey`          | env              | Explicit API key                                 |
| `model`           | provider default | Model override                                   |
| `baseUrl`         | provider default | Custom OpenAI-compatible base URL                |
| `tokenBudget`     | `64000`          | Soft token budget                                |
| `defaultTopology` | `SINGLE`         | Fallback topology                                |
| `persistSessions` | `true`           | Keep recent session summaries in memory          |

## Core methods

| Method                        | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `connect()` / `disconnect()`  | Lifecycle — wires core runtime + event bus     |
| `run(task)`                   | Full multi-agent execution → `ExecutionResult` |
| `plan(task)`                  | Deliberation only                              |
| `onEvent(handler)`            | Subscribe to agent/tool lifecycle events       |
| `createAgent(config)`         | Register a named agent profile                 |
| `writeMemory` / `queryMemory` | Three-layer memory helpers                     |

## HTTP API (server mode)

When you run the API server (`docker compose` or `pnpm gui`), Commander also exposes REST + SSE:

```bash
# Health
curl http://localhost:4000/health

# Execute (Bearer auth when COMMANDER_API_KEY is set)
curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

See [Deployment](/deployment) for server configuration and [Python SDK](/guide/sdk-python) for the HTTP client.

## Next

- [Python SDK](/guide/sdk-python) — thin httpx client against the API server
- [Commands](/guide/commands) — CLI equivalents of SDK calls
- [Architecture](/architecture/overview) — what runs under `client.run()`
