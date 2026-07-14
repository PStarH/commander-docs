# Chaîne d’appels core

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Chaîne d’appels core**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
npx tsx packages/core/src/cliEntry.ts run "your task" --stream
```

| Fallo | Mecanismo |
|-------|-----------|
| Proveedor caído | Cadena de fallback + circuit breaker |
| Tool mutante fallida | Compensación / saga |
| Crash de proceso | Checkpoint SQLite WAL + resume |
| Salida de mala calidad | Reintento con contexto de gate |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
