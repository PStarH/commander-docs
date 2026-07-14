# Tráfico sombra (shadow traffic)

Ejecuta una copia “sombra” del tráfico de producción (o de un runner) para comparar comportamiento sin afectar a usuarios reales.

## Idea

1. Levantar un runner sombra  
2. Replicar o reenviar requests  
3. Medir drift (diferencias de salida, errores, latencia)  

## Ejemplo (monorepo)

```bash
# Runner sombra
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &

# Servir API principal (según tu setup)
npx tsx packages/core/src/cli/index.ts serve

# Analizar drift
npx tsx packages/core/src/cli/commands/shadow.ts drift
```

> Los paths exactos de comandos shadow pueden evolucionar; confirma en el monorepo `packages/core/src/cli/commands/shadow.ts`.

## Cuándo usarlo

- Validar un cambio de topología o proveedor  
- Comparar modelo barato vs caro  
- Regresiones de calidad antes de promover a prod  

## Relacionado

- [Despliegue](/es/deployment)  
- [Benchmarks](/es/guide/benchmarks)
