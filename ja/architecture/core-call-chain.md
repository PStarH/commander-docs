# コア呼び出しチェーン

Every Commander execution follows a structured pipeline: The deliberation engine analyzes the task's complexity, dependency graph, and domain requirements to determine the optimal execution strategy.

本ページは Commander における **コア呼び出しチェーン** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
CLI / HTTP / API
  │
  ├─ deliberation.ts     ← "What kind of task is this?"
  │   └─ TaskComplexityAnalyzer
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
