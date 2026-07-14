# Chaos Testing

**Chaos Testing.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Layer | Name | What it injects |
|-------|------|----------------|
| **L1** | LLM | Provider-level faults: rate limits, timeouts, context window overflow, malformed responses |
| **L2** | Tool | 10 failure modes: `http_5xx`, `http_4xx`, `disk_full`, `oom`, `process_crash`, `state_corrupt`, `dependency_unavailable`, `time_drift`, `auth_expired`, `http_timeout` |
| **L3** | System | Process/disk/CPU/memory faults: CPU throttle, memory pressure, disk full simulation |
| **L4** | Tenant | Multi-tenant blast radius enforcement: cross-tenant access attempts, resource exhaustion |


## 주요 섹션

### Quick Start

**Quick Start** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Chaos Layers

**Chaos Layers** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Running Chaos Tests

**Running Chaos Tests** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Recovery Verification

**Recovery Verification** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Adding New Scenarios

**Adding New Scenarios** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Programmatic API

**Programmatic API** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### CI Integration

**CI Integration** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```bash
# Run a single-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Run multi-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# With recovery verification (default)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```
```bash
# LLM provider faults only
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1

# Tool failure injection
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L2

# System-level faults
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L3

# Tenant isolation testing (requires --tenant)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L4 --tenant=ci-staging
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
