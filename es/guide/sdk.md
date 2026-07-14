# Agent SDK (TypeScript)

Integra Commander con `@commander/sdk`.

> **Estado:** monorepo-first; npm en curso.

## Instalación

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

## Inicio rápido

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('analyze this repository structure');
console.log(result.status, result.summary);
await client.disconnect();

const c = await createClient();
await c.run('audit this repo');
await c.disconnect();
```

## Plan y eventos

```typescript
const plan = await client.plan('refactor the auth module');
const unsub = client.onEvent((e) => console.log(e.type, e.data));
await client.run('debug the failing test');
unsub();
```

## Métodos

| Método | Rol |
|--------|-----|
| `connect` / `disconnect` | Ciclo de vida |
| `run` | Ejecución |
| `plan` | Solo deliberación |
| `onEvent` | Stream |
| memoria / `createAgent` | Avanzado |

## HTTP

```bash
curl http://localhost:4000/health
curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

[Despliegue](/es/deployment) · [Python SDK](/es/guide/sdk-python).
