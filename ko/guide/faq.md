# 자주 묻는 질문 (FAQ)

## 일반

### Commander란?

멀티 에이전트 오케스트레이션 엔진입니다. 5개 정규 토폴로지(SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW), 25 LLM 프로바이더, 18 내장 도구를 지원합니다.

### 다른 AI 코딩 도구와 무엇이 다른가?

대부분 도구는 단일 에이전트·단일 모델입니다. Commander는 **여러 에이전트**를 **토폴로지**로 조율하고, 복잡도 기반으로 전략을 고릅니다. 서킷 브레이커·멀티 테넌시·WAL 체크포인트·Prometheus·SSE 등 프로덕션 지향입니다.

### 오픈소스인가?

예. MIT 라이선스.

### 멀티 에이전트 오케스트레이션이란?

한 작업에 여러 AI 에이전트를 띄워 병렬·리뷰·리드-전문가 위임 등으로 협력하게 하는 것입니다.

## 설정

### API 키가 여러 개 필요한가?

아니요. **하나면 충분**합니다. `OPENAI_API_KEY`(또는 Anthropic, DeepSeek, Groq 등)만 설정하면 자동 감지. 여러 키를 두면 페일오버 체인이 동작합니다.

### 인터넷 없이 로컬만?

Ollama / vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### npm 패키지는?

`@commander/core` / `@commander/sdk` 공개는 **진행 중**. 지금은 monorepo를 클론해 workspace를 쓰세요. [Agent SDK](/ko/guide/sdk).

## 사용

### 파일을 수정하나?

기본은 가능. 승인 모드로 제어:

- `plan` — 계획만  
- `read-only` — 읽기만  
- `suggest` — 제안 후 승인  
- `auto-edit` — 자동 편집  
- `full-auto` — 완전 자율 (CI는 PR 리뷰 권장)  

### CI/CD에서?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

### 에이전트 수는?

복잡도 따라 1–20. 단순은 1, 복잡한 리서치/엔지니어링은 팀.

### 다섯 토폴로지?

| 토폴로지 | 언제 |
|----------|------|
| **SINGLE** | 단순 일회 |
| **CHAIN** | 순차 파이프 |
| **DISPATCH** | 병렬 전문가 + 합성 |
| **ORCHESTRATOR** | 리드가 위임 |
| **REVIEW** | 생성 후 비평/병합 |

[토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree).

## 성능 · 보안 · 더 보기

- 스트림·캐시·추측 실행으로 체감 지연을 줄입니다.  
- 보안: [보안](/ko/guide/security) · 게이트웨이 · DLP.  
- 문제: [문제 해결](/ko/guide/troubleshooting).  

## 관련

- [왜 Commander](/ko/guide/why-commander)  
- [빠른 시작](/ko/guide/getting-started)  
- [Cookbook](/ko/guide/cookbook/)  
