# Cache

Cache exacte (SHA-256) et sémantique pour éviter les appels LLM/tools redondants, par tenant.

## En pratique

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```

## Lié

- [Vue d’ensemble](/fr/architecture/overview)  
- [Prêt production](/fr/architecture/production-readiness)  
- [Sécurité](/fr/guide/security)
