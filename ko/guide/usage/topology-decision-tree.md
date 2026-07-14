# 토폴로지 의사결정 트리

어떤 오케스트레이션 토폴로지를 쓸지 모르겠다면 이 트리를 따르세요.

## 빠른 참조

```
작업이 단순하고 잘 정의되어 있나?
├── YES → SINGLE
└── NO  → 서브태스크가 독립적인가?
    ├── YES → DISPATCH
    └── NO  → 서로 의존하는가?
        ├── YES → CHAIN
        └── NO  → 명확한 리드 에이전트가 있나?
            ├── YES → ORCHESTRATOR
            └── NO  → REVIEW
```

## 상세

### SINGLE

**언제:** 단순·범위 명확 · **예:** 함수 설명, 파일 포맷 · **에이전트:** 1

### CHAIN

**언제:** 이전 단계에 의존하는 다단계 변환 · **에이전트:** 2–3

### DISPATCH

**언제:** 동시 실행 가능한 독립 서브태스크 · **에이전트:** 2–10

### ORCHESTRATOR

**언제:** 분해 경로가 있는 복잡 작업 · **에이전트:** 3–8

### REVIEW

**언제:** 교차 검증·합의가 필요한 고위험 · **에이전트:** 2–5

## 복잡도 기반 자동 선택

|  점수  | 자동 토폴로지 |
| :----: | :-----------: |
|  0–20  |    SINGLE     |
| 20–40  |     CHAIN     |
| 40–60  |   DISPATCH    |
| 60–80  | ORCHESTRATOR  |
| 80–100 |    REVIEW     |

강제:

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## 관련

- [멀티 에이전트](/ko/architecture/multi-agent)
- [토폴로지 탐색기](/ko/guide/topology-explorer)
- [작업 실행](/ko/guide/usage/running-tasks)
