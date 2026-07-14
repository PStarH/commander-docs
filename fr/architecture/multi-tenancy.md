# Multi-tenant

Isolation des rate limits, du storage, de la mémoire, du cache et du mapping des clés API par tenant. Activez `TENANT_PROVIDER=simple` (ou équivalent monorepo) en déploiement partagé.

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
