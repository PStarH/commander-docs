# 적응형 오케스트레이터

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/api/adaptive-orchestrator)



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
