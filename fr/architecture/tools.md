# Tools

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Tools**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
npx tsx packages/core/src/cliEntry.ts run "your task" --stream
```

| Capacidad | Por qué importa |
|-----------|-----------------|
| Schema de argumentos | Menos tool calls basura |
| Timeouts | Evita runs colgados |
| Políticas / aprobación | Tools peligrosas bajo control |
| Compensación | Rollback si muta estado |
| Caché de resultados | Menos trabajo redundante |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
