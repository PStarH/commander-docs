# Watch Mode (SSE Streaming)

Watch mode provides real-time streaming of every execution event via Server-Sent Events (SSE). This is ideal for monitoring long-running tasks, debugging agent behavior, or integrating with custom UIs.

## Usage

```bash
# From monorepo source (or: commander watch "...")
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## Streamed Events

Every event in the execution pipeline is streamed:

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

## Event Format

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

## Consuming Events

### CLI
```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

### JavaScript/TypeScript
```typescript
const client = new CommanderClient({ provider: 'openai' });
await client.connect();

const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
  if (event.type === 'task.complete') {
    console.log('Result:', event.data.summary);
  }
});

const result = await client.run('debug the failing test');
await client.disconnect();
```

### HTTP (curl)
```bash
curl -N \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: text/event-stream" \
  -d '{"task": "debug the failing test", "stream": true}' \
  http://localhost:4000/execute
```

## Use Cases

- **CI/CD pipelines** — Stream events to build dashboards
- **Custom UIs** — Build real-time agent monitoring interfaces
- **Debugging** — Inspect every step of a complex multi-agent execution
- **Logging** — Persist full execution traces for audit
