# 슈퍼비전 트리

Commander는 **Erlang/OTP 스타일 슈퍼비전 트리**로 장애를 격리합니다. 모든 오류를 에이전트 안에서 잡기보다, 에이전트가 크래시하면 슈퍼바이저가 자동 재시작합니다 — “Let It Crash”.

## 왜 슈퍼비전 트리인가

전통적 에러 핸들링은 모든 실패를 catch하려 해 코드가 취약해집니다. 슈퍼비전 트리는 모델을 뒤집습니다.

- **장애 격리** — 한 에이전트 크래시가 시스템을 죽이지 않음  
- **자동 복구** — 사람 없이 재시작  
- **에스컬레이션** — 자식이 계속 죽으면 부모로 상승  
- **우아한 종료** — 시작 역순으로 자식 종료  

## 구조

```
                    ┌──────────────────┐
                    │  Root Supervisor │
                    │  (one_for_one)   │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        Agent 1         Agent 2         Agent N
```

## 재시작 전략

| 전략 | 동작 | 언제 |
|------|------|------|
| `one_for_one` | 죽은 자식만 재시작 | 자식이 독립적 |
| `one_for_all` | 모든 자식 재시작 | 상호 의존 |
| `rest_for_one` | 죽은 자식 + 그 이후 시작분 | 시작 순서 의존 |

## 설정

```typescript
import { Supervisor } from '@commander/core';

const supervisor = new Supervisor({
  id: 'agent-pool',
  strategy: 'one_for_one',
  maxRestarts: 10,
  maxRestartIntervalMs: 60000,
  defaultShutdownMs: 5000,
  publishEvents: true,
});
```

## 자식 추가

```typescript
const handle = await supervisor.startChild({
  id: 'agent-1',
  start: async () => {
    const runtime = await createAgentRuntime({ /* config */ });
    return runtime;
  },
});
```

재시작 한도를 넘기면 슈퍼바이저가 부모로 에스컬레이션하거나 풀을 중단합니다. MessageBus로 이벤트를 발행할 수 있습니다.

## 관련

- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [Resilience](/ko/architecture/resilience)  
- [멀티 에이전트](/ko/architecture/multi-agent)  
