# Migración Architecture V2

Pasa de paths legacy V1 al kernel durable V2: el **control plane** programa; los **workers** ejecutan; el estado vive en **PostgreSQL**.

## Modelo mental

| Plano | Responsabilidad |
|-------|-----------------|
| Gateway | Acepta runs, WorkGraphs, pause/resume/cancel — no ejecuta agentes en V2 puro |
| Worker | Reclama steps, ejecuta, reporta |
| Kernel | Tablas `commander_*` en Postgres |

## Env clave

| Variable | Default | Significado |
|----------|---------|-------------|
| `COMMANDER_V2_MODE` | `0` | `1` activa V2 |
| `DATABASE_URL` | — | **Requerido** en V2 |
| `COMMANDER_LEGACY_EXECUTION` | `0` | Puente temporal |
| `COMMANDER_WORKER_*` | — | kind, auth, concurrency, tenants |

## Rutas

| Legacy | V2 |
|--------|-----|
| `POST /api/runtime/execute` | `POST /v1/runs` |
| `POST /api/chat` | `POST /v1/runs` (step agente) |
| pause/resume/cancel legacy | `/v1/runs/:id/pause|resume|cancel` |

## Rollout

1. Staging con puente legacy si hace falta  
2. Canary a `/v1/runs`  
3. `COMMANDER_V2_MODE=1`  
4. Monitorizar `/v1/slo`, DLQ, leases  

La CLI/SDK local monomáquina sigue siendo el camino más rápido para dev. V2 importa con **ejecución durable multi-réplica**.

Guía completa monorepo: `docs/v2-migration-guide.md`.

## Relacionado

- [Despliegue](/es/deployment)  
- [Event sourcing](/es/architecture/event-sourcing)  
- [Producción](/es/architecture/production-readiness)
