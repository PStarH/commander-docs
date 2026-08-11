# Commander V2 Documentation Design

## Scope

The English documentation is the source of truth for the V2 release. Existing
non-English trees remain in place for independent translation work and are not
changed by this update.

## Product boundary

Commander V2 is documented as a durable execution control plane. The Gateway
accepts authenticated, tenant-bound work and schedules it into the shared
PostgreSQL kernel. Workers claim leased steps and execute them. The Gateway
does not execute agents. Consequential tool and connector work goes through
the governed Action Gateway and Effect Broker, with idempotency, approval,
lease fencing, reconciliation, and signed evidence.

The documentation must distinguish shipped behavior from experimental harnesses,
pilot thresholds, and legacy local execution. It must not present SQLite,
automatic topology selection, self-evolution, provider counts, benchmark
fixtures, or production SLOs as the V2 product contract unless the source
implementation explicitly supports that claim.

## Information architecture

- Guide: install the monorepo, run the API and worker planes, configure V2,
  submit durable runs, and migrate from legacy routes.
- Architecture: Gateway/kernel/worker boundaries, leases and fencing, effects,
  evidence, tenant isolation, recovery, and observability.
- API: the canonical `/v1` resources, Action Gateway lifecycle, health, and
  OpenAPI discovery.
- Deployment: Docker Compose and Helm topology, PostgreSQL requirements,
  secrets, probes, backups, and rollout boundaries.

Old pages that describe obsolete product promises are removed from the English
navigation. Their translated counterparts remain available until translation
agents replace them.

## Verification

The docs repository must pass `npm run check` and `npm run build`. Checks must
also guard V2 terminology and the monorepo-first installation path.
