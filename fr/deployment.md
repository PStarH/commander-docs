# Déploiement

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Déploiement**.

## Entrée rapide

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000 · Dev GUI :5173 con pnpm gui
```

```bash
cp .env.example .env.production
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
