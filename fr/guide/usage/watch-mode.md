# Mode watch (streaming SSE)

Chaque événement d’exécution en temps réel via Server-Sent Events.

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## Événements

`task.start` · `deliberation` · `topology.select` · `agent.spawn` · `tool.call` · `tool.result` · `verification` · `checkpoint` · `task.complete` · `task.error`

## Consommer

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

```typescript
const unsub = client.onEvent((event) => console.log(event.type, event.data));
await client.run('debug the failing test');
```

```bash
curl -N -H "Accept: text/event-stream" -H "Authorization: Bearer $TOKEN" \
  -d '{"task":"debug","stream":true}' http://localhost:4000/execute
```

Cas d’usage : CI dashboards, UIs custom, debug multi-agents, audit.

[SDK](/fr/guide/sdk) · [Runtime](/fr/architecture/agent-runtime)
