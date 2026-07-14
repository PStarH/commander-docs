# Cookbook : audit de sécurité d’un dépôt

**Objectif :** audit multi-agents avec streaming. **Temps :** ~10 min. **Risque :** surtout lecture.

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
npx tsx packages/core/src/cliEntry.ts run "audit..." --stream --topology review
```

## Checklist

- [ ] Plan avec topologie  
- [ ] Stream agents/tools  
- [ ] Résumé de findings  
- [ ] Pas de hang >2 min sans événements  

[Sécurité](/fr/guide/security) · [Topologie](/fr/guide/usage/topology-decision-tree)
