# Arbre de supervision

Isolation des pannes et redémarrage contrôlé des agents/processus (esprit OTP) pour limiter les cascades d’échec.

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
