# Chaos testing

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Chaos testing**.

## Entrée rapide

```bash
# Capa L1 (LLM)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Varias capas
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# Suite amplia
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=ci-staging --duration=120
```

```bash
pnpm benchmark:chaos
pnpm benchmark:chaos:full
```

| Capa | Enfoque |
|------|---------|
| L1 | Fallos / latencia de LLM |
| L2 | Tools (timeout, error, poison) |
| L3 | Sistema (bus, checkpoint, memoria) |
| L4 | Aislamiento y cuotas multi-tenant |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
