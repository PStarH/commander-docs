# 인텔리전스 계층

인텔리전스 계층은 Commander를 시간이 갈수록 똑똑하게 만드는 **내부 자동 시스템**입니다. 사용자는 메커니즘이 아니라 결과만 봅니다.

## 구성 요소

| 구성 요소 | 역할 | 사용자가 보는 것 |
|-----------|------|------------------|
| **Cost Predictor** | 실행 전 비용 추정 | “약 $0.09, 계속할까요?” |
| **Failure Pattern Learner** | 과거 실패 학습 | “이 이슈를 전에 겪은 적 있습니다” |
| **Impact Analyzer** | 변경 부작용 예측 | “이 변경은 3개 파일에 영향” |
| **Skill Extractor** | 성공 패턴 추출 | “재사용용 솔루션 저장됨” |

## Cost Predictor

MetaLearner·심의 추정치로 실행 전 비용을 예측합니다.

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

분해 예: Deliberation · Execution · Synthesis · Quality Gates → 합계.

## Failure Pattern Learner

반복 실수를 경고합니다.

```typescript
import { getFailurePatternLearner } from '@commander/core';

const learner = getFailurePatternLearner();
const warnings = learner.checkPatterns({
  task: 'deploy to production',
  context: 'after database migration',
});

for (const warning of warnings) {
  console.log(`[${warning.severity}] ${warning.suggestion}`);
}
```

## Impact Analyzer · Skill Extractor

- 변경 범위·의존 파일을 추정해 위험 토폴로지(REVIEW) 권장에 반영  
- 성공 실행에서 재사용 스킬/패턴을 추출해 이후 심의에 주입  

## 사용자가 할 일

대부분 자동입니다. 비용을 엄격히 통제하려면 토큰 예산·승인 모드(`plan` / `suggest`)를 쓰세요.

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the auth module"
```

## 관련

- [Self-evolution](/ko/architecture/self-evolution)  
- [Token budget allocator](/ko/api/token-budget-allocator)  
- [Reflection engine](/ko/api/reflection-engine)  
