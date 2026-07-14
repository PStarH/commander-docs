# Multi-tenant

Isolation des quotas, du storage, de la mémoire, du cache et des clés API par tenant.

## En pratique

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```

## Lié

- [Vue d’ensemble](/fr/architecture/overview)  
- [Prêt production](/fr/architecture/production-readiness)  
- [Sécurité](/fr/guide/security)
