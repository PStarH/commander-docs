# Installation

## Prérequis

- **Node.js** 18+ (LTS recommandé)
- **pnpm** 8+ (`npm install -g pnpm`)
- Une clé API LLM (voir [Fournisseurs](/fr/guide/providers))

## Développement local

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### Console web (dev)

```bash
pnpm gui
# API :4000 + Web :5173
```

### CLI depuis les sources

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

Après build du core (`pnpm --filter @commander/core build`), le binaire `commander` est disponible.

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API : http://localhost:4000
# Web : http://localhost:3000
```

## Production (VM / VPS)

```bash
cp .env.example .env.production
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
# ou
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

### Overlay production

| Fonction | Réglage |
|----------|---------|
| Limites CPU/RAM | 2 CPU / 4GB API, 0.5 CPU / 256MB web |
| Logs | json-file, 10MB max, 3 rotations |
| Restart | `always` |
| Health checks | 30s / 10s / 5 retries |
| Rate limiting | configurable par tenant |
| Multi-tenant | optionnel `TENANT_PROVIDER=simple` |

## Vérifier

```bash
curl http://localhost:4000/health
cd packages/core && npx tsx --test tests/*.test.ts
```

## Suite

- [Démarrage rapide](/fr/guide/getting-started)
- [Commandes](/fr/guide/commands)
- [Déploiement](/fr/deployment)
