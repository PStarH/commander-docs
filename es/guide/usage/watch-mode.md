# Modo watch (streaming SSE)

Watch transmite en tiempo real **cada evento de ejecución** por Server-Sent Events. Ideal para tareas largas, depurar agentes o integrar UIs custom.

## Uso

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
# o: commander watch "..."
```

## Eventos emitidos

| Tipo | Descripción |
|------|-------------|
| `task.start` | Tarea iniciada |
| `deliberation` | Análisis de complejidad |
| `topology.select` | Topología elegida |
| `agent.spawn` | Agente creado |
| `tool.call` / `tool.result` | Inicio/fin de tool |
| `subtask.complete` | Subtarea terminada |
| `verification` | Puerta de calidad |
| `checkpoint` | Checkpoint guardado |
| `task.complete` / `task.error` | Fin o error |

## Formato de evento

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

## Consumir eventos

### CLI

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

### TypeScript

```typescript
const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
});
const result = await client.run('debug the failing test');
await client.disconnect();
```

### HTTP

```bash
curl -N \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: text/event-stream" \
  -d '{"task": "debug the failing test", "stream": true}' \
  http://localhost:4000/execute
```

## Casos de uso

- **CI/CD** — dashboards de build en vivo  
- **UIs custom** — monitorización de agentes  
- **Depuración** — cada paso de una ejecución multi-agente  
- **Auditoría** — trazas completas persistidas  

## Relacionado

- [Ejecutar tareas](/es/guide/usage/running-tasks)  
- [Agent SDK](/es/guide/sdk)  
- [Runtime](/es/architecture/agent-runtime)
