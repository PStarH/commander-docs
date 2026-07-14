# Exécuter des tâches

Commander propose plusieurs façons d’exécuter une tâche selon le besoin.

> **CLI monorepo :** `npx tsx packages/core/src/cliEntry.ts …`  
> **Après build :** `commander …`

## Tâche rapide

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

Analyse, topologie, exécution et résultat en une étape.

## Pipeline complet

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

1. Délibération · 2. Scale d’effort · 3. Topologie · 4. Atomisation · 5. Exécution multi-agents · 6. Vérification (5 portes)

## Plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

Montre complexité, topologie, agents, fournisseur, budget tokens — sans muter de fichiers.

## Watch (SSE)

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

Stream : délibération, tools, vérifications, tokens.

## Lot

```bash
npx tsx packages/core/src/cliEntry.ts run --file tasks.json
```

## Modes d’approbation

| Mode | Comportement |
|------|--------------|
| `plan` | Plan seul |
| `read-only` | Lecture |
| `auto-edit` | Édition auto |
| `full-auto` | Autonome (CI) |
| `suggest` | Suggestion + attente |

```bash
export COMMANDER_MODE=auto-edit
```

## Lié

- [Mode plan](/fr/guide/usage/plan-mode) · [Watch](/fr/guide/usage/watch-mode) · [Commandes](/fr/guide/commands)
