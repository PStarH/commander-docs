# Preparación para producción

Commander se diseña para producción desde el día uno: observabilidad, seguridad y fiabilidad en cada componente.

## Matriz

| Capacidad       | Estado                                          |
| --------------- | ----------------------------------------------- |
| Tipos           | TypeScript strict, cero `as any` / `@ts-ignore` |
| Errores         | Cero catch vacíos en 100+ módulos               |
| Métricas        | Prometheus/OpenMetrics + labels de tenant       |
| Tracing         | Spans persistentes, OpenTelemetry               |
| Crash safety    | Checkpoints SQLite WAL + hash chain             |
| Circuit breaker | 5 fallos → 30s open → half-open                 |
| DLQ             | 7 categorías, 15 modos, replay                  |
| Multi-tenant    | Rate limits, cuotas, aislamiento storage/cache  |
| Seguridad       | Gateway 7 capas, DLP, tokens, Bearer, CORS      |
| Event sourcing  | WAL SHA-256, snapshots, replay determinista     |
| Plugins         | Sandbox de carga; permisos ≤ sistema principal  |

## Mecanismos

- **Circuit breaker** — registro por provider
- **DLQ** — fallos no recuperables persistidos
- **Compensation** — rollback de tools de mutación + Saga
- **Checkpointer** — WAL atomic por paso
- **Recovery bootstrapper** — reanuda o aborta runs zombi al arrancar

## Observabilidad

```typescript
getMetricsCollector().exportOpenMetrics();
```

Endpoints: `/health`, `/ready`, `/metrics`, `/health/detailed`. Dashboards Grafana (negocio + ops).

## Tests

6700+ unit/integration/chaos/e2e, aislamiento multi-tenant, permisos de plugins, stress.

```
npx tsx --test tests/*.test.ts
npx tsc --noEmit
```

## Relacionado

- [Agent Runtime](/es/architecture/agent-runtime)
- [Verificación](/es/architecture/verification)
- [Despliegue](/es/deployment)
