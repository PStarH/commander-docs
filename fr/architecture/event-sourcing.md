# Event sourcing et recovery

Journal append-only (WAL + hash chain) pour replay déterministe, audit et recovery des runs zombies au démarrage. Le bootstrap de recovery reprend les runs incomplets lorsque c’est sûr.

## En pratique

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```

Observez le comportement via le stream CLI, la console web et les métriques Prometheus.

## Lié

- [Vue d’ensemble](/fr/architecture/overview)  
- [Prêt production](/fr/architecture/production-readiness)  
- [Sécurité](/fr/guide/security)  
