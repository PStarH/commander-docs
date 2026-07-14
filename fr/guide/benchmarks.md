# Benchmarks

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Benchmarks**.

## Entrée rapide

```bash
pnpm benchmark:all
pnpm benchmark:redteam
pnpm benchmark:agentdojo
pnpm benchmark:chaos
pnpm bench:slo
pnpm check:readiness
```

| Suite | Cobertura | Resultado (doc producto) |
|-------|-----------|---------------------------|
| Chaos | 255 synth + 55 mut | ~55.7% pass |
| Red Team | 47 escenarios | 100% defensa (doc) |
| AgentDojo | 12 casos | 100% defensa (doc) |
| RealWorld | 50 casos | 96% pass (doc) |
| GAIA / SLO | diario | medido en CI/scripts |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
