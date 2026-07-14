# クックブック: CI full-auto lint

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

ルール: 捨てブランチ / PR、秘密情報最小、ローカル dry-run、ログを成果物に。main への force-push 禁止。

[FAQ](/ja/guide/faq) · [デプロイ](/ja/deployment)
