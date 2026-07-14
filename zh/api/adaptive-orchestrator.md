# 自适应编排器

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/api/adaptive-orchestrator)



Manages agent coordination and task execution across different orchestration modes.

## Types


```typescript
interface Agent {
  id: string;
  name: string;
  role: string;
  capabilities: string[];
  load: number;         // 0-1
  successRate: number;  // 0-1
  isAvailable: boolean;
}

interface OrchestrationPlan {
  id: string;
  mode: OrchestrationMode;
  tasks: Task[];
  agents: Agent[];
  resourceAllocation: ResourceAllocation;
  estimatedDuration: number;
}

interface ResourceAllocation {
  leadAgentId?: string;
  specialistAgentIds: string[];
  maxConcurrent: number;
  tokenBudget: {
    lead: number;
    specialists: number;
    evaluation: number;
    overhead: number;
  };
}
```

## API


```typescript
const orchestrator = new AdaptiveOrchestrator();

// Register agents
const agentId = orchestrator.registerAgent(
  agent: Omit<Agent, 'load' | 'successRate' | 'isAvailable'>
): string;

// Create plan
const plan = orchestrator.createPlan(
  tasks: Task[],
  suggestedMode?: OrchestrationMode
): OrchestrationPlan;

// Execute plan
const results = await orchestrator.execute(plan): Map<string, Task>;

// Get metrics
const metrics = orchestrator.getMetrics(): ExecutionMetrics;

// Adapt plan based on metrics
const adaptedPlan = orchestrator.adapt(plan: OrchestrationPlan): OrchestrationPlan;
```
