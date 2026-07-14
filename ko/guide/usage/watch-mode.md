# Watch Mode (SSE Streaming)

Watch mode provides real-time streaming of every execution event via Server-Sent Events (SSE). This is ideal for monitoring long-running tasks, debugging agent behavior, or integrating with custom UIs. Every event in the execution pipeline is streamed:

이 문서는 Commander에서 **Watch Mode (SSE Streaming)** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
# From monorepo source (or: commander watch "...")
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
