# Plan モード

Plan モードは、Commander が **実際に動く前に** 何をするかを見せます。実行戦略・エージェント配分・ツール呼び出しをゼロリスクで確認できます。

## なぜ使うか

- **安全** — ファイル変更前に計画をレビュー  
- **学習** — 分解とアプローチを理解  
- **デバッグ** — トポロジ・エージェント・ツールを確認  
- **協働** — チームで計画を共有・反復  

## 使い方

> monorepo ソース。ビルド後は `commander` に置き換え可。

```bash
npx tsx packages/core/src/cliEntry.ts mode plan
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# 一回だけ
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## 出力の例

```
┃ → Deliberating task...
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃ → Subtasks: ...
┃ → Estimated duration: 45s
```

ファイルは変更されません。問題なければ `suggest` / `auto-edit` で本実行します。

## 関連

- [タスク実行](/ja/guide/usage/running-tasks)  
- [Watch モード](/ja/guide/usage/watch-mode)  
- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)  
