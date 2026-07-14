# Self-Evolution

Commander improves over time through a meta-learning system that tunes agent configurations based on execution outcomes. The system combines Thompson Sampling and Reflexion to optimize topology selection, provider choice, and parameter settings. Uses Thompson Sampling with Beta distributions to balance exploration and exploitation:

本ページは Commander における **Self-Evolution** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Execution completes
  │
  ├─ TrajectoryAnalyzer       ← Analyze execution patterns
  │   └─ Extract features: duration, tokens, success rate
  │
  ├─ MetaLearner              ← Thompson Sampling
  │   └─ Update Beta distributions per arm
  │
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
