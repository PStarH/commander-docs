# 추측 실행 (Speculative Execution)

Commander는 LLM 사고 시간 동안 다음 도구 호출을 미리 실행하는 **PASTE 스타일 추측 실행**(Pattern-Aware Speculative Execution)을 구현합니다. 연구상 작업 완료 시간을 최대 약 48.5% 줄일 수 있습니다.

## 동작 방식

LLM이 생각·처리하는 동안, 관측된 패턴으로 다음 도구를 예측해 선실행합니다. 모델이 실제로 그 호출을 하면 결과는 이미 준비되어 있고(대기 0), 틀린 예측은 부작용 없이 버립니다.

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                                             Pre-executed tool results (cache)
```

## 안전

**읽기 전용** 도구만 추측 실행합니다.

- 예: `file.read`, `web.search`, `web.fetch`, `code.search`, `git.status`

**상태 변경** 도구는 절대 추측 실행하지 않습니다.

- 예: `file.write`, `file.edit`, `shell.execute`, `git.commit`, `apply_patch`

잘못된 예측도 부작용이 없습니다.

## PatternTracker

```typescript
import { PatternTracker } from '@commander/core';

const tracker = new PatternTracker();
tracker.recordSequence(['file.read', 'code.search', 'file.read']);
const predictions = tracker.predictNext(['file.read']);
// → [{ toolName: 'code.search', confidence: 0.8 }]
```

### 패턴 수명주기

1. **관측** — n-gram (2, 3, 4) 시퀀스 기록  
2. **신뢰도** — 재현 시 `min(1, frequency / 10)` 증가  
3. **정리** — 출현 &lt;2 또는 5분 미사용 패턴 제거  

## 운영 메모

추측 실행은 런타임 내부 최적화입니다. 사용자는 `run --stream` 으로 도구 호출을 그대로 봅니다. 설치·CLI는 monorepo 우선:

```bash
npx tsx packages/core/src/cliEntry.ts run "explain this repo" --stream
```

## 관련

- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [도구](/ko/architecture/tools)  
- [캐싱](/ko/architecture/caching)  
