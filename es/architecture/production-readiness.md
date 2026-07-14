# Listo para producción

Commander incorpora primitivas típicas de sistemas distribuidos:

| Capacidad | Implementación |
|-----------|----------------|
| Circuit breakers | CLOSED / OPEN / HALF-OPEN por proveedor |
| Dead letter queue | NDJSON append-only, reenvío |
| Saga / compensación | Rollback de mutaciones |
| Checkpoints | SQLite + WAL |
| Caché semántica | SHA-256 + similitud |
| Multi-tenant | Cuotas, storage, memoria aislados |
| Métricas | Prometheus `/metrics` |

## Health

```bash
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
```

## Tests

6700+ tests en CI (unit, integración, chaos, e2e según monorepo).

## Relacionado

- [Despliegue](/es/deployment)  
- [Benchmarks](/es/guide/benchmarks)  
