# Speculative Execution

Commander implements **PASTE-style speculative execution** (Pattern-Aware Speculative Execution) that pre-executes likely tool calls during LLM thinking time. Research shows this achieves up to 48.5% reduction in task completion time. During LLM thinking/processing time, Commander predicts the most likely next tool calls based on observed patterns and pre-executes them. If the model actually makes

이 문서는 Commander에서 **Speculative Execution** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                         ┌─────────────────────────────┘
                         ▼
               ┌──────────────────┐
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
