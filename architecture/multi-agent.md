# Multi-Agent Orchestration

Commander's core differentiator is its ability to orchestrate multiple agents across **8 distinct topologies**.

## Topology Selection

The deliberation engine (`deliberation.ts`) classifies every task and selects the optimal topology:

| Complexity | Dependencies | Selected Topology |
|------------|-------------|-------------------|
| Trivial | None | SINGLE |
| Low | Sequential | SEQUENTIAL |
| Low | Independent | PARALLEL |
| Medium | Mixed | HIERARCHICAL |
| High | Mixed | HYBRID |
| High-risk | Any | DEBATE |
| Critical | Any | ENSEMBLE |
| Iterative | Any | EVALUATOR-OPT |

## Topology Details

### SINGLE
One agent handles the entire task. Best for simple, well-scoped requests.

### SEQUENTIAL
Agents execute in order, each building on the previous output. Best for multi-step transformations.

### PARALLEL
Independent subtasks run concurrently via sub-agents. Results are synthesized at the end.

### HIERARCHICAL
A lead agent decomposes the task and delegates subtasks to specialist agents, then synthesizes results.

### HYBRID
Mixed topology: some steps run in parallel, others sequentially, with adaptive rerouting.

### DEBATE
Multiple agents independently solve the same problem, then cross-validate each other's answers.

### ENSEMBLE
Multiple models vote on the answer, weighted by their confidence and historical accuracy.

### EVALUATOR-OPTIMIZER
Generate → critique → refine loop. One agent produces output, another critiques, the first refines.

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
- **Three-layer memory**: Shared working/episodic/long-term memory for context across agents
