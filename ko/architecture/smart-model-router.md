# Smart Model Router

**Smart Model Router.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Capability | Description |
|------------|-------------|
| `code` | Code generation and understanding |
| `reasoning` | Logical reasoning and chain-of-thought |
| `analysis` | Data analysis and interpretation |
| `creative` | Creative writing and brainstorming |
| `math` | Mathematical computation |
| `multimodal` | Multiple input modalities |
| `vision` | Image understanding |
| `image_generation` | Image creation |
| `long_context` | Large context window support |
| `low_cost` | Cost-efficient inference |
| `fast` | Low-latency inference |
| `high_quality` | Highest quality output |
| `function_calling` | Tool use support |
| `json_mode` | Structured JSON output |
| `streaming` | Streaming response support |
| `translation` | Multi-language translation |
| `summarization` | Text summarization |
| `extraction` | Information extraction |


## 주요 섹션

### Capabilities

**Capabilities** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Configuration

**Configuration** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Routing Modes

**Routing Modes** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Model Tiers

**Model Tiers** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Routing Decision

**Routing Decision** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Programmatic API

**Programmatic API** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Integration with Deliberation

**Integration with Deliberation** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```typescript
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
      capabilities: ['code', 'reasoning', 'function_calling', 'streaming'],
      costPer1MInput: 2.5,
      costPer1MOutput: 10,
      contextWindow: 128000,
      tier: 'power',
    },
    {
      id: 'claude-sonnet-4-20250514',
      provider: 'anthropic',
      capabilities: ['code', 'reasoning', 'long_context', 'function_calling'],
      costPer1MInput: 3,
      costPer1MOutput: 15,
      contextWindow: 200000,
      tier: 'power',
    },
    {
      id: 'deepseek-chat',
      provider: 'deepseek',
      capabilities: ['code', 'reasoning', 'low_cost'],
      costPer1MInput: 0.14,
      costPer1MOutput: 0.28,
      contextWindow: 64000,
      tier: 'eco',
    },
  ],
  routingRules: [
    {
      taskType: 'code_review',
      requiredCapabilities: ['code', 'reasoning'],
      preferredTier: 'power',
      maxCostPer1K: 0.05,
    },
    {
      taskType: 'simple_query',
      requiredCapabilities: ['reasoning'],
      preferredTier: 'eco',
      maxCostPer1K: 0.001,
    },
  ],
  budget: {
    maxCostPerTask: 1.0,
    dailyBudget: 10.0,
  },
});
```
```
Task → Analyze requirements → Match capabilities → Filter by budget
                                                         │
                    ┌────────────────────────────────────┘
                    ▼
            Select model by tier preference
                    │
                    ┌────────────────────────────────────┐
                    ▼                                    ▼
            Primary model                          Fallback chain
            (best match)                           (next tier)
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
