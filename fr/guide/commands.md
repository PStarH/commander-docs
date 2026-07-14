# Commandes CLI

```bash
npx tsx packages/core/src/cliEntry.ts   # sources
commander                               # après build
```

## Exécution

| Commande | Description |
|----------|-------------|
| `commander run <task>` | Pipeline multi-agents |
| `commander plan <task>` | Plan de délibération |
| `commander run <task> --stream` | Stream SSE |
| `commander swarm` / `drive` / `goal` / `company` | Modes avancés |

## Interface

`commander gui` · `tui` · `web`

## Config

`commander mode` · `config` · `doctor` · `budget` · `--debug`

## Modes d’approbation

`plan` · `read-only` · `suggest` · `auto-edit` · `full-auto`

```bash
export COMMANDER_MODE=auto-edit
```
