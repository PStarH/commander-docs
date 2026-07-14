# Frequently Asked Questions

**Frequently Asked Questions.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Topology | Use when |
|----------|----------|
| **SINGLE** | Simple, one-shot answers |
| **CHAIN** | Sequential pipeline steps |
| **DISPATCH** | Parallel specialists + synthesis |
| **ORCHESTRATOR** | Lead agent delegates to workers |
| **REVIEW** | Produce then critique / merge |


## 주요 섹션

### General

**General** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Setup

**Setup** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Usage

**Usage** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Performance

**Performance** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Enterprise

**Enterprise** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Data & Privacy

**Data & Privacy** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Related

**Related** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```
```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

## 운영 체크

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
