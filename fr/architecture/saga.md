# Transactions Saga

Compensation ordonnée des mutations lorsqu’une étape échoue au milieu d’un pipeline multi-agents. Indispensable pour tools qui écrivent sur le disque ou des systèmes externes.

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
