# トポロジ探索

5 正規トポロジを比較し、タスク種に合う選択をするためのガイドです。

## 一覧

| トポロジ | 一言 | エージェント目安 |
|----------|------|------------------|
| **SINGLE** | 1 エージェントが全体 | 1 |
| **CHAIN** | 順次パイプライン | 2–3 |
| **DISPATCH** | 独立並列 + 合成 | 2–10 |
| **ORCHESTRATOR** | リードが委譲 | 3–8 |
| **REVIEW** | 生成→批評→洗練 | 2–5 |

## 強制

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology dispatch
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

自動選択は審議・複雑度スコアに従います。[トポロジ決定木](/ja/guide/usage/topology-decision-tree)。

## 関連

- [マルチエージェント](/ja/architecture/multi-agent)  
- [なぜ Commander](/ja/guide/why-commander)  
- [クックブック](/ja/guide/cookbook/)  
