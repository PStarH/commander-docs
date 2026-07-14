# Benchmarks

Commander mesure sécurité, fiabilité, perf, chaos et capacité.

## Matrice (doc produit)

| Suite | Couverture |
|-------|------------|
| Chaos | 255 synth + 55 mut |
| Red Team | 47 scénarios |
| AgentDojo | 12 cas |
| RealWorld | 50 cas |
| GAIA / SLO | quotidien |

## Reproduire

```bash
pnpm benchmark:all
pnpm benchmark:redteam
pnpm benchmark:agentdojo
pnpm benchmark:chaos
pnpm bench:slo
pnpm check:readiness
```

Source : monorepo [`BENCHMARK.md`](https://github.com/PStarH/Commander/blob/master/BENCHMARK.md).

[Chaos testing](/fr/guide/usage/chaos-testing) · [Sécurité](/fr/guide/security)
