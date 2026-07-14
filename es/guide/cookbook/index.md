# Cookbook

Documentación en español de **Cookbook**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```bash
# Source checkout
npx tsx packages/core/src/cliEntry.ts <command>

# After building @commander/core
commander <command>
```

| Recipe | Time | What you practice |
|--------|------|-------------------|
| [Security audit a repo](/guide/cookbook/security-audit) | ~10 min | DISPATCH-style analysis, streaming, gates |
| [Refactor a module safely](/guide/cookbook/refactor-module) | ~15 min | Plan mode → run → review |
| [CI full-auto lint fix](/guide/cookbook/ci-full-auto) | ~15 min | Non-interactive mode, exit codes |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
