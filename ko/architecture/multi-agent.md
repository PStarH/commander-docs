# 멀티 에이전트 오케스트레이션

Commander의 핵심 차별점은 **5개 정규 토폴로지**로 여러 에이전트를 조율하는 능력입니다. Anthropic의 “Building effective agents” 온톨로지에 맞춥니다. 레거시 이름 9개는 2버전 마이그레이션 동안 별칭으로 남습니다.

## 정규 토폴로지

| 토폴로지         | 설명                                 | 레거시 별칭                       |
| ---------------- | ------------------------------------ | --------------------------------- |
| **SINGLE**       | 한 에이전트가 전체 작업              | —                                 |
| **CHAIN**        | 순차 파이프라인, 이전 출력 위에 구축 | SEQUENTIAL                        |
| **DISPATCH**     | 독립 서브태스크 동시 실행 후 합성    | PARALLEL                          |
| **ORCHESTRATOR** | 리드가 분해·위임 후 합성             | HIERARCHICAL / HYBRID             |
| **REVIEW**       | 생성 → 비평 → 정제 루프              | DEBATE / ENSEMBLE / EVALUATOR-OPT |

## 토폴로지 선택

심의 엔진(`deliberation.ts`)이 작업을 분류하고 최적 토폴로지를 고릅니다.

| 복잡도    | 의존성 | 선택         |
| --------- | ------ | ------------ |
| Trivial   | 없음   | SINGLE       |
| Low       | 순차   | CHAIN        |
| Low       | 독립   | DISPATCH     |
| Medium    | 혼합   | ORCHESTRATOR |
| High      | 혼합   | ORCHESTRATOR |
| High-risk | 임의   | REVIEW       |
| Critical  | 임의   | REVIEW       |
| Iterative | 임의   | REVIEW       |

## 토폴로지 상세

### SINGLE

한 에이전트가 전체 처리. 단순·범위 명확한 요청.

### CHAIN

순서 실행, artifact 참조로 이전 출력 위에 쌓음. 다단계 변환.

### DISPATCH

독립 서브태스크를 서브 에이전트로 동시 실행 후 합성. 병렬화 가능한 작업.

### ORCHESTRATOR

리드가 분해·전문가에게 위임·합성. 혼합 병렬/순차 재라우팅.

### REVIEW

여러 에이전트가 독립 해법 → 교차 검증·정제. debate / ensemble / evaluator-optimizer 패턴.

## 에이전트 스케일

`effortScaler.ts`가 동적으로 수를 조절합니다.

- 단순: 1
- 보통: 2–5
- 복잡: 5–10
- 리서치: 10–20

## 통신

- **Message bus** (`messageBus.ts`): pub/sub
- **Agent handoff** (`agentHandoff.ts`): 영속 inbox 직접 핸드오프
- **Artifact system** (`artifactSystem.ts`): 참조 기반 통신
- **Three-layer memory**: working / episodic / long-term 공유

## 관련

- [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree)
- [에이전트 런타임](/ko/architecture/agent-runtime)
- [코어 호출 체인](/ko/architecture/core-call-chain)
