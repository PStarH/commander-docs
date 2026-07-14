# Orchestration multi-agents

Commander coordonne plusieurs agents sur des **topologies canoniques** choisies par la délibération.

## Topologies

| Topologie | Motif | Cas typique |
|-----------|-------|-------------|
| **SINGLE** | Un agent | FAQ, one-shot |
| **CHAIN** | Pipeline A→B→C | Migrer puis mettre à jour |
| **DISPATCH** | Parallèle + synthèse | Audit, research multi-angle |
| **ORCHESTRATOR** | Lead + workers | Gros chantier ambigu |
| **REVIEW** | Producteur + critique | Code à haut risque |

## Coordination

- **Message bus** — événements inter-agents et système  
- **Handoff** — transfert de contexte  
- **Synthèse** — fusion des sorties  
- **Budget tokens** — répartition par rôle  

## Contrôle CLI

```bash
npx tsx packages/core/src/cliEntry.ts plan "cross-repo security audit"
npx tsx packages/core/src/cliEntry.ts run "audit" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts run "task" --agent-count 4
```

## Lié

- [Explorateur de topologie](/fr/guide/topology-explorer)  
- [Arbre de décision](/fr/guide/usage/topology-decision-tree)  
- [Runtime](/fr/architecture/agent-runtime)
