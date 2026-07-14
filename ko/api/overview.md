# API 레퍼런스

Commander API는 **두 계층**입니다. 대부분의 앱은 Layer 1만 필요합니다.

## Layer 1 — 공개 통합 (여기서 시작)

| 표면 | 패키지 / 엔트리 | 용도 |
|------|-----------------|------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | 터미널, 스크립트, CI |
| **TypeScript SDK** | `@commander/sdk` → `CommanderClient` | Node 앱 임베드 |
| **HTTP API** | 서버 `:4000` | 다언어 클라이언트, Web Console |
| **Python SDK** | `commander-ai` (HTTP 클라이언트) | API 서버 대상 Python |

### TypeScript SDK

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

const c = await createClient();
await c.run('explain the architecture');
await c.disconnect();
```

| 메서드 | 역할 |
|--------|------|
| `connect` / `disconnect` | 수명주기 |
| `run(task)` | 전체 실행 → `ExecutionResult` |
| `plan(task)` | 심의만 |
| `onEvent(handler)` | 에이전트/도구 이벤트 스트림 |
| `createAgent` / memory helpers | 고급 세션 |

> **npm 상태:** monorepo 우선. 공개 npm은 진행 중. [Agent SDK](/ko/guide/sdk).

### HTTP

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

Architecture V2: `POST /v1/runs` — [V2 마이그레이션](/ko/guide/migration-v2).

### Python

```python
from commander import CommanderClient
# thin httpx client → API server
```

[Python SDK](/ko/guide/sdk-python).

---

## Layer 2 — 런타임 오케스트레이션 컴포넌트

`@commander/core` 내부 모듈. **런타임을 확장**할 때만 사용하세요.

| 컴포넌트 | 목적 |
|----------|------|
| [Task Complexity Analyzer](/ko/api/task-complexity-analyzer) | 점수 → 토폴로지 추천 |
| [Adaptive Orchestrator](/ko/api/adaptive-orchestrator) | 멀티 에이전트 계획 |
| [Token Budget Allocator](/ko/api/token-budget-allocator) | 예산 분배 |
| [Three-Layer Memory](/ko/api/three-layer-memory) | working · episodic · long-term |
| [Reflection Engine](/ko/api/reflection-engine) | 사후 평가 |
| [Consensus Checker](/ko/api/consensus-checker) | 고위험 다중 모델 투표 |
| [Inspector Agent](/ko/api/inspector-agent) | 헬스 / 이슈 탐지 |

### Layer 2를 쓸 때

- 커스텀 토폴로지·플래너  
- 메모리·합의 연구/계측  
- 서브시스템 단위 테스트  

### 쓰지 말 때

- “이 작업 실행”만 필요 → `CommanderClient`  
- 원격 다언어 → HTTP  

### 최소 예

```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
} from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

const allocator = new TokenBudgetAllocator({ baseBudget: 100_000 });
const budget = allocator.allocate(
  complexity.recommendedTopology,
  complexity.score,
  3,
);

const orchestrator = new AdaptiveOrchestrator();
orchestrator.registerAgent({
  id: 'lead',
  name: 'Lead',
  role: 'architect',
  capabilities: [],
});

const plan = orchestrator.createPlan(
  [{ id: 'task-1', description: '...', complexity: complexity.score }],
  complexity.recommendedTopology,
);
```

### 전역 접근자

`getGlobalTaskComplexityAnalyzer()` 등 프로세스 싱글톤이 있습니다. 공유 상태가 필요할 때만 쓰고, 기본은 `CommanderClient`를 선호하세요.

## 관련

- [CLI 명령](/ko/guide/commands)  
- [Web Console](/ko/guide/web-console)  
- [Cookbook](/ko/guide/cookbook/)  
- [아키텍처 개요](/ko/architecture/overview)  
