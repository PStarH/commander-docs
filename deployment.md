# Deployment

Commander supports multiple deployment options for different environments.

## Local (Docker Compose)

```bash
docker compose up -d
# API: http://localhost:4000
# Web GUI: http://localhost:3000
```

The Docker setup features:
- 6-stage multi-architecture build
- Nginx reverse proxy (2 workers, 100 connections)
- Health checks (30s interval, 10s timeout, 3 retries)
- Persistent volumes for trace store and samples
- tini init for proper signal handling

## Production (VM / VPS)

### Prerequisites

- Linux VM with Docker and Docker Compose
- SSH access with key authentication
- A domain name pointing to the VM (optional)

### One-Click Deploy

```bash
# 1. Configure environment
cp .env.example .env.production
# Edit .env.production with your API keys and settings

# 2. Deploy to any Linux VM with Docker
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
```

### Manual Deploy

```bash
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
| Multi-tenancy | Optional `TENANT_PROVIDER=simple` with static config |

### CI/CD

```yaml
# .github/workflows/cd.yml — Auto-deploy to production on main branch
name: CD
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to production
        run: |
          echo "${{ secrets.DEPLOY_KEY }}" > deploy_key
          chmod 600 deploy_key
          ssh -i deploy_key ${{ secrets.DEPLOY_USER }}@${{ secrets.DEPLOY_HOST }} \
            "cd /opt/commander && git pull && docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build"
```

Requires GitHub Secrets: `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`.

## Configuration Reference

See `.env.example` for all configurable options:

```bash
# LLM Provider (set at least one)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Server
PORT=4000
HOST=0.0.0.0
CORS_ORIGIN=*

# Rate Limiting
RATE_LIMIT_WINDOW_MS=60000
RATE_LIMIT_MAX=100

# Multi-Tenancy
TENANT_PROVIDER=null      # null | simple
# TENANT_PROVIDER_CONFIG={"tenant-1":{"tokenBudget":100000,"maxConcurrency":5}}
```
