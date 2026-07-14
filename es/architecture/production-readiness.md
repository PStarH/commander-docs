# Listo para producción

Primitivas de sistemas distribuidos aplicadas a workloads LLM.

| Capacidad | Implementación |
|-----------|----------------|
| Circuit breakers | CLOSED / OPEN / HALF-OPEN por proveedor |
| Dead letter queue | NDJSON append-only + replay |
| Saga / compensación | Rollback de mutaciones |
| Checkpoints | SQLite + WAL |
| Caché semántica | SHA-256 + similitud |
| Multi-tenant | Cuotas, storage, memoria |
| Métricas | Prometheus `/metrics` |

## Health

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Tests

6700+ tests en CI (unit, integración, chaos, e2e según monorepo).

## Relacionado

- [Despliegue](/es/deployment) · [Resiliencia](/es/architecture/resilience) · [Benchmarks](/es/guide/benchmarks)
