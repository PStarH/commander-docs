# トポロジ決定木

Not sure which orchestration topology to use? Follow this decision tree. **When**: Simple, well-scoped tasks

本ページは Commander における **トポロジ決定木** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Is the task simple and well-defined?
├── YES → SINGLE
└── NO  → Are subtasks independent?
    ├── YES → DISPATCH
    └── NO  → Do subtasks depend on each other?
        ├── YES → CHAIN
        └── NO  → Is there a clear lead agent?
            ├── YES → ORCHESTRATOR
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
