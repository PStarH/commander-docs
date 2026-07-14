# インテリジェンス層

インテリジェンス層は、Commander を時間とともに賢くする **内部の自動システム** です。ユーザーは仕組みではなく結果を見ます。

## 構成要素

| コンポーネント | 役割 | ユーザーが見るもの |
|----------------|------|--------------------|
| **Cost Predictor** | 実行前のコスト見積もり | 「約 $0.09、続けますか？」 |
| **Failure Pattern Learner** | 過去の失敗から学習 | 「この問題は以前にも」 |
| **Impact Analyzer** | 変更の副作用予測 | 「3 ファイルに影響」 |
| **Skill Extractor** | 成功パターン抽出 | 「再利用用に保存」 |

## Cost Predictor

```typescript
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();
const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
  agentCount: 4,
});

console.log(`Estimated cost: $${estimate.estimatedCostUsd}`);
```

内訳例: Deliberation · Execution · Synthesis · Quality Gates。

## Failure Pattern Learner

```typescript
import { getFailurePatternLearner } from '@commander/core';

const learner = getFailurePatternLearner();
const warnings = learner.checkPatterns({
  task: 'deploy to production',
  context: 'after database migration',
});
```

## Impact · Skill

変更範囲の推定、成功パターンのスキル化。いずれも審議・トポロジ選択にフィードバックされます。

## 運用

コストを厳しくしたい場合は予算と承認モードを使います。

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the auth module"
```

## 関連

- [Self-evolution](/ja/architecture/self-evolution)  
- [Token budget allocator](/ja/api/token-budget-allocator)  
- [Reflection engine](/ja/api/reflection-engine)  
