# 쿡북: CI full-auto lint

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

규칙: 일회성 브랜치/PR, 최소 시크릿, 로컬 dry-run, 로그 아티팩트. main force-push 금지.

[FAQ](/ko/guide/faq)
