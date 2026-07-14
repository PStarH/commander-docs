# 코어 호출 체인

모든 Commander 실행은 구조화된 파이프라인을 따릅니다.

## 1. 심의 (Deliberation)

```
CLI / HTTP / API
  │
  ├─ deliberation.ts     ← "이 작업은 어떤 종류인가?"
  │   └─ TaskComplexityAnalyzer
```

복잡도·의존 그래프·도메인을 분석해 실행 전략을 정합니다.

## 2. 노력 스케일링

```
  ├─ effortScaler.ts     ← "에이전트 몇 명?"
```

1–20 에이전트로 스케일. 단순 작업은 1명, 복잡한 리서치는 팀.

## 3. 토폴로지 라우팅

```
  ├─ topologyRouter.ts   ← "어떤 토폴로지?"
```

5 정규 토폴로지: **SINGLE** · **CHAIN** · **DISPATCH** · **ORCHESTRATOR** · **REVIEW** (레거시 별칭 지원).

## 4. 원자화

```
  ├─ atomizer.ts         ← "서브태스크로 분해"
```

ROMA 스타일 분해로 의존성 인식 원자 작업 생성.

## 5. 실행

```
  ├─ agentRuntime.ts.execute(ctx)
      ├─ acquireSlot / tenant check / storage
      ├─ [Retry loop]
      │   ├─ LLM callWithTimeout
      │   ├─ ToolPlanner → executeTool → cache
      │   ├─ verification (5 gates)
      │   └─ checkpoint
      └─ releaseSlot / flush traces
```

## 6. 검증 & 합성

품질 게이트 통과 후 리드/합성기가 최종 결과를 만듭니다. 실패 시 재시도·DLQ·보상.

## 로컬에서 따라가기

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)  
- [멀티 에이전트](/ko/architecture/multi-agent)  
- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [검증](/ko/architecture/verification)  
