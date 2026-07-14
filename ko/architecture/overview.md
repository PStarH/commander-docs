# 아키텍처 개요

Commander는 작업 설명을 여러 에이전트·tools·LLM 프로바이더에 걸친 구조화 실행 계획으로 바꾸는 multi-agent 오케스트레이션 엔진입니다.

## 먼저 읽을 다섯 페이지

1. **이 페이지**  
2. [핵심 호출 체인](/ko/architecture/core-call-chain)  
3. [멀티 에이전트](/ko/architecture/multi-agent)  
4. [에이전트 런타임](/ko/architecture/agent-runtime)  
5. [검증 파이프라인](/ko/architecture/verification)  

## 고수준 흐름

```
CLI / HTTP / SDK
  → 심의 (분류·복잡도)
  → 노력 스케일 (1–20)
  → 토폴로지
  → 런타임 (LLM ↔ tools)
  → 품질 게이트
  → 합성 · 영속화 · 메트릭
```

## 설계 원칙

토폴로지 우선 · 프로바이더 비의존(25+fallback) · 크래시 안전 · 기본 관측 가능 · 멀티 테넌트 · 기본 보안 · 가역성.

[프로덕션 준비](/ko/architecture/production-readiness) · [빠른 시작](/ko/guide/getting-started)
