# Benchmarks

Commander mide **seguridad, fiabilidad, rendimiento, chaos y capacidad**. Los números del README del producto se re-ejecutan con scripts del monorepo.

## Matriz headline

| Suite | Cobertura | Resultado (doc producto) |
|-------|-----------|---------------------------|
| Chaos | 255 synth + 55 mut | ~55.7% pass |
| Red Team | 47 escenarios | 100% defensa (doc) |
| AgentDojo | 12 casos | 100% defensa (doc) |
| RealWorld | 50 casos | 96% pass (doc) |
| GAIA / SLO | diario | medido en CI/scripts |

## Reproducir

```bash
pnpm benchmark:all
pnpm benchmark:redteam
pnpm benchmark:agentdojo
pnpm benchmark:chaos
pnpm bench:slo
pnpm check:readiness
```

Fuente de verdad: monorepo [`BENCHMARK.md`](https://github.com/PStarH/Commander/blob/master/BENCHMARK.md).

## Relacionado

- [Chaos testing](/es/guide/usage/chaos-testing)  
- [Seguridad](/es/guide/security)  
- [Producción](/es/architecture/production-readiness)
