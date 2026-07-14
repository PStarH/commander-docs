# Prêt pour la production

Primitives de systèmes distribués appliquées aux workloads LLM.

| Capacité | Implémentation |
|----------|----------------|
| Circuit breakers | CLOSED / OPEN / HALF-OPEN par fournisseur |
| Dead letter queue | NDJSON append-only + replay |
| Saga / compensation | Rollback des mutations |
| Checkpoints | SQLite + WAL |
| Cache sémantique | SHA-256 + similarité |
| Multi-tenant | Quotas, storage, mémoire isolés |
| Métriques | Prometheus `/metrics` |

## Health

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Tests

6700+ tests en CI (unit, intégration, chaos, e2e selon monorepo).

## Lié

- [Déploiement](/fr/deployment)  
- [Résilience](/fr/architecture/resilience)  
- [Benchmarks](/fr/guide/benchmarks)
