# Console web

Surface visuelle de Commander : chat streaming, topologie live, gouvernance et vues d’ops.

## Démarrage

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
pnpm gui
```

| Service | URL typique |
|---------|-------------|
| API | http://localhost:4000 |
| Web (Vite) | http://localhost:5173 |

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## Ce que vous obtenez

| Zone | Rôle |
|------|------|
| **Dashboard** | Rapport, tokens, topologie, roster |
| **Chat** | Runs conversationnels en stream |
| **Governance** | Approbations, politiques, audit |
| **DLQ** | File morte : inspecter et rejouer |
| **Security** | Posture conformité |
| **Execution** | Flux d’exécution, risque d’hallucination |
| **Agents** | Roster et arbre de lignée |

## Health checks

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics
```

Si `COMMANDER_API_KEY` est défini :

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

## Console vs CLI

| Console | CLI |
|---------|-----|
| Topologie visuelle, approbations | Scripts, CI, SSH seul |
| Debug de longs runs | `plan` / `run --stream` one-shot |
| Ops (DLQ, audit) | Automatisation |

Plus : [Dépannage](/fr/guide/troubleshooting) · [Déploiement](/fr/deployment).
