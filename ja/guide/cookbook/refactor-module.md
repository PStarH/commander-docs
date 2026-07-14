# クックブック: 安全なモジュールリファクタ

```bash
git checkout -b chore/commander-refactor
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module; keep public API stable"
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module; keep public API stable" --stream
git diff && pnpm test
```

チェック: プラン妥当 · diff が意図範囲 · テスト緑 · git で戻せる。

[プランモード](/ja/guide/usage/plan-mode)
