# Commandes CLI

Après build de `@commander/core` : binaire `commander`.  
Sans build :

```bash
npx tsx packages/core/src/cliEntry.ts
```

## Exécution

| Commande | Description |
|----------|-------------|
| `commander <task>` | Analyse rapide |
| `commander run <task>` | Pipeline multi-agents |
| `commander plan <task>` | Plan de délibération |
| `commander run <task> --stream` | Stream SSE |
| `commander run --file tasks.json` | Lot |
| `commander swarm` / `drive` / `goal` / `company` | Modes avancés |

## Interface

| Commande | Description |
|----------|-------------|
| `commander gui` | War Room (React + API) |
| `commander tui` | Dashboard terminal |
| `commander web` | Interface web |

## Analyse & config

| Commande | Description |
|----------|-------------|
| `commander review` | Code review P0–P3 |
| `commander status` | État système |
| `commander cost` | Coût |
| `commander mode` | Mode d’approbation |
| `commander doctor` | Diagnostics |
| `commander budget` | Budget tokens |
| `commander --debug` | Logs verbeux |

## Skills / session / saga

`skill list|view|create|pin` · `history` · `saga` · `checkpoint` · `compensation` · `resume` · `undo`

## Modes d’approbation

`plan` · `read-only` · `suggest` · `auto-edit` · `full-auto`

```bash
export COMMANDER_MODE=auto-edit
commander mode plan
```
