# Despliegue

Documentación en español de **Despliegue**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:     http://localhost:4000
# Web GUI: http://localhost:3000   (Docker / Nginx)
# Dev GUI: http://localhost:5173   (pnpm gui, no Docker)
```

```bash
# 1. Configure environment
cp .env.example .env.production
# Edit .env.production with your API keys and settings

# 2. Deploy to any Linux VM with Docker
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
```

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

| Feature | Setting |
|---------|---------|
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web |
| Logging | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy | `always` (auto-restart) |
| Health checks | 30s interval, 10s timeout, 5 retries |
| Rate limiting | Configurable per-tenant window/max |
| Multi-tenancy | Optional `TENANT_PROVIDER=simple` with static config |


| Component | Version | Purpose |
|-----------|---------|---------|
| Prometheus | v2.51.0 | Metrics scraping (10s interval, 30-day retention) |
| Grafana | 10.4.0 | Dashboards (admin/admin, auto-provisioned) |
| Jaeger | 1.55 | Distributed tracing (optional, `--profile tracing`) |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
