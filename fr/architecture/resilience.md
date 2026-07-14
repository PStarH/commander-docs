# Résilience

| Mécanisme | Rôle |
|-----------|------|
| Circuit breaker | Isole un fournisseur malade |
| Chaîne de fallback | Passe au suivant |
| DLQ | Classe et rejoue les échecs |
| Checkpoint / resume | Continue après crash |
| Saga | Compense les mutations |
| Backpressure | Protège sous charge |

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```

## Chaos

```bash
pnpm benchmark:chaos
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```

## Lié

- [Prêt production](/fr/architecture/production-readiness)  
- [Chaos testing](/fr/guide/usage/chaos-testing)  
- [Event sourcing](/fr/architecture/event-sourcing)
