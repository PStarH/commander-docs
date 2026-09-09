# Deployment

> This page is synchronized from the canonical English documentation. Español navigation is available; commands and product limits are identical in every locale.

## Supported local deployment

Copy the environment template, set an API key and one provider key, then start
the local stack:

```bash
cp .env.example .env
# Set COMMANDER_API_KEY and a provider API key in .env.
docker compose up
```

The API listens on `http://localhost:4000` and the web interface on
`http://localhost:3000`. Grafana, when the observability profile is enabled,
uses port `3001`; it is not the Commander API.

Check the API after startup:

```bash
curl http://localhost:4000/health
curl http://localhost:4000/readyz
```

## Enterprise Gateway boundary

The `/v1` Gateway needs a PostgreSQL DSN and is alpha. Do not present it as a
complete production multi-tenant SaaS or rely on it for strict tenant-isolation
requirements without your own validation and controls.

## Production prerequisites

- Terminate TLS and set explicit CORS origins.
- Generate a strong `COMMANDER_API_KEY` and store provider credentials outside
  source control.
- Change default observability credentials before exposing any dashboard.
- Back up durable state and rehearse recovery before relying on it.

See [Operations and rollback](/operations) for recovery and rollback limits.