# Cookbook: refactorizar un módulo con seguridad

**Objetivo:** plan → ejecución controlada → verificar diff y tests.  
**Tiempo:** ~15 min

## 1. Rama limpia

```bash
git checkout -b chore/commander-refactor
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

## 2. Plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

Revisa: ¿toca solo los paths esperados? ¿topología razonable?

## 3. Suggest o auto-edit

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream

# cuando confíes:
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

## 4. Verificar

```bash
git diff
pnpm test
```

## Checklist

- [ ] Plan correcto antes de escribir  
- [ ] Diff acotado  
- [ ] Tests/typecheck verdes  
- [ ] Reversible con git  

## Fallos

| Problema | Acción |
|----------|--------|
| Demasiadas ediciones | Quédate en plan/suggest; acota paths |
| Módulo equivocado | Nombra `packages/foo/src/auth/*` |
| Merge flojo | `--topology chain` o `review` |

## Relacionado

- [Modo plan](/es/guide/usage/plan-mode) · [Ejecutar tareas](/es/guide/usage/running-tasks)
