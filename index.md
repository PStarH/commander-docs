---
layout: home

hero:
  name: Commander
  text: Multi-Agent Orchestration Engine
  tagline: 18 providers · 8 topologies · 25+ tools · 330+ tests — production-grade from day one.
  image:
    src: /logo.svg
    alt: Commander
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: View on GitHub
      link: https://github.com/sampan/Commander
    - theme: alt
      text: Benchmarks
      link: /benchmarks

features:
  - title: Multi-Agent Orchestration
    details: 8 topologies — SINGLE, SEQUENTIAL, PARALLEL, HIERARCHICAL, HYBRID, DEBATE, ENSEMBLE, EVALUATOR-OPT — automatically selected based on task complexity.
    icon: 🧠
  - title: 18 LLM Providers
    details: OpenAI, Anthropic, Google, DeepSeek, GLM, MiMo, Groq, Together, Ollama, vLLM, Bedrock, xAI, OpenRouter, Mistral, Cohere, Replicate, Fireworks, Perplexity.
    icon: 🔌
  - title: Production-Grade
    details: Circuit breakers, dead letter queues, compensation registry, atomic state checkpoints, Prometheus metrics, span-based tracing.
    icon: 🛡️
  - title: Multi-Tenant
    details: Per-tenant rate limits, concurrency quotas, storage isolation, memory sandboxing, and API key mapping.
    icon: 🏢
  - title: 25+ Built-in Tools
    details: Filesystem ops, LSP integration, web research, AST-aware code transformation, sub-agent delegation, session management.
    icon: 🔧
  - title: Self-Evolving
    details: Thompson Sampling + Reflexion meta-learner for continuous improvement across runs. Plugin system with 19 hook points.
    icon: ⚡
---

## Benchmark Performance

| Benchmark | Commander | Bare LLM | OpenClaw |
|-----------|:---------:|:--------:|:--------:|
| **GAIA** (165 multi-step reasoning) | **69.7%** | 21.2% | — |
| **BFCL** (35 function calling scenarios) | Tool **60.0%** / Param **91.4%** | — | — |
| **PinchBench** (43 agentic tasks) | **97.7%** (42/43) | — | 89.5% |
| **HumanEval+** (164 Python problems) | **91.5%** | — | — |

Commander adds **+48.5 percentage points** over bare MiMo on GAIA. See the [full benchmarks](/benchmarks) for details.
