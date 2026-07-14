# Équipes d’agents

| Motif | Topologie typique |
|-------|-------------------|
| Un expert | SINGLE |
| Pipeline analyse → impl → test | CHAIN |
| Security + deps en parallèle | DISPATCH |
| Architecte + N workers | ORCHESTRATOR |
| Implémenteur + critique | REVIEW |

```bash
npx tsx packages/core/src/cliEntry.ts plan "cross-repo security audit"
npx tsx packages/core/src/cliEntry.ts run "audit" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts run "task" --agent-count 4
```

Handoffs via message bus ; lignée pour l’audit.

[Multi-agents](/fr/architecture/multi-agent) · [Explorateur](/fr/guide/topology-explorer)
