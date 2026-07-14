# Cookbook: CI full-auto para lint

**Objetivo:** Commander no interactivo en CI para arreglar lint.  
**Riesgo:** alta autonomía — siempre vía PR.

## Reglas

1. Rama desechable / PR — nunca force-push a main  
2. Secrets mínimos  
3. Dry-run local primero  
4. Logs como artefactos  

## Dry-run local

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

## Esquema GitHub Actions

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

## Checklist

- [ ] Job no interactivo  
- [ ] Logs con deliberación  
- [ ] Diff revisado por humano  
- [ ] Sin secretos en logs  

## Relacionado

- [FAQ](/es/guide/faq) · [Despliegue](/es/deployment)
