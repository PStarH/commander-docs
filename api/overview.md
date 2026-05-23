# API Reference

Commander exposes 7 core components for multi-agent orchestration.

## Components

| Component | Size | Purpose |
|-----------|------|---------|
| [Task Complexity Analyzer](/api/task-complexity-analyzer) | 14.1KB | Analyzes task complexity and selects orchestration mode |
| [Adaptive Orchestrator](/api/adaptive-orchestrator) | 16.2KB | Manages agent coordination and task execution |
| [Token Budget Allocator](/api/token-budget-allocator) | 9.9KB | Allocates and tracks token budgets |
| [Three-Layer Memory](/api/three-layer-memory) | 9.6KB | Manages working, episodic, and long-term memory |
| [Reflection Engine](/api/reflection-engine) | 13.2KB | Self-reflection and pattern detection |
| [Consensus Checker](/api/consensus-checker) | 11.3KB | Multi-model consensus for high-risk decisions |
| [Inspector Agent](/api/inspector-agent) | 13.6KB | System health monitoring and issue detection |

## Complete Workflow Example

```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
  ThreeLayerMemory,
  ReflectionEngine,
  ConsensusChecker,
  InspectorAgent
} from '@commander/core';

// 1. Analyze task
const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high'
});

// 2. Allocate budget
const allocator = new TokenBudgetAllocator({ baseBudget: 100000 });
const budget = allocator.allocate(complexity.recommendedMode, complexity.score, 3);

// 3. Create plan
const orchestrator = new AdaptiveOrchestrator();
orchestrator.registerAgent({
  id: 'lead', name: 'Lead', role: 'architect', capabilities: []
});
const plan = orchestrator.createPlan(
  [{ id: 'task-1', description: '...', complexity: complexity.score }],
  complexity.recommendedMode
);

// 4. Store in memory
const memory = new ThreeLayerMemory();
memory.add('Starting task', 'working', 'task-1', 0.9);

// 5. Consensus for high-risk decisions
const checker = new ConsensusChecker();
const checkId = checker.createCheck('Best technology stack?');
checker.addVote(checkId, 'm1', 'Model A', 'Kafka + ES', 0.9, 'Industry standard');
checker.addVote(checkId, 'm2', 'Model B', 'Kafka + ES', 0.85, 'Scalable');
const result = checker.getResult(checkId);

// 6. Reflect
const engine = new ReflectionEngine();
const sessionId = engine.startSession('task-1');
engine.addReflection(sessionId, 'post_execution', 'Result?', 'Succeeded');
engine.completeSession(sessionId, 'success');

// 7. Inspect
const inspector = new InspectorAgent();
inspector.updateComponent('orchestrator', 'healthy', 0.9);
const report = inspector.inspect();
```

## Global Accessors

Each component has a global singleton accessor:

- `getGlobalTaskComplexityAnalyzer()`
- `getGlobalAdaptiveOrchestrator()`
- `getGlobalTokenBudgetAllocator()`
- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalConsensusChecker()`
- `getGlobalInspectorAgent()`
