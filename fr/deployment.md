# Déploiement

## Docker local

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000 · Dev GUI :5173 avec pnpm gui
```

Build multi-stage, Nginx, health checks, volumes, tini.

## Production (VM)

```bash
cp .env.example .env.production
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
# ou
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

### Overlay prod

| Fonction | Réglage |
|----------|---------|
| CPU/RAM | 2 CPU / 4GB API |
| Logs | json-file, 10MB, 3 rotations |
| Restart | `always` |
| Health | 30s / 10s / 5 retries |
| Multi-tenant | `TENANT_PROVIDER=simple` optionnel |

## Health

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Lié

- [Installation](/fr/guide/installation)  
- [Migration V2](/fr/guide/migration-v2)  
- [Prêt production](/fr/architecture/production-readiness)
