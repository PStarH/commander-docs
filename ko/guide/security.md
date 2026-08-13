# 보안

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/security)



Commander is designed for multi-agent workloads that touch code, tools, and untrusted model output. This page is the operator-facing summary. Deep dives: [Security Gateway](/ko/architecture/security-gateway), [Sandbox](/ko/architecture/sandbox), [Multi-Tenancy](/ko/architecture/multi-tenancy).

## 취약점 보고


**Do not open public GitHub issues for security bugs.**

Email **sampan090611@gmail.com** with:

- Issue type and impact  
- Paths / commits involved  
- Reproduction steps  
- PoC if available  

Expect acknowledgment within **48 hours** (see product [SECURITY.md](https://github.com/PStarH/Commander/blob/master/SECURITY.md)).

## 위협 모델(요약)


| Threat | Mitigations in Commander |
|--------|---------------------------|
| Prompt / tool injection | Injection scanning on tool output, sanitizers, reversibility gates for irreversible tools |
| Secrets leakage | DLP patterns, structured logging without secrets, vault patterns in enterprise gateway |
| Runaway agents | Approval modes, token budgets, timeouts, circuit breakers |
| Provider outage / abuse | Failover chains, rate limits, per-tenant quotas |
| Cross-tenant bleed | Tenant isolation (storage, memory, cache, rate limits) |
| Supply-chain / deps | CI npm audit; keep keys out of git |

## 구성해야 할 제어


### 1. Approval modes


| Mode | Use when |
|------|----------|
| `plan` | Preview only |
| `read-only` | Analysis / audit |
| `suggest` | Human approves writes |
| `auto-edit` | Trusted local dev |
| `full-auto` | CI with PR review |

```bash
export COMMANDER_MODE=read-only
```

### 2. API authentication


When running the HTTP server:

```bash
export COMMANDER_API_KEY="long-random-secret"
```

Require Bearer tokens on API routes; do not expose `:4000` to the public internet without TLS and auth.

### 3. Network binding


Default posture favors localhost for the API. In production, put TLS termination and auth at the reverse proxy ([Deployment](/ko/deployment)).

### 4. Local / sensitive code


Prefer **Ollama / vLLM** so code never leaves your network:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Multi-tenant production


Enable tenant provider and quotas — see [Multi-Tenancy](/ko/architecture/multi-tenancy).

## Security benchmarks (in monorepo)


| Suite | Purpose |
|-------|---------|
| Red Team (47 scenarios) | Attack categories against defenses |
| AgentDojo | Indirect injection robustness |
| Tenant isolation fuzz | Cross-tenant mutation tests |

Run from the product repo:

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

Details: [Benchmarks](/ko/guide/benchmarks) · product `BENCHMARK.md`.

## 아키텍처 맵


```
Request / CLI
  → Auth / rate limit / tenant context
  → Deliberation + topology
  → Agent runtime (tools under policy)
  → Security gateway / sandbox / DLP
  → Quality gates (incl. SAFETY)
  → Result + audit / event log
```

## 프로덕션 전 체크리스트


- [ ] `COMMANDER_API_KEY` set; no default example keys  
- [ ] Approval mode appropriate for environment  
- [ ] Provider keys only in secret store / env  
- [ ] Health + metrics endpoints monitored  
- [ ] DLQ / compensation reviewed for write-heavy tools  
- [ ] Backup strategy for SQLite/Postgres state  

## 관련


- [Security Gateway](/ko/architecture/security-gateway)  
- [Sandbox](/ko/architecture/sandbox)  
- [Cookbook: security audit](/ko/guide/cookbook/security-audit)  
- [Community / responsible disclosure](/ko/community)  
