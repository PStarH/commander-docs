# Intelligence Layer

**Intelligence Layer.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Component | Purpose | User sees |
|-----------|---------|-----------|
| **Cost Predictor** | Estimates task cost before execution | "Estimated $0.09, continue?" |
| **Failure Pattern Learner** | Learns from past failures | "You've hit this issue before" |
| **Impact Analyzer** | Predicts change side effects | "Changing this affects 3 files" |
| **Skill Extractor** | Extracts reusable patterns from successes | "Solution saved for reuse" |


## 주요 섹션

### Components

**Components** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Cost Predictor

**Cost Predictor** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Failure Pattern Learner

**Failure Pattern Learner** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Impact Analyzer

**Impact Analyzer** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Skill Extractor

**Skill Extractor** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Configuration

**Configuration** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```typescript
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();

const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
  agentCount: 4,
});

console.log(`Estimated cost: $${estimate.estimatedCostUsd}`);
console.log(`Estimated duration: ${estimate.estimatedDurationMs}ms`);
console.log(`Confidence: ${estimate.confidence}`);
```
```
┌─────────────────────────────────┐
│         Total Estimate          │
├─────────────────────────────────┤
│  Deliberation:  $0.002         │
│  Execution:     $0.06          │
│  Synthesis:     $0.02          │
│  Quality Gates: $0.008         │
├─────────────────────────────────┤
│  Total:         $0.09          │
└─────────────────────────────────┘
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
