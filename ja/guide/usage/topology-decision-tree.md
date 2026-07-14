# トポロジ決定木

どの編成トポロジを使うか迷ったら、この木に従ってください。

## クイック参照

```
タスクは単純で明確か？
├── YES → SINGLE
└── NO  → サブタスクは独立か？
    ├── YES → DISPATCH
    └── NO  → 互いに依存するか？
        ├── YES → CHAIN
        └── NO  → 明確なリードがあるか？
            ├── YES → ORCHESTRATOR
            └── NO  → REVIEW
```

## 詳細

| トポロジ     | いつ                     | エージェント目安 |
| ------------ | ------------------------ | ---------------- |
| SINGLE       | 単純・範囲明確           | 1                |
| CHAIN        | 前段依存の多段変換       | 2–3              |
| DISPATCH     | 並列可能な独立サブタスク | 2–10             |
| ORCHESTRATOR | 分解パスがある複雑タスク | 3–8              |
| REVIEW       | 高リスク・交差検証       | 2–5              |

## 複雑度スコア

| スコア |   自動選択   |
| :----: | :----------: |
|  0–20  |    SINGLE    |
| 20–40  |    CHAIN     |
| 40–60  |   DISPATCH   |
| 60–80  | ORCHESTRATOR |
| 80–100 |    REVIEW    |

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## 関連

- [マルチエージェント](/ja/architecture/multi-agent)
- [トポロジ探索](/ja/guide/topology-explorer)
- [タスク実行](/ja/guide/usage/running-tasks)
