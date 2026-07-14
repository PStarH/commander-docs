# Pipeline de vérification

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Pipeline de vérification**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
npx tsx packages/core/src/cliEntry.ts run "your task" --stream
```

| Puerta | Comprueba |
|--------|-----------|
| Hallucination | Hechos inventados (señales / LLM-as-judge) |
| Consistency | Acuerdo entre agentes, sin contradicciones |
| Completeness | Dimensiones requeridas cubiertas |
| Accuracy | Alineación con material fuente |
| Safety | Contenido, inyección, secretos |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
