# Plugin System

**Plugin System.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentStart` | Agent begins work |
| `onAgentComplete` | Agent finishes work |
| `onSubtaskCreate` | New subtask created |
| `onSubtaskComplete` | Subtask finished |
| `onCheckpoint` | State checkpoint saved |
| `onError` | Error occurred (non-fatal) |
| `onRetry` | Retry attempt starting |
| `beforeVerification` | Before quality gate check |
| `afterVerification` | After quality gate check |
| `onTokenUsage` | Token budget updated |
| `onMetricsEmit` | Metrics collected |
| `beforeRun` | Execution run starts |
| `afterRun` | Execution run completes |
| `onHandoff` | Agent-to-agent handoff |
| `onStreamEvent` | SSE event emitted |


## 주요 섹션

### Hook Points

**Hook Points** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Creating a Plugin

**Creating a Plugin** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Registering a Plugin

**Registering a Plugin** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Plugin Security

**Plugin Security** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Use Cases

**Use Cases** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```typescript
import { CommanderPlugin } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';

  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] Calling ${params.provider} with ${params.messages.length} messages`);
      return params; // Return modified params, or throw to block
    },

    afterToolCall: async (result) => {
      console.log(`[Tool] ${result.tool} completed in ${result.durationMs}ms`);
      return result; // Return modified result, or throw to block
    },

    onError: async (error) => {
      console.error(`[Error] ${error.message}`);
      // Don't return — errors are fire-and-forget
    },

    onMetricsEmit: async (metrics) => {
      // Forward metrics to external monitoring
      await fetch('https://monitor.example.com/metrics', {
        method: 'POST',
        body: JSON.stringify(metrics),
      });
    },
  };
}
```
```typescript
import { getHookManager } from '@commander/core';

const hookManager = getHookManager();
hookManager.register(new LoggingPlugin());
```

## 운영 체크

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
