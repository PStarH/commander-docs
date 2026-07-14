# Référence API

**Référence API.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Couche 1 — Intégration publique (commencez ici)

| Surface | Paquet / entrée | Idéal pour |
|---------|-----------------|------------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | Terminal, scripts, CI |
| **SDK TypeScript** | `@commander/sdk` → `CommanderClient` | Embed dans des apps Node |
| **API HTTP** | Serveur `:4000` | Clients polyglottes, console web |
| **SDK Python** | `commander-ai` (client HTTP) | Python contre l’API server |

### SDK TypeScript

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

const c = await createClient();
await c.run('explain the architecture');
await c.disconnect();
```

| Méthode | Rôle |
|---------|------|
| `connect` / `disconnect` | Cycle de vie |
| `run(task)` | Exécution complète → `ExecutionResult` |
| `plan(task)` | Délibération seule |
| `onEvent(handler)` | Stream d’événements agent/tool |
| `createAgent` / mémoire | Contrôle de session avancé |

> **Statut npm :** monorepo-first ; publication publique en cours. Voir [Agent SDK](/fr/guide/sdk).

### HTTP (serveur)

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

API durable Architecture V2 : `POST /v1/runs` — voir [Migration V2](/fr/guide/migration-v2).

### Python

```python
from commander import CommanderClient
# client httpx fin → API server
```

[Python SDK](/fr/guide/sdk-python).

---

## Couche 2 — Composants d’orchestration runtime

Ces modules pilotent délibération, budget, mémoire et vérification dans `@commander/core`. Utilisez-les pour **étendre** le runtime — pas pour l’intégration produit courante.

| Composant | Rôle |
|-----------|------|
| [Analyseur de complexité](/fr/api/task-complexity-analyzer) | Scorer la tâche → recommander une topologie |
| [Orchestrateur adaptatif](/fr/api/adaptive-orchestrator) | Plan multi-agents + coordination |
| [Budget de tokens](/fr/api/token-budget-allocator) | Répartition du budget |
| [Mémoire à 3 couches](/fr/api/three-layer-memory) | Working · episodic · long-term |
| [Moteur de réflexion](/fr/api/reflection-engine) | Évaluation post-run |
| [Consensus](/fr/api/consensus-checker) | Votes multi-modèles à haut risque |
| [Inspecteur](/fr/api/inspector-agent) | Santé / détection d’issues |

### Quand utiliser la couche 2

- Construire une topologie ou un planner custom  
- Rechercher mémoire et consensus  
- Tests isolant un sous-système  

### Quand **ne pas** utiliser la couche 2

- Features qui ont juste besoin de « lance cette tâche » → `CommanderClient`  
- Clients distants multi-langues → HTTP  

### Exemple minimal couche 2

```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
} from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

const allocator = new TokenBudgetAllocator({ baseBudget: 100_000 });
const budget = allocator.allocate(
  complexity.recommendedTopology,
  complexity.score,
  3,
);
```

### Accesseurs globaux

Certains composants exposent des singletons de process (utilisés par runtime/SDK) :

- `getGlobalTaskComplexityAnalyzer()`
- `getGlobalAdaptiveOrchestrator()`
- `getGlobalTokenBudgetAllocator()`
- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalConsensusChecker()`
- `getGlobalInspectorAgent()`

Préférez `CommanderClient` sauf besoin d’état partagé process-wide.

---

## Profondeur architecture

Conception des sous-systèmes : [Architecture](/fr/architecture/overview), [Runtime](/fr/architecture/agent-runtime), [Vérification](/fr/architecture/verification), [Sécurité](/fr/guide/security).

## Guides liés

- [Commandes CLI](/fr/guide/commands)  
- [Console web](/fr/guide/web-console)  
- [Cookbook](/fr/guide/cookbook/)  
