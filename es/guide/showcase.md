# Showcase

Documentación en español de **Showcase**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
npx tsx packages/core/src/cliEntry.ts run "your task" --stream
```

| Project | How Commander is used | Link |
|---------|------------------------|------|
| *Your project* | *e.g. CI security audit + streaming review* | *URL* |


| Pattern | Docs |
|---------|------|
| Security audit stream | [Cookbook: security audit](/guide/cookbook/security-audit) |
| Safe module refactor | [Cookbook: refactor](/guide/cookbook/refactor-module) |
| CI full-auto lint | [Cookbook: CI](/guide/cookbook/ci-full-auto) |
| Web Console ops | [Web Console](/guide/web-console) |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
