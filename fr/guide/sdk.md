# Agent SDK (TypeScript)

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Agent SDK (TypeScript)**.

## Entrée rapide

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

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

```typescript
const plan = await client.plan('refactor the auth module');
const unsub = client.onEvent((e) => console.log(e.type, e.data));
await client.run('debug the failing test');
unsub();
```

| Método | Rol |
|--------|-----|
| `connect` / `disconnect` | Ciclo de vida |
| `run` | Ejecución |
| `plan` | Solo deliberación |
| `onEvent` | Stream |
| memoria / `createAgent` | Avanzado |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
