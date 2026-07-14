# Cookbook: Security audit a repository

**Goal:** Run a multi-agent security-oriented audit with live streaming and readable findings.

**Time:** ~10 minutes · **Risk:** read-heavy (prefer `read-only` or `plan` first)

## 1. Setup

```bash
cd /path/to/Commander   # monorepo root
export OPENAI_API_KEY=sk-...   # or any supported key
```

Optional: restrict writes while learning:

```bash
export COMMANDER_MODE=read-only
```

## 2. Plan first

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**Expect:** classification (often ANALYSIS), complexity score, topology (often DISPATCH or REVIEW), agent roles.

## 3. Execute with stream

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**Expect in the stream:**

- Deliberation banner (task class + topology)  
- Multiple agents or sequential tools (grep, package audit, etc.)  
- Quality gate lines (ACCURACY / COMPLETENESS / SAFETY …)  
- A synthesized findings summary  

## 4. Tighten the topology (optional)

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream --topology review
```

REVIEW forces produce → critique style execution when you want higher scrutiny.

## 5. Success checklist

- [ ] Plan printed a topology without crashing  
- [ ] Stream showed agent/tool activity  
- [ ] Final summary lists concrete findings or explicit “none found” with scope  
- [ ] No unexplained hang (>2 min with zero events)  

## Failure modes

| Issue | Action |
|-------|--------|
| No provider | `doctor`; verify env var in current shell |
| Empty / shallow audit | Point at a real codebase path; increase specificity in the prompt |
| SAFETY gate flags | Expected if secrets-like patterns exist — treat as signal |
| Cost / latency high | Use `plan` only, or a faster provider (Groq) for triage |

## Related

- [Security](/guide/security)  
- [Topology Decision Tree](/guide/usage/topology-decision-tree)  
- [Watch Mode](/guide/usage/watch-mode)  
