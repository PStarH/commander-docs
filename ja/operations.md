# Operations and rollback

> This page is synchronized from the canonical English documentation. 日本語 navigation is available; commands and product limits are identical in every locale.

## Health checks

Use the API health endpoints to distinguish process availability from readiness:

```bash
curl http://localhost:4000/health
curl http://localhost:4000/readyz
```

## Rollback

Treat configuration, provider credentials, and deployment images as a single
release unit. Before changing one, record the prior version and verify that it
can be restored. Stop a rollout when readiness fails or a consequential action
cannot be reconciled.

## Data recovery

Back up durable state before upgrades. Local file-backed state is not a
multi-replica authority. Recovery objectives depend on the storage topology and
operational drill; this site does not promise a universal RPO or RTO.

## Escalation

Keep an operator responsible for rollback, credential rotation, and customer
communications. For security incidents, use the private disclosure route in
`SECURITY.md`.