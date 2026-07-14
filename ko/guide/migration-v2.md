# Architecture V2 마이그레이션

레거시 V1 실행 경로에서 **Architecture V2** 내구성 커널로 이전합니다. 컨트롤 플레인이 작업을 스케줄하고, 워커가 스텝을 실행하며, 상태는 PostgreSQL에 둡니다.

> 운영 상세는 monorepo [`docs/v2-migration-guide.md`](https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md). 이 페이지는 docs 사이트 요약입니다.

## 멘탈 모델

| 플레인             | 책임                                                                                                |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| **Gateway (제어)** | run 수락, WorkGraph 스케줄, lifecycle (pause/resume/cancel). 순수 V2에서는 에이전트를 실행하지 않음 |
| **Worker (실행)**  | 스텝 claim, 에이전트/도구 실행, 결과 보고                                                           |
| **Kernel storage** | runs / steps / events PostgreSQL 테이블                                                             |

## 기능 플래그 / 환경 변수

| 변수                         | 기본          | 의미                              |
| ---------------------------- | ------------- | --------------------------------- |
| `COMMANDER_V2_MODE`          | `0`           | `1`이면 V2 (레거시 라우트 비활성) |
| `NODE_ENV=production`        | —             | 종종 V2 강제                      |
| `COMMANDER_LEGACY_EXECUTION` | `0`           | 임시로 레거시 재활성              |
| `DATABASE_URL`               | —             | V2 커널에 **필수**                |
| `COMMANDER_WORKER_*`         | monorepo 참조 | worker 종류·동시성·인증·테넌트    |

## 라우트 매핑

| Legacy                           | V2                                   |
| -------------------------------- | ------------------------------------ |
| `POST /api/runtime/execute`      | `POST /v1/runs`                      |
| `POST /api/orchestrator/execute` | `POST /v1/runs` (다단계 그래프)      |
| `POST /api/chat`                 | `POST /v1/runs` (단일 에이전트)      |
| pause / resume / cancel          | `/v1/runs/:id/{pause,resume,cancel}` |

### 핵심 V2 엔드포인트

- `POST /v1/runs` · `GET /v1/runs/:id` · steps · events
- lifecycle · human-in-the-loop
- `/health` · `/metrics` · `/v1/slo`

## 스토리지 마이그레이션

| Legacy            | V2                         |
| ----------------- | -------------------------- |
| SQLite / pod 로컬 | PostgreSQL `commander_*`   |
| 인메모리 chat     | 이벤트 소싱 재구성         |
| 구 체크포인트     | **이식 불가** — run 재제출 |

```bash
# DATABASE_URL 설정 후
pnpm db:migrate   # monorepo product scripts
```

## Worker 스케치

```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# monorepo worker-plane 패키지로 기동
```

## 롤아웃

1. 스테이징 dual-run (`COMMANDER_LEGACY_EXECUTION=1` 필요 시)
2. 카나리 테넌트를 `POST /v1/runs`로
3. 레거시 비활성 (`COMMANDER_V2_MODE=1`)
4. `/v1/slo` · DLQ · worker lease 모니터링

## 언제 V1 스타일 로컬 CLI를 유지하나

단일 머신 개발의 `cliEntry.ts` / SDK `CommanderClient`는 여전히 가장 빠릅니다. V2는 **내구성 멀티 레플리카 실행**과 gateway/worker 분리가 필요할 때입니다.

## 관련

- [배포](/ko/deployment)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [이벤트 소싱](/ko/architecture/event-sourcing)
