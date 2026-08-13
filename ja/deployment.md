# デプロイ

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/deployment)



Commander supports multiple deployment options for different environments.

## Local (Docker Compose)


```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:     http://localhost:4000
# Web GUI: http://localhost:3000   (Docker / Nginx)
# Dev GUI: http://localhost:5173   (pnpm gui, no Docker)
```

The Docker setup features:
- 6-stage multi-architecture build
- Nginx reverse proxy (2 workers, 100 connections)
- Health checks (30s interval, 10s timeout, 3 retries)
- Persistent volumes for trace store and samples
- tini init for proper signal handling

## Production (VM / VPS)


### 前提条件


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

## Observability Stack


Commander includes a pre-configured observability stack for production monitoring:

```bash
# Start the full observability stack
docker compose -f deploy/observability/docker-compose.yml up -d
```

### Components


| Component | Version | Purpose |
|-----------|---------|---------|
| Prometheus | v2.51.0 | Metrics scraping (10s interval, 30-day retention) |
| Grafana | 10.4.0 | Dashboards (admin/admin, auto-provisioned) |
| Jaeger | 1.55 | Distributed tracing (optional, `--profile tracing`) |

### Grafana Dashboards


Two pre-configured dashboards are auto-provisioned:

**Developer View** (default home):
- Run success rate (threshold: 0.8 warn / 0.95 green)
- P95 latency (5s warn / 10s red)
- Token cost USD/hour ($1 warn / $10 red)
- Active run count
- Token usage trends, tool call success rate, cost by component

**Mechanistic View** (Ops perspective):
- EventSourcing WAL write latency p95 (50ms warn / 200ms red)
- WAL file size MB (100MB warn / 500MB red)
- DLQ backlog (10 warn / 50 red)
- Circuit breaker open state
- Event backlog ratio trends (1000 warn / 10000 red)
- SQLite busy lock contention error rate
- Compensation execution rate (success/failure)
- Audit event rate
- Checkpoint success rate

### Prometheus Configuration


Prometheus scrapes two jobs:
- `commander` — `host.docker.internal:3000/metrics` (application metrics)
- `commander-process` — `host.docker.internal:9091` (process metrics)

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
