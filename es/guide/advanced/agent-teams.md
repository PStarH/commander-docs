# Equipos de agentes

Los equipos agrupan roles (lead, specialist, reviewer) bajo una topología. La deliberación puede proponer un equipo; tú también puedes forzar conteo y topología.

## Patrones

| Patrón | Topología típica |
|--------|------------------|
| Un experto | SINGLE |
| Pipeline analista → implementador → tester | CHAIN |
| Security + deps + licenses en paralelo | DISPATCH |
| Arquitecto + N implementadores | ORCHESTRATOR |
| Implementador + crítico | REVIEW |

## Control desde CLI

```bash
npx tsx packages/core/src/cliEntry.ts plan "cross-repo security audit"
npx tsx packages/core/src/cliEntry.ts run "cross-repo security audit" --stream --topology dispatch
npx tsx packages/core/src/cliEntry.ts run "task" --agent-count 4
```

## Handoffs

Los agentes pueden transferir contexto vía handoff / message bus. El runtime mantiene linaje para auditoría.

## Relacionado

- [Multi-agente](/es/architecture/multi-agent)  
- [Explorador de topología](/es/guide/topology-explorer)
