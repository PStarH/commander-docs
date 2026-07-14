# Architecture V2 Migration

**Architecture V2 Migration.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Plane | Responsibility |
|-------|----------------|
| **Gateway (control)** | Accept runs, schedule WorkGraphs, lifecycle (pause/resume/cancel) — **does not** execute agents in pure V2 |
| **Worker (execution)** | Claim steps, run agents/tools, report results |
| **Kernel storage** | PostgreSQL tables for runs, steps, events |


## 주요 내용

### Mental model

운영 시 **Mental model** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### Feature flags / env

운영 시 **Feature flags / env** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### Route mapping

운영 시 **Route mapping** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### Storage migration

운영 시 **Storage migration** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### Worker sketch

운영 시 **Worker sketch** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### Rollout strategy

운영 시 **Rollout strategy** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### When you can stay on V1-style local CLI

운영 시 **When you can stay on V1-style local CLI** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

### 관련

운영 시 **Related** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/migration-v2)를 보세요.

## 예제 (코드는 영어 유지)

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# start worker process — see monorepo worker-plane package
```

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
