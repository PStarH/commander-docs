# 플랜 모드

Commander가 **실행 전에 무엇을 할지** 보여 줍니다. 파일 변경 위험 없이 전략·에이전트·tools를 검토합니다.

## 왜 쓰나

- 안전 · 학습 · 디버그 · 팀 공유  

## 사용

```bash
npx tsx packages/core/src/cliEntry.ts mode plan
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## 출력 예

```
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4
┃ → Token budget: 100,000
```

[작업 실행](/ko/guide/usage/running-tasks) · [토폴로지 탐색기](/ko/guide/topology-explorer)
