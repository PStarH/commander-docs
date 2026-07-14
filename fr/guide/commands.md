# Commandes CLI

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Commandes CLI**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts
```

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts mode plan
commander mode plan
```

| Comando | Descripción |
|---------|-------------|
| `commander <task>` | Análisis rápido |
| `commander run <task>` | Pipeline multi-agente completo |
| `commander plan <task>` | Plan de deliberación |
| `commander run <task> --stream` | Stream SSE en tiempo real |
| `commander run --file <tasks.json>` | Lote |
| `commander swarm <task>` | Descomposición paralela |
| `commander drive <task>` | Autónomo paso a paso |
| `commander goal <task>` | Convergencia multi-ronda |
| `commander company <task>` | Pipeline enterprise |


| Comando | Descripción |
|---------|-------------|
| `commander gui` | War Room (React + API) |
| `commander tui` | Dashboard terminal |
| `commander web` | Interfaz web |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
