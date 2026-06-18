# Changelog

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

### Deployment
- Docker Compose (6-stage multi-arch build)
- Production overlay with CPU/memory limits, health checks, JSON logging
- One-click VM deploy script
- GitHub Actions CI/CD
