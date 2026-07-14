# Comandos CLI

Los ejemplos usan el binario `commander` (tras compilar `@commander/core`).
Desde un checkout sin build:

```bash
npx tsx packages/core/src/cliEntry.ts
```

## Ejecución de tareas

| Comando | Descripción |
|---------|-------------|
| `commander <task>` | Análisis rápido |
| `commander run <task>` | Pipeline multi-agente completo |
| `commander plan <task>` | Plan de deliberación |
| `commander run <task> --stream` | Stream SSE en tiempo real |
| `commander run --file <tasks.json>` | Lote |
| `commander swarm <task>` | Descomposición paralela |
| `commander drive <task>` | Autónomo paso a paso |
| `commander goal <task>` | Convergencia multi-ronda |
| `commander company <task>` | Pipeline enterprise |

## Interfaz

| Comando | Descripción |
|---------|-------------|
| `commander gui` | War Room (React + API) |
| `commander tui` | Dashboard terminal |
| `commander web` | Interfaz web |

## Análisis

| Comando | Descripción |
|---------|-------------|
| `commander review` | Code review P0–P3 |
| `commander workers` | Research paralelo |
| `commander status` | Estado del sistema |
| `commander cost` | Coste |

## Configuración

| Comando | Descripción |
|---------|-------------|
| `commander mode [mode]` | plan / read-only / auto-edit / full-auto / suggest |
| `commander config` | Ajustes |
| `commander doctor` | Diagnósticos |
| `commander budget` | Presupuesto de tokens |

## Skills, sesión, saga

| Comando | Descripción |
|---------|-------------|
| `commander skill list\|view\|create\|pin` | Skills |
| `commander history [...]` | Sesiones |
| `commander saga` / `checkpoint` / `compensation` / `resume` / `undo` | Recuperación |

## Modos de aprobación

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts mode plan
commander mode plan
```
