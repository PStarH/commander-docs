# Watch Mode (SSE Streaming)

**Watch Mode (SSE Streaming).** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Event Type | Description |
|------------|-------------|
| `task.start` | Task started |
| `deliberation` | Complexity analysis |
| `topology.select` | Topology selected |
| `agent.spawn` | Agent created |
| `tool.call` | Tool execution started |
| `tool.result` | Tool execution completed |
| `subtask.complete` | Subtask finished |
| `verification` | Quality gate check |
| `checkpoint` | State checkpoint saved |
| `task.complete` | Task finished |
| `task.error` | Error occurred |


## 주요 내용

### 사용법

운영 시 **Usage** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/watch-mode)를 보세요.

### Streamed Events

운영 시 **Streamed Events** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/watch-mode)를 보세요.

### Event Format

운영 시 **Event Format** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/watch-mode)를 보세요.

### Consuming Events

운영 시 **Consuming Events** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/watch-mode)를 보세요.

### Use Cases

운영 시 **Use Cases** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/watch-mode)를 보세요.

## 예제 (코드는 영어 유지)

```bash
# From monorepo source (or: commander watch "...")
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

```json
{
  "type": "tool.call",
  "data": {
    "tool": "grep",
    "args": { "pattern": "deprecated", "path": "./src" },
    "agentId": "agent-3",
    "timestamp": "2026-05-23T10:30:00Z"
  }
}
```

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
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
