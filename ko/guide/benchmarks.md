# Benchmarks

**Benchmarks.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Suite | Coverage | Result (as documented) |
|-------|----------|------------------------|
| Chaos Engineering | 255 synthetic + 55 mutation | 55.7% pass rate |
| Red Team | 47 scenarios, 8 attack categories | 100% defense |
| AgentDojo | 12 security test cases | 100% defense |
| RealWorld | 50 production-like cases | 96% pass rate |
| GAIA Spine | Core capability | Running daily |
| SLO | API success / latency | Measured daily |


## 주요 섹션

### Headline matrix (product README)

**Headline matrix (product README)** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Reliability SLO Targets

**Reliability SLO Targets** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Health Check Components

**Health Check Components** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Chaos Engineering Benchmark

**Chaos Engineering Benchmark** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Topology Performance

**Topology Performance** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Provider Latency

**Provider Latency** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Test Suite

**Test Suite** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Reproducing Benchmarks

**Reproducing Benchmarks** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```bash
pnpm benchmark:all          # multi-suite readiness
pnpm benchmark:redteam      # 47 scenarios
pnpm benchmark:agentdojo    # injection suite
pnpm benchmark:chaos        # chaos (simulated default)
pnpm bench:slo              # SLO baseline
pnpm check:readiness        # baseline freshness
```
```bash
# Run full 255-case benchmark
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=bench --duration=300

# Run specific domain
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=bench --fault-types=payment_timeout,rate_limit
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
