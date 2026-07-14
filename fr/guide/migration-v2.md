# Migration Architecture V2

Le **control plane** planifie ; les **workers** exécutent ; l’état vit dans **PostgreSQL**.

## Variables

| Variable | Rôle |
|----------|------|
| `COMMANDER_V2_MODE=1` | Active V2 |
| `DATABASE_URL` | Requis |
| `COMMANDER_LEGACY_EXECUTION` | Pont temporaire |
| `COMMANDER_WORKER_*` | kind, auth, concurrency |

## Routes

| Legacy | V2 |
|--------|-----|
| `POST /api/runtime/execute` | `POST /v1/runs` |
| pause/resume/cancel legacy | `/v1/runs/:id/...` |

## Rollout

1. Staging avec pont legacy si besoin  
2. Canary sur `/v1/runs`  
3. Couper le legacy  
4. Monitorer `/v1/slo`, DLQ, leases  

La CLI locale reste le plus rapide en dev. V2 compte pour l’exécution durable multi-réplicas.

Monorepo : `docs/v2-migration-guide.md`.

[Déploiement](/fr/deployment) · [Event sourcing](/fr/architecture/event-sourcing)
