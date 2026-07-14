# Changelog

## v0.2.1-pre (Unreleased)

### Features
- **SQLite persistence**: `SqliteWarRoomStore` with WAL mode, 9 indexes, transaction-safe writes. Enable via `WARROOM_STORAGE=sqlite`; `createWarRoomStore()` factory provides transparent switching
- **Event sourcing engine**: Write-Ahead Log with SHA-256 hash chain tamper protection, snapshot-based recovery, deterministic event replay (IF-05)
- **Recovery bootstrapper**: Process startup scans for zombie runs (EXECUTING/VERIFYING/PAUSED), acquires fencing lease, and either resumes from checkpoint or aborts with compensation
- **Petri net scheduler**: Formal resource allocation for sandbox execution slots (v8_slots, seccomp_slots, wasm_slots, tee_slots) with deadlock detection
- **Enterprise security gateway**: 7-layer defense-in-depth (zero-trust signatures, auth, rate limiting, input scanning, cost pre-check, request processing, DLP output scanning)
- **Data Loss Prevention (DLP)**: 12+ sensitive data pattern detections (API keys, JWT, PEM keys, credit cards, SSN, etc.) with 4 redaction strategies (REDACT/MASK/HASH/ALLOW)
- **Plugin security hardening**: Sandboxed load context prevents privilege escalation; `withTimeout()` enforces per-plugin `maxExecutionTimeMs`; `updateConfig()` routes through sandbox
- **RAG knowledge base plugin**: Built-in optional plugin (`builtin-rag`) with HNSW vector search, OpenAI/local embedding fallback, auto-inject context mode
- **Unified audit log**: Cross-source audit aggregation (security events, approvals, execution traces, user actions, config changes) with unified query, statistics, and export
- **Web onboarding wizard**: 4-step guided setup (welcome → provider config → first task → complete)
- **Grafana dashboards**: Developer view (business metrics) and Mechanistic view (ops metrics) with pre-configured Prometheus datasource
- **Agent degradation detection**: QualityGater using Agent Capsules method — starts with compound execution, escalates to per-agent when quality drops

### Improvements
- **260+ new unit tests** across 15 test files (sandbox, deliberation, memory, plugin, orchestration, runtime, API security)
- **ESLint `no-explicit-any`** upgraded from warn to error
- **Coverage thresholds** raised: statements 40→60%, functions 55→70%, lines 40→60%
- Prettier + EditorConfig formatting enforced in CI
- Staging environment CD pipeline

## v0.2.0 (2026-05-19)

### Features
- **Agent War Room**: Web GUI dashboard with live execution feed, topology visualization, and agent roster
- **OpenAPI 3.0**: Full REST API specification with Swagger UI
- **Readiness probe**: `/ready` endpoint for Kubernetes deployment
- **Prometheus metrics**: `/metrics` endpoint with OpenMetrics-compatible format
- **Multi-tenant isolation**: Per-tenant rate limits, concurrency, storage, memory, cache isolation
- **Circuit breakers**: Per-provider circuit breaker with 3-state (CLOSED/OPEN/HALF-OPEN) and registry
- **Dead letter queue**: Persistent failure storage with replay support, 7 categories, 15 failure modes
- **Compensation registry**: Automatic rollback for mutation tools via registered compensation actions
- **Graceful shutdown**: Connection draining with configurable timeout
- **HTTP security**: Default localhost binding, Bearer token auth, configurable CORS
- **Structured logging**: All `console.*` replaced with structured logger; zero empty catch blocks
- **Docker build**: 6-stage multi-architecture build with Nginx reverse proxy and tini init
- **Canonical topologies**: 5 canonical topologies (SINGLE/CHAIN/DISPATCH/ORCHESTRATOR/REVIEW) aligned with Anthropic's agent ontology, with 9 legacy aliases for backward compatibility
- **Artifact-based communication**: Agents communicate via references instead of raw text to prevent information loss
- **A2A protocol**: Agent-to-Agent HTTP server with Agent Card discovery and mandatory auth tokens

### CLI
- `commander company` — Enterprise pipeline with quality gates and memory
- `commander swarm` — Recursive decomposition with parallel execution
- `commander drive` — Autonomous step-by-step execution
- `commander goal` — Multi-round convergence loop
- `commander review` — AI code review (P0-P3 findings)
- `commander saga` — Saga transaction operations
- `commander budget` — Token budget management
- `commander checkpoint` — Checkpoint operations
- `commander cost` — Cost analysis

## v0.1.0 (2026-05-17)

### Features
- **8 orchestration topologies**: SINGLE, SEQUENTIAL, PARALLEL, HIERARCHICAL, HYBRID, DEBATE, ENSEMBLE, EVALUATOR-OPT
- **18 LLM providers**: OpenAI, Anthropic, Google, DeepSeek, GLM, MiMo, Groq, Together, Ollama, vLLM, Bedrock, xAI, OpenRouter, Mistral, Cohere, Replicate, Fireworks, Perplexity
- **25+ built-in tools**: Filesystem, LSP, web research, AST transformation, sub-agent delegation
- **Multi-tenant architecture**: Per-tenant rate limits, concurrency, storage, memory
- **Production readiness**: Circuit breakers, dead letter queues, compensation registry, atomic checkpoints
- **Observability**: Prometheus metrics, span-based tracing, SSE stream events
- **Plugin system**: 19 hook points (before/after LLM, tool, run, etc.)
- **Meta-learning**: Thompson Sampling + Reflexion for self-evolution

### CLI
- `commander <task>` — Quick task analysis
- `commander run <task>` — Full execution
- `commander plan <task>` — Deliberation plan
- `commander watch <task>` — SSE streaming
- `commander gui` — Agent War Room dashboard
- `commander tui` — Terminal dashboard
- 15 total commands

### Benchmarks
- **GAIA**: 69.7% (115/165) — +48.5 pp over bare MiMo
- **BFCL**: 60.0% tool / 91.4% parameter (35-scenario); 91.7%/91.7% (12-core)
- **PinchBench**: 97.7% (42/43) — vs OpenClaw 89.5%
- **HumanEval+**: 91.5%

### Deployment
- Docker Compose (6-stage multi-arch build)
- Production overlay with CPU/memory limits, health checks, JSON logging
- One-click VM deploy script
- GitHub Actions CI/CD
