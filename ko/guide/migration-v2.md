# Architecture V2 Migration

Migrate from legacy V1 execution paths to the **Architecture V2** durable kernel: control plane schedules work; workers execute steps; state lives in PostgreSQL. - `POST /v1/runs` · `GET /v1/runs/:id` · `GET /v1/runs/:id/steps` · `GET /v1/runs/:id/events`

이 문서는 Commander에서 **Architecture V2 Migration** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
