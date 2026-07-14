# Trafic fantôme (shadow)

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Trafic fantôme (shadow)**.

## Entrée rapide

```bash
# Runner sombra
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &

# Servir API principal (según tu setup)
npx tsx packages/core/src/cli/index.ts serve

# Analizar drift
npx tsx packages/core/src/cli/commands/shadow.ts drift
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
