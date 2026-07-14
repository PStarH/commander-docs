# Prêt production

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Prêt production**.

## Entrée rapide

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

| Capacidad | Implementación |
|-----------|----------------|
| Circuit breakers | CLOSED / OPEN / HALF-OPEN por proveedor |
| Dead letter queue | NDJSON append-only + replay |
| Saga / compensación | Rollback de mutaciones |
| Checkpoints | SQLite + WAL |
| Caché semántica | SHA-256 + similitud |
| Multi-tenant | Cuotas, storage, memoria |
| Métricas | Prometheus `/metrics` |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
