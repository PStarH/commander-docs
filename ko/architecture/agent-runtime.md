# 에이전트 런타임

Commander의 핵심 실행 엔진입니다. `AgentRuntime`은 단일 에이전트의 전체 수명주기를 관리합니다. LLM 호출, 도구 실행, 검증, 체크포인트, 재시도 — 모두 설정 가능한 토큰·스텝 예산 안에서.

## 구조

```
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot()        ← 동시성 세마포어
  ├─ [Tenant check]       ← rate limit + 동시성 쿼터
  ├─ resolve storage      ← 테넌트 스코프 메모리 + 캐시
  │
  ├─ [Retry loop: 0..maxRetries]
  │   ├─ callWithTimeout()       ← LLM 프로바이더
  │   ├─ [Tool execution loop]
  │   │   ├─ planner.plan()      ← 의존성 인식 실행 계획
  │   │   ├─ executeTool()       ← StepErrorBoundary → tool.execute()
  │   │   └─ cache.set()
  │   ├─ verification.check()    ← 5 품질 게이트
  │   └─ checkpoint()            ← atomic 저장
  │
  ├─ releaseSlot()
  └─ flush traces + samples
```

## 메인 루프

1. **슬롯 획득** — 최대 동시 run 초과 방지
2. **테넌트 검증** — rate limit·동시성 쿼터
3. **LLM 호출** — 타임아웃 설정 가능
4. **도구 실행** — `ToolPlanner`가 의존성을 분석해 병렬 가능 도구를 동시 실행
5. **검증** — 5 게이트 실패 시 재시도
6. **체크포인트** — 단계마다 atomic 영속화
7. **트레이싱** — 실행 트레이스·LLM 샘플 flush

## 핵심 컴포넌트

| 컴포넌트             | 파일                            | 역할                    |
| -------------------- | ------------------------------- | ----------------------- |
| `AgentRuntime`       | `runtime/agentRuntime.ts`       | 메인 루프               |
| `ToolPlanner`        | `runtime/toolPlanner.ts`        | 의존성 인식 도구 계획   |
| `ToolOrchestrator`   | `runtime/toolOrchestrator.ts`   | 계획된 도구 실행        |
| `StepErrorBoundary`  | `runtime/stepErrorBoundary.ts`  | 단계별 skip/retry/abort |
| `StepTimeoutManager` | `runtime/stepTimeoutManager.ts` | 단계 타임아웃           |
| `ContextCompactor`   | `runtime/contextCompactor.ts`   | 토큰 인식 메시지 압축   |
| `ContextWindow`      | `runtime/contextWindow.ts`      | 슬라이딩 윈도우         |
| `TokenGovernor`      | `runtime/tokenGovernor.ts`      | 토큰 예산               |
| `CycleDetector`      | `runtime/cycleDetector.ts`      | 무한 루프 탐지          |
| `ToolOutputManager`  | `runtime/toolOutputManager.ts`  | 도구 출력 토큰 예산     |

## 설정

```typescript
interface AgentRuntimeConfig {
  maxStepsPerRun: number; // run당 최대 LLM→tool 사이클
  maxRetries: number; // 검증 재시도
  timeoutMs: number; // LLM 호출 타임아웃
  maxConcurrency: number; // 최대 동시 에이전트
  budgetHardCapTokens: number; // 절대 토큰 상한
}
```

## 실행 계획

도구는 LLM 응답 순서 그대로가 아닙니다. `ToolPlanner`가 의존성을 분석합니다.

- 독립 도구는 동시 실행
- 종속 도구는 선행 후 순차
- 순환 의존성은 실행 전에 검증

## 관련

- [검증 파이프라인](/ko/architecture/verification)
- [멀티 에이전트](/ko/architecture/multi-agent)
- [코어 호출 체인](/ko/architecture/core-call-chain)
