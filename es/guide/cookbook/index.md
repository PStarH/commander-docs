# Cookbook

Recetas de extremo a extremo. Cada página: **objetivo → comandos → señales de éxito → modos de fallo**.

| Receta | Tiempo | Practicas |
|--------|--------|-----------|
| [Auditoría de seguridad](/es/guide/cookbook/security-audit) | ~10 min | Análisis tipo DISPATCH, streaming, gates |
| [Refactor seguro de un módulo](/es/guide/cookbook/refactor-module) | ~15 min | Plan → run → review |
| [CI full-auto lint](/es/guide/cookbook/ci-full-auto) | ~15 min | Modo no interactivo, códigos de salida |

## Convenciones

Desde la raíz del monorepo tras `pnpm install`, con una API key exportada:

```bash
npx tsx packages/core/src/cliEntry.ts <command>
# Tras build: commander <command>
```

¿Nuevo en Commander? Empieza por [Inicio rápido](/es/guide/getting-started).
