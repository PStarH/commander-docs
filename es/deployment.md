# Despliegue

## Docker local

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000 · Dev GUI :5173 con pnpm gui
```

## Producción

```bash
cp .env.example .env.production
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

## Health

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics
```

[Instalación](/es/guide/installation) · [Migración V2](/es/guide/migration-v2)
