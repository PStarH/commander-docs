# Référence API

L’API Commander a **deux couches**. La plupart des apps n’ont besoin que de la Layer 1.

## Layer 1 — Intégration publique (commencez ici)

| Surface | Package / entrée | Usage |
|---------|------------------|-------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | Terminal, scripts, CI |
| **SDK TypeScript** | `@commander/sdk` → `CommanderClient` | Apps Node |
| **HTTP API** | Serveur `:4000` | Clients polyglottes, Console |
| **SDK Python** | `commander-ai` (HTTP) | Python contre l’API |

### SDK TypeScript

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();
```

| Méthode | Rôle |
|---------|------|
| `connect` / `disconnect` | Cycle de vie |
| `run(task)` | Exécution complète → `ExecutionResult` |
| `plan(task)` | Délibération seule |
| `onEvent(handler)` | Stream d’événements |

> **npm :** monorepo d’abord. Publish public en cours. [Agent SDK](/fr/guide/sdk).

### HTTP

```bash
# Ops health server — default port 8081 (COMMANDER_OPS_HEALTH_PORT)
curl http://localhost:8081/health   # → 200 {"status":"ok"}
curl http://localhost:8081/ready    # → 200 (ready) / 503 (fail-closed)

# HTTP API base used by the Web Console client — default :4000 (VITE_API_BASE_URL).
# Requests carry `Authorization: Bearer <token>` when a token is configured.
curl http://localhost:4000/v1/actions \
  -H "Authorization: Bearer <token>"
```

V2 : `POST /v1/runs` — [Migration V2](/fr/guide/migration-v2).

### Python

```python
from commander import CommanderClient
```

[SDK Python](/fr/guide/sdk-python).

---

## Layer 2 — Composants d’orchestration runtime

Modules internes `@commander/core`. Pour **étendre** le runtime uniquement.

| Composant | Rôle |
|-----------|------|
| [Task Complexity Analyzer](/fr/api/task-complexity-analyzer) | Score → topologie |
| [Token Budget Allocator](/fr/api/token-budget-allocator) | Budget |
| [Three-Layer Memory](/fr/api/three-layer-memory) | Mémoire 3 couches |
| [Reflection Engine](/fr/api/reflection-engine) | Éval post-run |
| [Consensus Checker](/fr/api/consensus-checker) | Votes multi-modèles |

### Quand utiliser Layer 2

Topologie custom, recherche mémoire/consensus, tests d’un sous-système.

### Quand ne pas

« Lancer une tâche » → `CommanderClient`. Clients distants → HTTP.

### Exemple minimal

```typescript
import { TaskComplexityAnalyzer } from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});
// complexity: { level, score, factors, recommendedMode, tokenBudget, confidence }
```

Le partage du budget au runtime est géré en interne par le gestionnaire de budget de tokens — voir [Allocateur de budget tokens](/fr/api/token-budget-allocator).

Préférez `CommanderClient` aux singletons `getGlobal…` sauf état partagé voulu.

## Voir aussi

- [Commandes CLI](/fr/guide/commands)  
- [Console web](/fr/guide/web-console)  
- [Cookbook](/fr/guide/cookbook/)  
- [Vue d’architecture](/fr/architecture/overview)  
