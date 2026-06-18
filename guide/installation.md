# Installation

## Prerequisites

- **Node.js** 18+ (LTS recommended)
- **pnpm** 8+ (`npm install -g pnpm`)
- One LLM provider API key (see [Providers](/guide/providers))

## Local Development

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

## Docker

Commander includes a 6-stage multi-architecture Docker build:

```bash
docker compose up -d
# API: http://localhost:4000
# Web GUI: http://localhost:3000
```

The Docker setup includes Nginx reverse proxy, health checks, persistent volumes, and tini init.

## Production (VM / VPS)

```bash
# 1. Configure environment
cp .env.example .env.production
# Edit .env.production with your API keys and settings

# 2. Deploy to any Linux VM with Docker
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production

# Or manually:
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

### Production Overlay

The production overlay (`docker-compose.prod.yml`) adds:

| Feature | Setting |
|---------|---------|
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web |
| Logging | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy | `always` (auto-restart) |
| Health checks | 30s interval, 10s timeout, 5 retries |
| Rate limiting | Configurable per-tenant window/max |
| Multi-tenancy | Optional `TENANT_PROVIDER=simple` |

## CI/CD

Commander's CI pipeline (`.github/workflows/ci.yml`) runs on every push/PR:

| Job | Checks |
|-----|--------|
| **quality** | TypeScript compilation, 330+ tests, CLI check, core build |
| **docker** | `docker compose build` |
| **web-gui** | Vite production build |

CD auto-deploys to production on main branch. Requires GitHub Secrets: `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`.

## Verify Installation

```bash
# Run the test suite (233+ tests, must be all green)
cd packages/core
npx tsx --test tests/*.test.ts

# Verify zero type errors
npx tsc --noEmit
```
