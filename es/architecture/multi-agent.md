# Orquestación multi-agente

Commander coordina varios agentes sobre topologías canónicas elegidas por deliberación.

## Topologías

| Topología | Patrón |
|-----------|--------|
| SINGLE | Un agente, un pase |
| CHAIN | Etapas secuenciales |
| DISPATCH | Especialistas en paralelo + síntesis |
| ORCHESTRATOR | Líder que delega y replanifica |
| REVIEW | Productor + crítico |

Ver [Explorador de topología](/es/guide/topology-explorer).

## Coordinación

- **Message bus** — eventos entre agentes y sistema  
- **Handoff** — transferencia de contexto entre agentes  
- **Síntesis** — merge de salidas con resolución de conflictos  
- **Presupuesto de tokens** — reparto por rol y complejidad  

## Cuándo forzar topología

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review --stream
```

## Relacionado

- [Árbol de decisión](/es/guide/usage/topology-decision-tree)  
- [Runtime](/es/architecture/agent-runtime)  
