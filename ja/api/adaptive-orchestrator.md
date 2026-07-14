# Adaptive Orchestrator

**Adaptive Orchestrator.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 主な内容

### Types

運用では **Types** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/adaptive-orchestrator)を参照してください。

### API

運用では **API** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/adaptive-orchestrator)を参照してください。

## 例（コードは英語のまま）

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

## 運用

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
