# Cookbook : CI full-auto lint

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Cookbook : CI full-auto lint**.

## Entrée rapide

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

```yaml
name: Commander lint fix
on: { workflow_dispatch: {} }
jobs:
  fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: |
          git clone --depth 1 https://github.com/PStarH/Commander.git /tmp/Commander
          cd /tmp/Commander && pnpm install
      - env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          COMMANDER_MODE: full-auto
        run: npx tsx /tmp/Commander/packages/core/src/cliEntry.ts run "fix all lint errors" --stream
      - run: git diff --stat
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
