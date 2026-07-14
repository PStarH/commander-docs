# Modo plan

El modo plan te deja ver **qué hará Commander antes de hacerlo**. Revisa estrategia, agentes y tools — sin riesgo de cambios no deseados.

## Por qué usarlo

- **Seguridad** — revisa el plan completo antes de tocar archivos  
- **Aprendizaje** — entiende cómo descompone la tarea  
- **Depuración** — ve topología, agentes y tools previstos  
- **Colaboración** — comparte e itera el plan con el equipo  

## Uso

> Tras el build, usa `commander` en lugar de `npx tsx packages/core/src/cliEntry.ts`.

```bash
# Activar modo plan
npx tsx packages/core/src/cliEntry.ts mode plan

# Luego cualquier tarea
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# O plan de un solo disparo
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## Salida del plan

```
┃ → Deliberating task...
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃
┃ → Subtasks:
┃   1. Analyze existing database schema
┃   2. Design migration plan
┃   3. Implement changes (parallel: 2 agents)
┃   4. Verify and test
```

## Indicador visual

El terminal muestra un **indicador de modo plan** cuando está activo, para que sepas si estás en plan o en ejecución.

## Relacionado

- [Ejecutar tareas](/es/guide/usage/running-tasks)  
- [Explorador de topología](/es/guide/topology-explorer)
