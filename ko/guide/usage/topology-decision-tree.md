# 토폴로지 결정 트리

Not sure which orchestration topology to use? Follow this decision tree. **When**: Simple, well-scoped tasks

이 문서는 Commander에서 **토폴로지 결정 트리** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
Is the task simple and well-defined?
├── YES → SINGLE
└── NO  → Are subtasks independent?
    ├── YES → DISPATCH
    └── NO  → Do subtasks depend on each other?
        ├── YES → CHAIN
        └── NO  → Is there a clear lead agent?
            ├── YES → ORCHESTRATOR
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
