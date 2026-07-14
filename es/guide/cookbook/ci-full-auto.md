# Cookbook: CI full-auto lint

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

En Actions: clonar Commander, instalar, lanzar con secret `OPENAI_API_KEY`, revisar `git diff` en PR.

[FAQ](/es/guide/faq)
