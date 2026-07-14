# 멀티 에이전트 오케스트레이션

Commander's core differentiator is its ability to orchestrate multiple agents across **5 canonical topologies**, aligned with Anthropic's "Building effective agents" ontology. Nine legacy topology names remain as aliases for backward compatibility during a 2-version migration window. The deliberation engine (`deliberation.ts`) classifies every task and selects the optimal topology:

이 문서는 Commander에서 **멀티 에이전트 오케스트레이션** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
