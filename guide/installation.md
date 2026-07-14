# Installation

::: tip Monorepo first
Commander ships as an open-source **monorepo**. Today the supported install path is **clone + pnpm**. Public npm packages (`@commander/core`, `@commander/sdk`) are **not** the primary path yet — treat `pnpm add @commander/*` as upcoming, not the quick-start success path.
:::

## Prerequisites

- **Node.js** 18+ (LTS recommended)
- **pnpm** 8+ (`npm install -g pnpm`)
- One LLM provider API key (see [Providers](/guide/providers))

> Use **pnpm**, not npm alone — multi-package workspaces.

## Local development (recommended)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### Web Console (dev)

```bash
# API :4000 + Web :5173 + open browser
pnpm gui
```

### CLI from source (works without a global binary)

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

After building core (`pnpm --filter @commander/core build`), the `commander` binary is available from the package workspace (PATH depends on your shell / pnpm bin setup).

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:      http://localhost:4000
# Web GUI:  http://localhost:3000
```

The Docker setup includes multi-stage multi-architecture build, Nginx reverse proxy, health checks, persistent volumes, and tini init.

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

### Production overlay

The production overlay (`docker-compose.prod.yml`) adds:

| Feature           | Setting                                     |
| ----------------- | ------------------------------------------- |
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web        |
| Logging           | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy    | `always` (auto-restart)                     |
| Health checks     | 30s interval, 10s timeout, 5 retries        |
| Rate limiting     | Configurable per-tenant window/max          |
| Multi-tenancy     | Optional `TENANT_PROVIDER=simple`           |

## CI/CD

Commander's CI pipeline (`.github/workflows/ci.yml`) runs on every push/PR:

| Job         | Checks                                                     |
| ----------- | ---------------------------------------------------------- |
| **quality** | TypeScript compilation, 6700+ tests, CLI check, core build |
| **docker**  | `docker compose build`                                     |
| **web-gui** | Vite production build                                      |

CD deploys on the main product branch. Requires GitHub Secrets: `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`.

## Verify installation

```bash
# Health (when API is running)
curl http://localhost:4000/health

# Test suite from monorepo root (or packages/core)
cd packages/core
npx tsx --test tests/*.test.ts

# Typecheck
npx tsc --noEmit
```

## Next

- [Quick Start](/guide/getting-started)
- [Commands](/guide/commands)
- [Deployment](/deployment)
