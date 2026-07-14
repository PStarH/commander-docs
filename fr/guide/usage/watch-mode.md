# Mode watch (streaming SSE)

Chaque événement d’exécution en temps réel via Server-Sent Events.

## Usage

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## Événements

| Type | Description |
|------|-------------|
| `task.start` | Début |
| `deliberation` | Analyse de complexité |
| `topology.select` | Topologie choisie |
| `agent.spawn` | Agent créé |
| `tool.call` / `tool.result` | Tool |
| `verification` | Porte de qualité |
| `checkpoint` | Checkpoint |
| `task.complete` / `task.error` | Fin |

## Consommer

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

```typescript
const unsub = client.onEvent((e) => console.log(e.type, e.data));
await client.run('debug the failing test');
```

```bash
curl -N -H "Accept: text/event-stream" -H "Authorization: Bearer $TOKEN" \
  -d '{"task":"debug","stream":true}' http://localhost:4000/execute
```

Cas d’usage : dashboards CI, UIs custom, debug multi-agents, audit.

## Lié

- [SDK](/fr/guide/sdk) · [Runtime](/fr/architecture/agent-runtime)
