# Enterprise Security Gateway

Commander's `EnterpriseSecurityGateway` provides a 7-layer defense-in-depth architecture that is invoked during all LLM calls and tool executions. It cannot be bypassed — cost checks execute both before and after LLM calls.

## 7-Layer Defense

| Layer | Name | Purpose |
|-------|------|---------|
| 1 | Zero-Trust Signature | Integrity verification + replay prevention |
| 2 | Authentication | API Key validation with timing-safe comparison |
| 3 | Rate Limiting | Global token bucket + tiered IP limits |
| 4 | Input Scanning | Content injection detection + input validation |
| 5 | Cost Pre-Check | Bill explosion prevention (pre-call estimation) |
| 6 | Request Processing | Business logic execution |
| 7 | Output Scanning | DLP data leak prevention + cost recording |

### Design Principles

- **Defense in depth** — Multiple independent layers, each with distinct responsibility
- **Fail fast** — Reject early at the cheapest layer
- **Observable** — Every decision is logged with security metadata
- **Tenant isolation** — All checks are per-tenant
- **Unbypassable** — Cost checks execute both before and after LLM calls

## Data Loss Prevention (DLP)

The `dataLossPrevention.ts` module scans all egress points for sensitive data across a 5-stage pipeline.

### Detected Patterns (12+)

| Pattern | Example |
|---------|---------|
| API Key | `sk-...`, `sk-ant-...` |
| JWT | `eyJ...` |
| Private Key (PEM) | `-----BEGIN PRIVATE KEY-----` |
| Credit Card (Luhn) | `4111 1111 1111 1111` |
| SSN | `123-45-6789` |
| Email | `user@example.com` |
| Phone | `+1-555-0123` |
| Internal IP | `10.0.0.1`, `192.168.1.1` |
| Database Connection String | `mongodb://user:pass@host:port` |
| AWS/GCP/Azure Credentials | `AKIA...`, `AIza...` |
| China ID Card (checksum) | `110101199003077735` |
| Bank Account | Numeric with branch code |

### Redaction Strategies

| Strategy | Behavior |
|----------|----------|
| `REDACT` | Replace with `[REDACTED]` |
| `MASK` | Partial masking (`sk-...abc`) |
| `HASH` | SHA-256 hash |
| `ALLOW` | Pass through (logged only) |

### Egress Points

DLP is applied at all output boundaries:

- API responses
- Log entries
- Tool results
- Agent outputs
- SSE event streams

### Tool Input Scanning

Tool inputs are scanned for 6 specific sensitive patterns before execution:

1. API Key
2. Private Key
3. AWS Key
4. GitHub Token
5. JWT
6. Password

## Capability Tokens

The `capabilityToken.ts` module issues short-lived HMAC-signed authorization tokens:

- **Short TTL** — Tokens expire automatically, limiting exposure window
- **Scope-bound** — Each token carries specific capabilities (tool, resource, duration)
- **HMAC-signed** — Tamper-proof via server-side secret
- **Revocable** — Can be invalidated before expiry

All tool executions require capability token validation at execution points.

## Audit Chain Ledger

The `auditChainLedger.ts` creates a tamper-proof hash chain of all security-relevant events:

```
entry_1 → SHA256(prev_hash | entry_1) → hash_1
entry_2 → SHA256(hash_1 | entry_2) → hash_2
```

Any modification to historical entries breaks the chain, making tampering detectable.

## Agent Lineage

The `agentLineage.ts` module tracks immutable parent-child relationships between agents:

- `spawnChild()` validates parent node existence in the lineage tree
- Lineage is immutable once recorded
- Enables complete audit trail of agent delegation chains

## Additional Security Components

| Component | Purpose |
|-----------|---------|
| `guardianAgent.ts` | Semantic drift, anomaly, and safety monitoring |
| `securityMonitor.ts` | Continuous monitoring + anomaly detection + alerting |
| `zeroTrustValidator.ts` | Zero-trust request validation |
| `billExplosionGuard.ts` | Cost explosion prevention |
| `memoryPoisoningDefenseEngine.ts` | Memory poisoning attack defense |
| `toolPoisoningGuard.ts` | Tool poisoning detection |
| `mcpToolPoisoningGuard.ts` | MCP tool poisoning detection |
| `mlInjectionDetector.ts` | ML injection detection |
| `taintTracker.ts` | Taint tracking across data flows |
| `supplyChainScanner.ts` | Dependency supply chain scanning |
| `owaspAgenticAiTop10.ts` | OWASP Agentic AI Top 10 compliance |
| `mitreAtlasMapper.ts` | MITRE ATLAS threat mapping |
| `redTeamFramework.ts` | Red team testing framework |
| `postQuantumCrypto.ts` | Post-quantum cryptography |
| `gdprCompliance.ts` | GDPR compliance checking |
| `euAiActCompliance.ts` | EU AI Act compliance |

## Plugin Permission Enforcement

Third-party plugins receive a **sandboxed load context** that deliberately excludes the raw `HookManager`:

```typescript
// buildSandboxedLoadContext() — only for third-party plugins
const sandboxContext = {
  registerHook: enforcer.wrapRegisterHook(...),
  readFile: enforcer.wrapReadFile(...),
  writeFile: enforcer.wrapWriteFile(...),  // mode 0o600
  fetch: enforcer.wrapFetch(...),          // domain + port check
  getEnvVar: enforcer.wrapGetEnvVar(...),
  getConfig: enforcer.wrapGetConfig(...),
  log: enforcer.wrapLog(...),
};
// hookManager is NOT included — prevents privilege escalation
```

Built-in plugins (no enforcer) still receive the full `hookManager`.

### Permission Constraints

- Plugin permissions must **never exceed** main system permissions
- `updateConfig()` routes through the same sandbox context as `register()`
- `withTimeout()` uses `Math.min(plugin.maxExecutionTimeMs, globalTimeoutMs)` — the stricter value wins
- Network requests are URL-parsed and checked via `enforcer.checkNetwork()`
- All failures are reported via `reportSilentFailure` (never throws to plugin)
