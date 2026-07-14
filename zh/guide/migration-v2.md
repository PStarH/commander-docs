# 架构 V2 迁移

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/guide/migration-v2)



Migrate from legacy V1 execution paths to the **Architecture V2** durable kernel: control plane schedules work; workers execute steps; state lives in PostgreSQL.

> Full operator detail lives in the monorepo: [`docs/v2-migration-guide.md`](https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md). This page is the docs-site summary.

## 心智模型


| Plane | Responsibility |
|-------|----------------|
| **Gateway (control)** | Accept runs, schedule WorkGraphs, lifecycle (pause/resume/cancel) — **does not** execute agents in pure V2 |
| **Worker (execution)** | Claim steps, run agents/tools, report results |
| **Kernel storage** | PostgreSQL tables for runs, steps, events |

## 特性开关 / 环境变量


| Variable | Default | Meaning |
|----------|---------|---------|
| `COMMANDER_V2_MODE` | `0` | `1` enables V2 (disables legacy routes) |
| `NODE_ENV=production` | — | Often forces V2 on |
| `COMMANDER_LEGACY_EXECUTION` | `0` | Temporary bridge to re-enable legacy routes |
| `DATABASE_URL` | — | **Required** for V2 kernel |
| `COMMANDER_WORKER_*` | see monorepo guide | Worker kind, concurrency, auth, tenants |

## 路由映射


| Legacy | V2 |
|--------|-----|
| `POST /api/runtime/execute` | `POST /v1/runs` |
| `POST /api/orchestrator/execute` | `POST /v1/runs` (multi-step graph) |
| `POST /api/chat` | `POST /v1/runs` (single agent step) |
| `POST /api/pause/:runId` | `POST /v1/runs/:id/pause` |
| `POST /api/resume/:runId` | `POST /v1/runs/:id/resume` |
| `POST /api/cancel/:runId` | `POST /v1/runs/:id/cancel` |

### Core V2 endpoints


- `POST /v1/runs` · `GET /v1/runs/:id` · `GET /v1/runs/:id/steps` · `GET /v1/runs/:id/events`  
- Lifecycle: pause / resume / cancel  
- Interactions: human-in-the-loop  
- `/health` · `/metrics` · `/v1/slo`  

## 存储迁移


| Legacy | V2 |
|--------|-----|
| SQLite / pod-local files | PostgreSQL `commander_*` tables |
| In-memory chat maps | Event-sourced reconstruction |
| Old checkpoints | **Not** portable — re-submit runs |

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

## Worker 示意


```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# start worker process — see monorepo worker-plane package
```

## 发布策略


1. **Dual-run in staging** with `COMMANDER_LEGACY_EXECUTION=1` if needed  
2. Point a canary tenant at `POST /v1/runs`  
3. Disable legacy routes (`COMMANDER_V2_MODE=1`)  
4. Monitor `/v1/slo`, DLQ, worker lease health  

## When you can stay on V1-style local CLI


Local `cliEntry.ts` / SDK `CommanderClient` for single-machine development remains the fastest path. V2 matters when you need **durable multi-replica execution** and gateway/worker split.

## 相关


- [Deployment](/zh/deployment)  
- [Production readiness](/zh/architecture/production-readiness)  
- [Event sourcing](/zh/architecture/event-sourcing)  
- Monorepo guide: https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md  
