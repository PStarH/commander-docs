# Cookbook : refactoriser un module en sécurité

```bash
git checkout -b chore/commander-refactor
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module; keep public API stable"
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module; keep public API stable" --stream
git diff && pnpm test
```

## Checklist

- [ ] Plan correct avant écriture  
- [ ] Diff limité  
- [ ] Tests verts  
- [ ] Reversible avec git  

En cas de surplus d’éditions : restez en `plan`/`suggest` ; forcez `--topology chain` ou `review`.

[Mode plan](/fr/guide/usage/plan-mode)
