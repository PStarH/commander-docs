# FAQ

## Général

### Qu’est-ce que Commander ?

Un moteur d’orchestration multi-agents qui coordonne plusieurs agents IA sur 5 topologies canoniques, avec 25 fournisseurs LLM et 18 tools intégrés.

### Différence avec les outils de coding IA classiques ?

La plupart utilisent un seul agent et un seul modèle. Commander orchestre **plusieurs agents**, choisit la topologie selon la complexité, streame via SSE, applique des portes de qualité et des primitives de production.

### Open source ?

Oui, MIT.

## Configuration

### Plusieurs clés API ?

Non. **Une suffit**. `OPENAI_API_KEY` (ou autre) suffit pour l’auto-détection. Le failover apparaît quand vous en configurez plusieurs.

### Hors ligne ?

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### npm publié ?

Publication publique **en cours**. En attendant, clonez le monorepo. Voir [Agent SDK](/fr/guide/sdk).

## Usage

### Peut-il modifier mes fichiers ?

Oui par défaut — contrôlez avec les modes : `plan`, `read-only`, `suggest`, `auto-edit`, `full-auto`.

### En CI/CD ?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

### Combien d’agents ?

1–20 selon la complexité.

### Les cinq topologies ?

| Topologie | Quand |
|-----------|-------|
| **SINGLE** | One-shot |
| **CHAIN** | Pipeline séquentiel |
| **DISPATCH** | Spécialistes en parallèle + synthèse |
| **ORCHESTRATOR** | Lead qui délègue |
| **REVIEW** | Produire puis critiquer |

Voir [Arbre de topologie](/fr/guide/usage/topology-decision-tree).

## Entreprise

### Multi-tenant ? On-premise ?

Oui. Voir [Multi-tenant](/fr/architecture/multi-tenancy) et [Déploiement](/fr/deployment).

## Données

Le code reste sur votre machine (ou serveur) sauf envoi vers les fournisseurs LLM **que vous configurez**. Pour le sensible : Ollama/vLLM ou VPC.

## Lié

- [Dépannage](/fr/guide/troubleshooting)
- [Installation](/fr/guide/installation)
- [Communauté](/fr/community)
