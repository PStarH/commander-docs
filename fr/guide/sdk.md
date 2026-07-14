# Agent SDK (TypeScript)

Intégrez Commander avec `@commander/sdk`.

> **Statut :** packages sous `packages/sdk` dans le monorepo. **npm n’est pas encore le chemin principal** — clonez et buildez le workspace.

## Installation

### Monorepo (recommandé aujourd’hui)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

`"@commander/sdk": "workspace:*"` ou import depuis `packages/sdk` en dev.

### Quand publié sur npm (à venir)

```bash
# Après publish public seulement
pnpm add @commander/sdk
```

## Démarrage rapide

```typescript
import { CommanderClient } from "@commander/sdk";

const client = new CommanderClient({ provider: "openai" });
await client.connect();

const result = await client.run("analyze this repository structure");
console.log(result.status, result.summary);

await client.disconnect();
```

Zéro config :

```typescript
import { createClient } from "@commander/sdk";

const client = await createClient();
const result = await client.run("audit this repo for security vulnerabilities");
await client.disconnect();
```

## Plan sans exécuter

```typescript
const plan = await client.plan("refactor the auth module");
console.log(plan);
```

## Événements temps réel

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
  provider: "anthropic",
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: "claude-sonnet-4-20250514",
  tokenBudget: 64_000,
  defaultTopology: "SINGLE",
  persistSessions: true,
});
```

| Option | Défaut | Description |
|--------|--------|-------------|
| `provider` | auto | `openai`, `anthropic`, `ollama`, … |
| `apiKey` | env | Clé explicite |
| `model` | défaut provider | Override modèle |
| `baseUrl` | défaut provider | Base URL compatible OpenAI |
| `tokenBudget` | `64000` | Budget soft |
| `defaultTopology` | `SINGLE` | Topologie de repli |
| `persistSessions` | `true` | Résumés de session |

## Méthodes core

| Méthode | Description |
|---------|-------------|
| `connect` / `disconnect` | Cycle de vie runtime |
| `run(task)` | Exécution multi-agents → `ExecutionResult` |
| `plan(task)` | Délibération seule |
| `onEvent(handler)` | Événements agent/tool |
| `createAgent` / memory | Contrôle avancé |

## API HTTP

```bash
curl http://localhost:4000/health

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

[Déploiement](/fr/deployment) · [SDK Python](/fr/guide/sdk-python).

## Suite

- [SDK Python](/fr/guide/sdk-python)  
- [Commandes](/fr/guide/commands)  
- [Vue API](/fr/api/overview)  
