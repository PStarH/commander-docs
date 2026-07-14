# Déploiement

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

Production : `./scripts/deploy-vm.sh` ou overlay `docker-compose.prod.yml`.

```bash
curl http://localhost:4000/health
```
