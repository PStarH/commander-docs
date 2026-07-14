# API リファレンス

Commander の API は **2 層** です。多くのアプリは Layer 1 だけで足ります。

## Layer 1 — 公開統合（ここから）

| 面 | パッケージ / 入口 | 用途 |
|----|-------------------|------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | 端末・スクリプト・CI |
| **TypeScript SDK** | `@commander/sdk` → `CommanderClient` | Node 埋め込み |
| **HTTP API** | サーバー `:4000` | 多言語・Web Console |
| **Python SDK** | `commander-ai`（HTTP） | API サーバー向け |

### TypeScript SDK

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();
```

| メソッド | 役割 |
|----------|------|
| `connect` / `disconnect` | ライフサイクル |
| `run(task)` | フル実行 → `ExecutionResult` |
| `plan(task)` | 審議のみ |
| `onEvent(handler)` | イベント・ストリーム |

> **npm:** monorepo 優先。公開は進行中。[Agent SDK](/ja/guide/sdk)。

### HTTP

```bash
curl http://localhost:4000/health
curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

V2: `POST /v1/runs` — [V2 移行](/ja/guide/migration-v2)。

### Python

```python
from commander import CommanderClient
```

[Python SDK](/ja/guide/sdk-python)。

---

## Layer 2 — ランタイム編成コンポーネント

`@commander/core` 内部。**ランタイム拡張**時のみ。

| コンポーネント | 目的 |
|----------------|------|
| [Task Complexity Analyzer](/ja/api/task-complexity-analyzer) | スコア → トポロジ |
| [Adaptive Orchestrator](/ja/api/adaptive-orchestrator) | マルチエージェント計画 |
| [Token Budget Allocator](/ja/api/token-budget-allocator) | 予算配分 |
| [Three-Layer Memory](/ja/api/three-layer-memory) | 3 層メモリ |
| [Reflection Engine](/ja/api/reflection-engine) | 事後評価 |
| [Consensus Checker](/ja/api/consensus-checker) | 高リスク合意 |
| [Inspector Agent](/ja/api/inspector-agent) | ヘルス / 問題検知 |

### Layer 2 を使うとき

カスタム・トポロジ、メモリ/合意の研究、サブシステム単体テスト。

### 使わないとき

「タスクを走らせたい」だけ → `CommanderClient`。遠隔多言語 → HTTP。

### 最小例

```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
} from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

const allocator = new TokenBudgetAllocator({ baseBudget: 100_000 });
const budget = allocator.allocate(
  complexity.recommendedTopology,
  complexity.score,
  3,
);
```

グローバル・アクセサ（`getGlobal…`）は共有状態が必要なときだけ。

## 関連

- [CLI コマンド](/ja/guide/commands)  
- [Web コンソール](/ja/guide/web-console)  
- [クックブック](/ja/guide/cookbook/)  
- [アーキテクチャ概要](/ja/architecture/overview)  
