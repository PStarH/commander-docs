# Adaptateurs de canal

Ponts IM/webhook (Slack, Feishu, Teams, etc. selon monorepo) pour faire entrer des messages dans le runtime.

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
