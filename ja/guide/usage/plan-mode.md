# プランモード

Commander が **実行前に何をするか** を確認できます。ファイル変更のリスクなしに、戦略・エージェント・tools をレビューします。

## なぜ使うか

- **安全** — 変更前に計画を確認  
- **学習** — タスク分解の理解  
- **デバッグ** — 予定トポロジ / agents / tools  
- **共有** — チームと計画をレビュー  

## 使い方

```bash
npx tsx packages/core/src/cliEntry.ts mode plan
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## 出力例

```
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
```

プランモード中はターミナルに表示インジケータが出ます。

## 関連

- [タスク実行](/ja/guide/usage/running-tasks)  
- [トポロジエクスプローラー](/ja/guide/topology-explorer)
