# Arbre de décision des topologies

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Arbre de décision des topologies**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts plan "task" --topology review
```

```bash
npx tsx packages/core/src/cliEntry.ts plan "your real task here"
```

| Señal en la tarea | Topología probable |
|-------------------|--------------------|
| “explica”, “qué es”, one-shot | SINGLE |
| “migra y luego actualiza callers” | CHAIN |
| “audita”, “investiga desde varios ángulos” | DISPATCH |
| “rediseña el sistema de billing end-to-end” | ORCHESTRATOR |
| “código de alto riesgo”, seguridad | REVIEW |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
