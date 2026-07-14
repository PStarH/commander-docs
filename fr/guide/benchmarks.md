# Benchmarks

**Benchmarks.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Suite | Coverage | Result (as documented) |
|-------|----------|------------------------|
| Chaos Engineering | 255 synthetic + 55 mutation | 55.7% pass rate |
| Red Team | 47 scenarios, 8 attack categories | 100% defense |
| AgentDojo | 12 security test cases | 100% defense |
| RealWorld | 50 production-like cases | 96% pass rate |
| GAIA Spine | Core capability | Running daily |
| SLO | API success / latency | Measured daily |


## Contenu principal

### Headline matrix (product README)

En pratique, **Headline matrix (product README)** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Reliability SLO Targets

En pratique, **Reliability SLO Targets** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Health Check Components

En pratique, **Health Check Components** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Chaos Engineering Benchmark

En pratique, **Chaos Engineering Benchmark** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Topology Performance

En pratique, **Topology Performance** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Provider Latency

En pratique, **Provider Latency** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Test Suite

En pratique, **Test Suite** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

### Reproducing Benchmarks

En pratique, **Reproducing Benchmarks** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/benchmarks) pour le détail exhaustif.

## Exemples (code inchangé)

```bash
pnpm benchmark:all          # multi-suite readiness
pnpm benchmark:redteam      # 47 scenarios
pnpm benchmark:agentdojo    # injection suite
pnpm benchmark:chaos        # chaos (simulated default)
pnpm bench:slo              # SLO baseline
pnpm check:readiness        # baseline freshness
```

```bash
# Run full 255-case benchmark
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=bench --duration=300

# Run specific domain
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=bench --fault-types=payment_timeout,rate_limit
```

```
Primary Provider → Timeout/Error → Circuit Breaker OPEN → Next Provider → ...
```

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
