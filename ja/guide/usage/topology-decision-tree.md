# トポロジ決定木

審議エンジンが **5 つの正規トポロジ** を選ぶ指針。[対話型エクスプローラー](/ja/guide/topology-explorer) も参照。

1. 明確な一問一答 → **SINGLE**  
2. 厳密なパイプライン A→B→C → **CHAIN**  
3. 並列スペシャリスト + 統合 → **DISPATCH**  
4. 委任・再計画が必要 → **ORCHESTRATOR**  
5. 高リスク / 批評が必要 → **REVIEW**  

```bash
npx tsx packages/core/src/cliEntry.ts plan "your real task"
npx tsx packages/core/src/cliEntry.ts run "task" --topology review --stream
```

名前: `single` · `chain` · `dispatch` · `orchestrator` · `review`。

[マルチエージェント](/ja/architecture/multi-agent)
