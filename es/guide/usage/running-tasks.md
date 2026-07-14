# Ejecutar tareas

Commander ofrece varias formas de ejecutar tareas según lo que necesites.

> **CLI desde el monorepo:** `npx tsx packages/core/src/cliEntry.ts …`  
> **Tras el build:** `commander …`  
> Los ejemplos de abajo usan la forma del monorepo.

## Tarea rápida

Para peticiones simples con respuesta inmediata:

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

Commander analiza la tarea, elige la topología óptima, ejecuta y devuelve el resultado — todo en un paso.

## Pipeline de ejecución completo

Para tareas multi-paso complejas:

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

El comando `run` activa el pipeline completo:

1. **Deliberación** — complejidad y dependencias  
2. **Escalado de esfuerzo** — cuántos agentes asignar  
3. **Enrutado de topología** — patrón de ejecución  
4. **Atomización** — descomposición en subtareas  
5. **Ejecución** — orquestación multi-agente con tools  
6. **Verificación** — 5 puertas de calidad (alucinación, consistencia, completitud, exactitud, seguridad)

## Modo plan

Previsualiza el plan antes de cambiar nada:

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

El plan muestra: score de complejidad, topología, agentes y roles, proveedor y fallback, presupuesto de tokens estimado.

## Modo watch (SSE)

Ejecuta con eventos en streaming en tiempo real:

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

Watch emite por SSE: pasos de deliberación, tool calls y resultados, checkpoints de verificación, uso de tokens.

## Procesamiento por lotes

```bash
npx tsx packages/core/src/cliEntry.ts run --file tasks.json
# [{"task": "analyze module A"}, {"task": "test module B"}]
```

## Modos de aprobación

| Modo | Comportamiento | Caso de uso |
|------|----------------|-------------|
| `plan` | Solo muestra el plan | Revisar antes de ejecutar |
| `read-only` | Solo lectura | Code review, análisis |
| `auto-edit` | Edita sin pedir permiso | Flujo de desarrollo |
| `full-auto` | Totalmente autónomo | CI/CD, lotes |
| `suggest` | Sugiere y espera | Aprendizaje, tutoriales |

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts mode auto-edit
```

## Relacionado

- [Modo plan](/es/guide/usage/plan-mode)  
- [Modo watch](/es/guide/usage/watch-mode)  
- [Comandos](/es/guide/commands)
