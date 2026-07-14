# Cookbook : refactor sûr

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module; keep public API stable"
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module; keep public API stable" --stream
```
