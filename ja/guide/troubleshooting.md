# トラブルシューティング

> monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## プロバイダー不可

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

## レート制限 / タイムアウト

- 待機、`COMMANDER_MAX_CONCURRENCY=1`、2 つ目のキー  
- `COMMANDER_TIMEOUT_MS=120000`  

## ハング / サーキットブレーカー

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## デバッグ

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task"
```

[FAQ](/ja/guide/faq) · [Issues](https://github.com/PStarH/Commander/issues)
