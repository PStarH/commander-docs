# Chaos testing

Commander incluye harness de chaos para validar resiliencia del runtime (capas L1–L4: LLM, tools, sistema, tenant).

## Idea

Inyectar fallos controlados (timeouts de proveedor, tools rotas, presión de tenant) y comprobar que breakers, DLQ, compensación y recovery se comportan como se espera.

## Ejecutar (monorepo)

```bash
# Capa L1 (LLM)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Varias capas
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# Suite amplia
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=ci-staging --duration=120
```

También vía scripts del producto:

```bash
pnpm benchmark:chaos
pnpm benchmark:chaos:full
```

## Capas

| Capa | Enfoque |
|------|---------|
| L1 | Fallos / latencia de LLM |
| L2 | Tools (timeout, error, poison) |
| L3 | Sistema (bus, checkpoint, memoria) |
| L4 | Aislamiento y cuotas multi-tenant |

## Relacionado

- [Resiliencia](/es/architecture/resilience)  
- [Benchmarks](/es/guide/benchmarks)  
- [Producción](/es/architecture/production-readiness)
