# カオステスト

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/usage/chaos-testing)



Commander includes a built-in chaos engineering framework that injects faults across 4 layers and verifies recovery. Use it to validate that your agent deployment can survive real-world failures.

## クイックスタート


```bash
# Run a single-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Run multi-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# With recovery verification (default)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```

## Chaos Layers


| Layer | Name | What it injects |
|-------|------|----------------|
| **L1** | LLM | Provider-level faults: rate limits, timeouts, context window overflow, malformed responses |
| **L2** | Tool | 10 failure modes: `http_5xx`, `http_4xx`, `disk_full`, `oom`, `process_crash`, `state_corrupt`, `dependency_unavailable`, `time_drift`, `auth_expired`, `http_timeout` |
| **L3** | System | Process/disk/CPU/memory faults: CPU throttle, memory pressure, disk full simulation |
| **L4** | Tenant | Multi-tenant blast radius enforcement: cross-tenant access attempts, resource exhaustion |

## Running Chaos Tests


### Single Layer


```bash
# LLM provider faults only
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1

# Tool failure injection
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L2

# System-level faults
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L3

# Tenant isolation testing (requires --tenant)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L4 --tenant=ci-staging
```

### Multi-Layer


```bash
# Full stack chaos
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=ci-staging --duration=120
```

### Options


| Flag | Default | Description |
|------|---------|-------------|
| `--layers` | required | Comma-separated layers: `L1`, `L2`, `L3`, `L4` |
| `--tenant` | — | Tenant ID (required for L4) |
| `--duration` | `30` | Test duration in seconds |
| `--fault-types` | all | Comma-separated fault types to inject |
| `--no-recovery` | false | Skip recovery verification |

## Recovery Verification


Every chaos run calls `RecoveryBootstrapper.bootstrap()` after fault injection. If recovery fails, the run is marked failed in the report.

The recovery verifier checks:
1. **Zombie detection** — No orphaned execution processes
2. **Checkpoint integrity** — SQLite WAL is consistent
3. **Circuit breaker state** — Breakers reset after fault window
4. **DLQ drain** — Dead letter queue is empty or draining
5. **Compensation completeness** — All in-progress mutations are resolved

## Adding New Scenarios


1. Add fault config to the appropriate layer module:
   - `packages/core/src/chaos/l1LlmLayer.ts`
   - `packages/core/src/chaos/l2ToolLayer.ts`
   - `packages/core/src/chaos/l3SystemLayer.ts`
   - `packages/core/src/chaos/l4TenantLayer.ts`

2. Write a test in `tests/chaos/`

3. Add to `ChaosOrchestrator.runLayer()` dispatcher

## Programmatic API


```typescript
import { ChaosOrchestrator } from '@commander/core';

const orchestrator = new ChaosOrchestrator({
  bootstrap: async () => { /* recovery bootstrap */ },
  delayMs: 1000,
});

const results = await orchestrator.run({
  layers: ['L1', 'L2'],
  tenantId: 'ci-staging',
  durationSec: 60,
  verifyRecovery: true,
});

for (const result of results) {
  console.log(`${result.layer}/${result.faultType}: ${result.recovery.status}`);
}
```

## CI Integration


Add chaos testing to your CI pipeline:

```yaml
# .github/workflows/chaos.yml
name: Chaos Tests
on:
  schedule:
    - cron: '0 2 * * 1'  # Weekly on Monday at 2am

jobs:
  chaos:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install
      - name: Run chaos tests
        run: |
          npx tsx packages/core/src/cli/commands/chaos.ts \
            --layers=L1,L2,L3 --tenant=ci-staging --duration=60
```
