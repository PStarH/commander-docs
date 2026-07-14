# 대화형 토폴로지 탐색기

Pick a task shape. Commander’s deliberation engine maps similar signals onto one of **five canonical topologies**. This page is a decision aid — not a substitute for `plan`. Answer mentally, then confirm with `plan`:

이 문서는 Commander에서 **대화형 토폴로지 탐색기** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
Is the task a single clear question with one owner?
  YES → SINGLE
  NO  ↓
Does work form a strict pipeline (A then B then C)?
  YES → CHAIN
  NO  ↓
Can specialists work in parallel then merge?
  YES → DISPATCH
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
