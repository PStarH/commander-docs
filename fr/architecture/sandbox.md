# Sandbox de sécurité

Profils limitant filesystem, réseau et syscalls pour shell/scripts et multi-tenant strict.

## En pratique

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```

## Lié

- [Vue d’ensemble](/fr/architecture/overview)  
- [Prêt production](/fr/architecture/production-readiness)  
- [Sécurité](/fr/guide/security)
