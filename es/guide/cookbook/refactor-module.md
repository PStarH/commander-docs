# Cookbook: refactor seguro

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module; keep public API stable"
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module; keep public API stable" --stream
git diff && pnpm test
```

[Modo plan](/es/guide/usage/plan-mode)
