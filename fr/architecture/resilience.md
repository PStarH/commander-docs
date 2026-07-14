# Résilience

Commander applique des primitives de systèmes distribués aux appels LLM.

| Mécanisme | Rôle |
|-----------|------|
| Circuit breaker | Isole un fournisseur en erreur |
| Chaîne de fallback | Passe au fournisseur suivant |
| DLQ | Classe et rejoue les échecs |
| Checkpoint / resume | Continue après crash |
| Saga | Compense les mutations |
| Backpressure | Protège sous charge |

```bash
npx tsx packages/core/src/cliEntry.ts doctor
curl http://localhost:4000/health/detailed
```


## Lié

- [Vue d’ensemble](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
