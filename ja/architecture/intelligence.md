# Intelligence Layer

The Intelligence Layer provides internal agent capabilities that make Commander smarter over time. These are automatic systems — users see the results, not the mechanism. Estimates the cost of a task before execution using historical data from MetaLearner and deliberation estimates.

本ページは Commander における **Intelligence Layer** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();

const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
