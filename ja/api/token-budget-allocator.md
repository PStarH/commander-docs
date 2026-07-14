# Token Budget Allocator

**Token Budget Allocator.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Topology | Lead | Specialists | Evaluation | Overhead |
|----------|------|-------------|------------|----------|
| SINGLE | 95% | 0% | 5% | 0% |
| CHAIN | 30% | 50% | 15% | 5% |
| DISPATCH | 15% | 65% | 15% | 5% |
| ORCHESTRATOR | 35% | 45% | 15% | 5% |
| REVIEW | 25% | 30% | 40% | 5% |


## 主な内容

### Types

運用では **Types** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/token-budget-allocator)を参照してください。

### API

運用では **API** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/token-budget-allocator)を参照してください。

### Allocation by Topology

運用では **Allocation by Topology** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/token-budget-allocator)を参照してください。

## 例（コードは英語のまま）

```typescript
interface TokenBudget {
  totalBudget: number;
  perAgentBudget: number;
  reservedForTools: number;
  reservedForVerification: number;
}

interface AllocationResult {
  lead: number;
  specialists: number;
  evaluation: number;
  overhead: number;
}
```

```typescript
const allocator = new TokenBudgetAllocator({ baseBudget: 100000 });

// Allocate based on topology
const budget = allocator.allocate(
  topology: Topology,
  complexity: number,
  agentCount: number
): TokenBudget;

// Get allocation breakdown
const allocation = allocator.getAllocation(
  topology: OrchestrationTopology,
  totalBudget: number
): AllocationResult;
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
