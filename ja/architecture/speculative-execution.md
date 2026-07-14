# Speculative Execution

Commander implements **PASTE-style speculative execution** (Pattern-Aware Speculative Execution) that pre-executes likely tool calls during LLM thinking time. Research shows this achieves up to 48.5% reduction in task completion time. During LLM thinking/processing time, Commander predicts the most likely next tool calls based on observed patterns and pre-executes them. If the model actually makes

本ページは Commander における **Speculative Execution** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                         ┌─────────────────────────────┘
                         ▼
               ┌──────────────────┐
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
