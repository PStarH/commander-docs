# Árbol de decisión de topología

Cómo el motor de deliberación elige entre las **cinco topologías canónicas**. Complementa al [Explorador interactivo](/es/guide/topology-explorer).

## Flujo mental

1. ¿Una pregunta clara, un responsable? → **SINGLE**  
2. ¿Pipeline estricto A→B→C? → **CHAIN**  
3. ¿Especialistas en paralelo + merge? → **DISPATCH**  
4. ¿Hace falta un lead que delegue y replanifique? → **ORCHESTRATOR**  
5. ¿Riesgo alto / hace falta crítica? → **REVIEW**  

## Señales típicas

| Señal en la tarea | Topología probable |
|-------------------|--------------------|
| “explica”, “qué es”, one-shot | SINGLE |
| “migra y luego actualiza callers” | CHAIN |
| “audita”, “investiga desde varios ángulos” | DISPATCH |
| “rediseña el sistema de billing end-to-end” | ORCHESTRATOR |
| “código de alto riesgo”, seguridad | REVIEW |

## Forzar topología

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts plan "task" --topology review
```

Nombres: `single` · `chain` · `dispatch` · `orchestrator` · `review`.

## Confirmar con plan

Siempre puedes validar sin mutar archivos:

```bash
npx tsx packages/core/src/cliEntry.ts plan "your real task here"
```

## Relacionado

- [Explorador de topología](/es/guide/topology-explorer)  
- [Multi-agente](/es/architecture/multi-agent)  
- [Ejecutar tareas](/es/guide/usage/running-tasks)
