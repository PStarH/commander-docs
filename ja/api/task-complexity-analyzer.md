# Task Complexity Analyzer

タスクをスコアし、推奨トポロジを返します。審議（deliberation）の中核です。

## 概念

```typescript
import { TaskComplexityAnalyzer } from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

// complexity.score, complexity.recommendedTopology, …
```

スコア帯の目安（自動選択）:

| スコア | トポロジ |
|:------:|:--------:|
| 0–20 | SINGLE |
| 20–40 | CHAIN |
| 40–60 | DISPATCH |
| 60–80 | ORCHESTRATOR |
| 80–100 | REVIEW |

## CLI で見る

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
```

## 関連

- [API 概要](/ja/api/overview)  
- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)  
- [コア呼び出しチェーン](/ja/architecture/core-call-chain)  
