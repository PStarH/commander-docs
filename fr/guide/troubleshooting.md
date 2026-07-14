# Dépannage

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Dépannage**.

## Entrée rapide

```bash
pnpm install && pnpm build
```

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor --reset
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
