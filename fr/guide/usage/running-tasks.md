# Exécuter des tâches

Commander propose plusieurs façons d’exécuter une tâche selon le besoin.

> **CLI monorepo :** `npx tsx packages/core/src/cliEntry.ts …`  
> **Après build :** `commander …`  
> Les exemples ci-dessous utilisent la forme monorepo.

## Tâche rapide

Pour une réponse immédiate :

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

Commander analyse, choisit la topologie, exécute et renvoie le résultat — en une étape.

## Pipeline complet

Pour les tâches multi-étapes :

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

Le pipeline `run` :

1. **Délibération** — complexité et dépendances  
2. **Scale d’effort** — nombre d’agents  
3. **Routage de topologie** — motif d’exécution  
4. **Atomisation** — sous-tâches  
5. **Exécution** — multi-agents + tools  
6. **Vérification** — 5 portes (hallucination, cohérence, complétude, exactitude, sécurité)

## Mode plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

Affiche score, topologie, agents, fournisseur/fallback, budget tokens — **sans modifier de fichiers**.

## Mode watch (SSE)

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

Stream : délibération, tool calls, gates, usage tokens.

## Lot

```bash
npx tsx packages/core/src/cliEntry.ts run --file tasks.json
# [{"task": "analyze module A"}, {"task": "test module B"}]
```

## Modes d’approbation

| Mode | Comportement | Cas d’usage |
|------|--------------|-------------|
| `plan` | Plan seul | Revue avant exécution |
| `read-only` | Lecture | Review, analyse |
| `auto-edit` | Édition auto | Dev local |
| `full-auto` | Autonome | CI/CD |
| `suggest` | Suggestion + attente | Tutoriels |

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts mode auto-edit
```

## Lié

- [Mode plan](/fr/guide/usage/plan-mode) · [Watch](/fr/guide/usage/watch-mode) · [Commandes](/fr/guide/commands)
