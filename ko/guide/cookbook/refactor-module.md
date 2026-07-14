# 쿡북: 안전한 모듈 리팩터

```bash
git checkout -b chore/commander-refactor
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module; keep public API stable"
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module; keep public API stable" --stream
git diff && pnpm test
```

[플랜 모드](/ko/guide/usage/plan-mode)
