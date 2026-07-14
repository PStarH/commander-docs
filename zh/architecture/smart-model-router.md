# 智能模型路由

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/smart-model-router)



The Smart Model Router provides **capability-based model selection** with user-configurable routing rules. It wraps the core `ModelRouter` with an extended API for defining model pools, routing rules, and budget constraints.

## Capabilities


Models are tagged with capability types for matching:

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

## 配置


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

## Routing Modes


| Mode | Behavior |
|------|----------|
| `auto` | Router selects best model based on task requirements and budget |
| `manual` | Use only the `defaultModel` — no automatic selection |
| `cascade` | Try models in tier order (eco → standard → power), failover on error |

## Model Tiers


| Tier | Description | Examples |
|------|-------------|---------|
| `eco` | Cheapest, fastest, good for simple tasks | DeepSeek, Groq |
| `standard` | Balanced cost/quality | GPT-4o-mini, Claude Haiku |
| `power` | Highest quality, most expensive | GPT-4o, Claude Sonnet |
| `consensus` | Used for multi-model voting | Any tier |

## Routing Decision


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

## Programmatic API


```typescript
// Get routing decision for a task
const decision = router.route({
  taskType: 'code_generation',
  requiredCapabilities: ['code', 'function_calling'],
  estimatedTokens: 5000,
});

console.log(`Selected: ${decision.modelId}`);
console.log(`Tier: ${decision.tier}`);
console.log(`Estimated cost: $${decision.estimatedCost}`);

// List available models for a capability set
const models = router.listModels({
  capabilities: ['code', 'reasoning'],
  tier: 'power',
});

// Check budget status
const budget = router.getBudgetStatus();
console.log(`Daily spend: $${budget.spent} / $${budget.limit}`);
```

## Integration with Deliberation


The Smart Model Router integrates with the deliberation engine to select the optimal model for each agent in a multi-agent run:

```
Deliberation → Topology Selection → Agent Count → Per-Agent Model Selection
                                                        │
                                                        ▼
                                                SmartModelRouter
                                                (capability matching)
```
