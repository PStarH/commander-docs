# Cookbook

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Cookbook**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts <command>
# tras build: commander <command>
```

| Receta | Tiempo | Practicas |
|--------|--------|-----------|
| [Auditoría de seguridad](/es/guide/cookbook/security-audit) | ~10 min | DISPATCH, streaming, gates |
| [Refactor seguro](/es/guide/cookbook/refactor-module) | ~15 min | plan → run → review |
| [CI full-auto lint](/es/guide/cookbook/ci-full-auto) | ~15 min | full-auto, PR |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
