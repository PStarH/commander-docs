# Cadena de llamadas core

Camino de un request desde la entrada hasta el resultado verificado.

## Entradas

- CLI (`cliEntry.ts` / `commander`)
- SDK (`CommanderClient.run` / `plan`)
- HTTP (`/execute`, Architecture V2 `/v1/runs`)

## Pasos

1. **Carga de entorno** — keys, modo de aprobación, tenant  
2. **Deliberación** — clasifica la tarea, estima complejidad  
3. **Escalado de esfuerzo** — agentes 1–20  
4. **Router de topología** — SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW  
5. **Atomización** — sub-tareas si aplica  
6. **Runtime de agentes** — LLM ↔ tools en bucle  
7. **Verificación** — cinco puertas de calidad  
8. **Síntesis** — fusiona salidas multi-agente  
9. **Persistencia / eventos** — checkpoints, event log, métricas  

## Fallos y recuperación

| Fallo | Mecanismo |
|-------|-----------|
| Proveedor caído | Cadena de fallback + circuit breaker |
| Tool mutante fallida | Compensación / saga |
| Crash de proceso | Checkpoint SQLite WAL + resume |
| Salida de mala calidad | Reintento con contexto de gate |

## Relacionado

- [Runtime](/es/architecture/agent-runtime)  
- [Multi-agente](/es/architecture/multi-agent)  
- [Verificación](/es/architecture/verification)  
