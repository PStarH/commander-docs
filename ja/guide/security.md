# セキュリティ

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/security)



Commander is designed for multi-agent workloads that touch code, tools, and untrusted model output. This page is the operator-facing summary. Deep dives: [Security Gateway](/ja/architecture/security-gateway), [Sandbox](/ja/architecture/sandbox), [Multi-Tenancy](/ja/architecture/multi-tenancy).

## 脆弱性の報告


**Do not open public GitHub issues for security bugs.**

Email **sampan090611@gmail.com** with:

- Issue type and impact  
- Paths / commits involved  
- Reproduction steps  
- PoC if available  

Expect acknowledgment within **48 hours** (see product [SECURITY.md](https://github.com/PStarH/Commander/blob/master/SECURITY.md)).

## 脅威モデル（要約）


| Threat | Mitigations in Commander |
|--------|---------------------------|
| Prompt / tool injection | Injection scanning on tool output, sanitizers, reversibility gates for irreversible tools |
| Secrets leakage | DLP patterns, structured logging without secrets, vault patterns in enterprise gateway |
| Runaway agents | Approval modes, token budgets, timeouts, circuit breakers |
| Provider outage / abuse | Failover chains, rate limits, per-tenant quotas |
| Cross-tenant bleed | Tenant isolation (storage, memory, cache, rate limits) |
| Supply-chain / deps | CI npm audit; keep keys out of git |

## 設定すべき制御


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


Default posture favors localhost for the API. In production, put TLS termination and auth at the reverse proxy ([Deployment](/ja/deployment)).

### 4. Local / sensitive code


Prefer **Ollama / vLLM** so code never leaves your network:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Multi-tenant production


Enable tenant provider and quotas — see [Multi-Tenancy](/ja/architecture/multi-tenancy).

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

Details: [Benchmarks](/ja/guide/benchmarks) · product `BENCHMARK.md`.

## アーキテクチャマップ


```
Request / CLI
  → Auth / rate limit / tenant context
  → Deliberation + topology
  → Agent runtime (tools under policy)
  → Security gateway / sandbox / DLP
  → Quality gates (incl. SAFETY)
  → Result + audit / event log
```

## 本番前チェックリスト


- [ ] `COMMANDER_API_KEY` set; no default example keys  
- [ ] Approval mode appropriate for environment  
- [ ] Provider keys only in secret store / env  
- [ ] Health + metrics endpoints monitored  
- [ ] DLQ / compensation reviewed for write-heavy tools  
- [ ] Backup strategy for SQLite/Postgres state  

## 関連


- [Security Gateway](/ja/architecture/security-gateway)  
- [Sandbox](/ja/architecture/sandbox)  
- [Cookbook: security audit](/ja/guide/cookbook/security-audit)  
- [Community / responsible disclosure](/ja/community)  
