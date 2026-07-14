# 아키텍처 개요

Commander는 단일 작업 설명을 여러 에이전트·도구·LLM 프로바이더에 걸친 구조화된 실행 계획으로 바꿉니다.

## 먼저 읽을 다섯 페이지

1. **이 페이지** — 고수준 흐름과 패키지 맵  
2. [코어 호출 체인](/ko/architecture/core-call-chain)  
3. [멀티 에이전트](/ko/architecture/multi-agent)  
4. [에이전트 런타임](/ko/architecture/agent-runtime)  
5. [검증 파이프라인](/ko/architecture/verification)  

나머지는 선택적 심화(신뢰성·보안·시스템)입니다.

## 고수준 흐름

```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         작업 분석 & 토폴로지 선택
  ├─ effortScaler.ts         에이전트 1–20 스케일
  ├─ topologyRouter.ts       5 정규 토폴로지
  ├─ atomizer.ts             ROMA 분해
  │
  ├─ agentRuntime.ts         LLM → tools → verify → retry
  │   ├─ providers/          25 프로바이더 + 폴백
  │   ├─ toolResultCache / stateCheckpointer / circuitBreaker
  │   ├─ deadLetterQueue / compensation / verificationLoop
  │   └─ eventSourcing / qualityGater
  │
  ├─ enterpriseSecurityGateway (7계층) · DLP · capability tokens
  ├─ agentHandoff / messageBus / metrics / threeLayerMemory
  ├─ hallucinationDetector / reflection / metaLearner
  ├─ recoveryBootstrapper / unifiedAuditLog
  └─ pluginManager (19 hook)
```

## 패키지 구조

```
packages/core/src/
├── runtime/     실행 엔진
├── ultimate/    오케스트레이션
├── security/    보안 게이트웨이
├── tools/       18 내장 도구
├── sandbox/     프로파일, TEE, seccomp, Petri net
├── atr/         Agent Transaction Runtime
├── selfEvolution/  메타러닝
├── saga/        보상 트랜잭션
├── mcp/         MCP + A2A
└── plugins/builtin/  RAG 등
```

## 설계 원칙

1. **Topology-first** — 실행 전에 작업 구조를 분석  
2. **Provider-agnostic** — 25 프로바이더 통일 인터페이스 + 폴백  
3. **Crash-safe** — 단계마다 WAL 체크포인트, 이벤트 재생  
4. **Observable by default** — 메트릭, 트레이스, SSE, Grafana  
5. **Multi-tenant by design** — 스토리지·메모리·쿼터·캐시 격리  
6. **Secure by default** — 7계층 게이트웨이, DLP, 토큰, 플러그인 샌드박스  
7. **Reversible by design** — 해시 체인, 보상, DLQ, RecoveryBootstrapper  

## 로컬에서 보기

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

## 관련

- [프로덕션 준비](/ko/architecture/production-readiness)  
- [빠른 시작](/ko/guide/getting-started)  
- [API 개요](/ko/api/overview)  
