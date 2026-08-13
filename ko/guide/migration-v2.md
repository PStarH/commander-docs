# 아키텍처 V2 마이그레이션

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/migration-v2)



Migrate from legacy V1 execution paths to the **Architecture V2** durable kernel: control plane schedules work; workers execute steps; state lives in PostgreSQL.

> Full operator detail lives in the monorepo: [`docs/v2-migration-guide.md`](https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md). This page is the docs-site summary.

## 멘탈 모델


| Plane | Responsibility |
|-------|----------------|
| **Gateway (control)** | Accept runs, schedule WorkGraphs, lifecycle (pause/resume/cancel) — **does not** execute agents in pure V2 |
| **Worker (execution)** | Claim steps, run agents/tools, report results |
| **Kernel storage** | PostgreSQL tables for runs, steps, events |

## Feature flags / env


| Variable | Default | Meaning |
|----------|---------|---------|
| `COMMANDER_V2_MODE` | `0` | `1` enables V2 (disables legacy routes) |
| `NODE_ENV=production` | — | Often forces V2 on |
| `COMMANDER_LEGACY_EXECUTION` | `0` | Temporary bridge to re-enable legacy routes |
| `DATABASE_URL` | — | **Required** for V2 kernel |
| `COMMANDER_WORKER_*` | see monorepo guide | Worker kind, concurrency, auth, tenants |

## 라우트 매핑


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

## 스토리지 마이그레이션


| Legacy | V2 |
|--------|-----|
| SQLite / pod-local files | PostgreSQL `commander_*` tables |
| In-memory chat maps | Event-sourced reconstruction |
| Old checkpoints | **Not** portable — re-submit runs |

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

## Worker sketch


```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# start worker process — see monorepo worker-plane package
```

## 롤아웃 전략


1. **Dual-run in staging** with `COMMANDER_LEGACY_EXECUTION=1` if needed  
2. Point a canary tenant at `POST /v1/runs`  
3. Disable legacy routes (`COMMANDER_V2_MODE=1`)  
4. Monitor `/v1/slo`, DLQ, worker lease health  

## When you can stay on V1-style local CLI


Local `cliEntry.ts` / SDK `CommanderClient` for single-machine development remains the fastest path. V2 matters when you need **durable multi-replica execution** and gateway/worker split.

## 관련


- [Deployment](/ko/deployment)  
- [Production readiness](/ko/architecture/production-readiness)  
- [Event sourcing](/ko/architecture/event-sourcing)  
- Monorepo guide: https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md  
