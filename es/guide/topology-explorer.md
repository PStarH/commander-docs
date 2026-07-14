# Explorador interactivo de topología

Elige la forma de la tarea. El motor de deliberación de Commander mapea señales similares a una de **cinco topologías canónicas**. Esta página es una ayuda a la decisión — no sustituye a `plan`.

## Árbol de decisión

```
¿La tarea es una pregunta clara con un solo responsable?
  SÍ → SINGLE
  NO  ↓
¿El trabajo forma un pipeline estricto (A luego B luego C)?
  SÍ → CHAIN
  NO  ↓
¿Pueden especialistas trabajar en paralelo y luego fusionar?
  SÍ → DISPATCH
  NO  ↓
¿Un líder debe delegar y replanificar?
  SÍ → ORCHESTRATOR
  NO  ↓
¿La calidad / riesgo exige crítica?
  SÍ → REVIEW
  si no → empieza con DISPATCH o pregunta a `commander plan`
```

## Tarjetas de topología

### SINGLE

| | |
|--|--|
| **Agentes** | 1 |
| **Ideal para** | FAQ, explicar algo simple, transform one-shot |
| **Coste** | Más bajo |
| **Riesgo** | Sin peer review |

```bash
npx tsx packages/core/src/cliEntry.ts plan "what does this function do?"
# a menudo → SINGLE
```

### CHAIN

| | |
|--|--|
| **Agentes** | Etapas secuenciales |
| **Ideal para** | Pipelines analizar → implementar → verificar |
| **Coste** | Medio |
| **Riesgo** | Un fallo de etapa bloquea la línea |

```bash
npx tsx packages/core/src/cliEntry.ts plan "migrate the auth module then update callers"
# a menudo → CHAIN
```

### DISPATCH

| | |
|--|--|
| **Agentes** | Especialistas en paralelo + sintetizador |
| **Ideal para** | Research, auditorías, análisis multi-ángulo |
| **Coste** | Más alto (paralelo) |
| **Riesgo** | Conflictos al fusionar |

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
# a menudo → DISPATCH
```

### ORCHESTRATOR

| | |
|--|--|
| **Agentes** | Líder + workers |
| **Ideal para** | Trabajo grande, ambiguo, multi-módulo |
| **Coste** | Alto |
| **Riesgo** | Cuello de botella del líder |

```bash
npx tsx packages/core/src/cliEntry.ts plan "redesign the billing system end to end"
# a menudo → ORCHESTRATOR
```

### REVIEW

| | |
|--|--|
| **Agentes** | Productor + crítico / merge |
| **Ideal para** | Código de alto riesgo, salida sensible a seguridad |
| **Coste** | Medio–alto |
| **Riesgo** | Latencia extra |

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## Selector rápido

| Si tu tarea es… | Prueba |
|-----------------|--------|
| Una pregunta, una respuesta | **SINGLE** |
| Pasos ordenados que dependen del anterior | **CHAIN** |
| Varias investigaciones independientes | **DISPATCH** |
| Alcance desconocido; necesitas un manager | **ORCHESTRATOR** |
| Correctitud > velocidad | **REVIEW** |

## Forzar una topología

```bash
npx tsx packages/core/src/cliEntry.ts run "your task" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts plan "your task" --topology review
```

Nombres canónicos: `single` · `chain` · `dispatch` · `orchestrator` · `review`.

## Relacionado

- [Árbol de decisión de topología](/es/guide/usage/topology-decision-tree)
- [Ejecutar tareas](/es/guide/usage/running-tasks)
- [Por qué Commander](/es/guide/why-commander)
- [Arquitectura multi-agente](/es/architecture/multi-agent)
