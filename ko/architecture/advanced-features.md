# 고급 엔진 기능

Commander는 정교한 실행 제어를 위한 여러 고급 엔진 컴포넌트를 포함합니다.

## Speculative Executor

여러 실행 경로를 병렬로 돌리고 최선 결과를 고릅니다.

```typescript
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
    { provider: 'openai', temperature: 0.5 },
    { provider: 'anthropic', temperature: 0.7 },
  ],
  selector: 'quality',
});
```

## Entropy Gater

엔트로피 기반으로 저신뢰 출력을 걸러냅니다.

```typescript
import { EntropyGater } from '@commander/core';

const gater = new EntropyGater({ threshold: 0.7 });
const filtered = gater.filter(agentOutputs);
```

## Cycle Detector

태스크 그래프의 순환 의존을 탐지·해제합니다.

```typescript
import { CycleDetector } from '@commander/core';

const detector = new CycleDetector();
if (detector.hasCycle(taskGraph)) {
  const broken = detector.breakCycles(taskGraph);
}
```

## Context Window Manager

토큰 예산을 넘지 않도록 메시지를 압축·윈도우 슬라이딩합니다. 런타임 `ContextCompactor` / `TokenGovernor` 와 연동됩니다.

## 언제 쓰나

일반 앱은 CLI/SDK `run` 만으로 충분합니다. 커스텀 플래너·연구 계측·특수 토폴로지에서 위 컴포넌트를 직접 조합합니다.

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 관련

- [추측 실행](/ko/architecture/speculative-execution)  
- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [검증](/ko/architecture/verification)  
