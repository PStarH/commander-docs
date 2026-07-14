# Smart Model Router

**Smart Model Router.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Capability | Description |
|------------|-------------|
| `code` | Code generation and understanding |
| `reasoning` | Logical reasoning and chain-of-thought |
| `analysis` | Data analysis and interpretation |
| `creative` | Creative writing and brainstorming |
| `math` | Mathematical computation |
| `multimodal` | Multiple input modalities |
| `vision` | Image understanding |
| `image_generation` | Image creation |
| `long_context` | Large context window support |
| `low_cost` | Cost-efficient inference |
| `fast` | Low-latency inference |
| `high_quality` | Highest quality output |
| `function_calling` | Tool use support |
| `json_mode` | Structured JSON output |
| `streaming` | Streaming response support |
| `translation` | Multi-language translation |
| `summarization` | Text summarization |
| `extraction` | Information extraction |


## 主な節

### Capabilities

**Capabilities** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Configuration

**Configuration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Routing Modes

**Routing Modes** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Model Tiers

**Model Tiers** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Routing Decision

**Routing Decision** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Programmatic API

**Programmatic API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Integration with Deliberation

**Integration with Deliberation** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```typescript
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
      capabilities: ['code', 'reasoning', 'function_calling', 'streaming'],
      costPer1MInput: 2.5,
      costPer1MOutput: 10,
      contextWindow: 128000,
      tier: 'power',
    },
    {
      id: 'claude-sonnet-4-20250514',
      provider: 'anthropic',
      capabilities: ['code', 'reasoning', 'long_context', 'function_calling'],
      costPer1MInput: 3,
      costPer1MOutput: 15,
      contextWindow: 200000,
      tier: 'power',
    },
    {
      id: 'deepseek-chat',
      provider: 'deepseek',
      capabilities: ['code', 'reasoning', 'low_cost'],
      costPer1MInput: 0.14,
      costPer1MOutput: 0.28,
      contextWindow: 64000,
      tier: 'eco',
    },
  ],
  routingRules: [
    {
      taskType: 'code_review',
      requiredCapabilities: ['code', 'reasoning'],
      preferredTier: 'power',
      maxCostPer1K: 0.05,
    },
    {
      taskType: 'simple_query',
      requiredCapabilities: ['reasoning'],
      preferredTier: 'eco',
      maxCostPer1K: 0.001,
    },
  ],
  budget: {
    maxCostPerTask: 1.0,
    dailyBudget: 10.0,
  },
});
```
```
Task → Analyze requirements → Match capabilities → Filter by budget
                                                         │
                    ┌────────────────────────────────────┘
                    ▼
            Select model by tier preference
                    │
                    ┌────────────────────────────────────┐
                    ▼                                    ▼
            Primary model                          Fallback chain
            (best match)                           (next tier)
```

## 運用チェック

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
