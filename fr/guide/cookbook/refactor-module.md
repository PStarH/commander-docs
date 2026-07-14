# Cookbook : refactor sûr

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Cookbook : refactor sûr**.

## Entrée rapide

```bash
git checkout -b chore/commander-refactor
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream

# cuando confíes:
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

| Problema | Acción |
|----------|--------|
| Demasiadas ediciones | Quédate en plan/suggest; acota paths |
| Módulo equivocado | Nombra `packages/foo/src/auth/*` |
| Merge flojo | `--topology chain` o `review` |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
