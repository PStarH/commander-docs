# 多代理编排

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/multi-agent)



Commander's core differentiator is its ability to orchestrate multiple agents across **5 canonical topologies**, aligned with Anthropic's "Building effective agents" ontology. Nine legacy topology names remain as aliases for backward compatibility during a 2-version migration window.

## Canonical Topologies


| Topology | Description | Legacy Alias |
|----------|-------------|--------------|
| **SINGLE** | One agent handles the entire task | — |
| **CHAIN** | Sequential pipeline, each agent builds on previous output | SEQUENTIAL |
| **DISPATCH** | Independent subtasks run concurrently, results synthesized | PARALLEL |
| **ORCHESTRATOR** | Lead agent decomposes and delegates to specialists | HIERARCHICAL / HYBRID |
| **REVIEW** | Generate → critique → refine loop | DEBATE / ENSEMBLE / EVALUATOR-OPT |

## Topology Selection


The deliberation engine (`deliberation.ts`) classifies every task and selects the optimal topology:

| Complexity | Dependencies | Selected Topology |
|------------|-------------|-------------------|
| Trivial | None | SINGLE |
| Low | Sequential | CHAIN |
| Low | Independent | DISPATCH |
| Medium | Mixed | ORCHESTRATOR |
| High | Mixed | ORCHESTRATOR |
| High-risk | Any | REVIEW |
| Critical | Any | REVIEW |
| Iterative | Any | REVIEW |

## Topology Details


### SINGLE

One agent handles the entire task. Best for simple, well-scoped requests.

### CHAIN

Agents execute in order, each building on the previous output via artifact references. Best for multi-step transformations.

### DISPATCH

Independent subtasks run concurrently via sub-agents. Results are synthesized at the end. Best for parallelizable work.

### ORCHESTRATOR

A lead agent decomposes the task and delegates subtasks to specialist agents, then synthesizes results. Adaptive rerouting allows mixed parallel/sequential execution.

### REVIEW

Multiple agents independently produce solutions, then cross-validate and refine. Includes debate (cross-validation), ensemble (weighted voting), and evaluator-optimizer (generate-critique-refine) patterns.

## Agent Scaling


The `effortScaler.ts` module scales the number of agents dynamically:

- **Simple tasks**: 1 agent
- **Moderate tasks**: 2–5 agents
- **Complex tasks**: 5–10 agents
- **Research tasks**: 10–20 agents

## Agent Communication


Agents communicate through:

- **Message bus** (`messageBus.ts`): Pub/sub for inter-agent and system events
- **Agent handoff** (`agentHandoff.ts`): Direct agent-to-agent handoff with persistent inbox
- **Artifact system** (`artifactSystem.ts`): Reference-based communication to prevent information loss
- **Three-layer memory**: Shared working/episodic/long-term memory for context across agents
