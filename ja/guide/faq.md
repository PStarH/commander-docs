# FAQ

## Commander とは？

5 つの正規トポロジで複数 AI エージェントを編成するエンジンです。25 プロバイダー、18 組み込みツール。

## 普通の AI コーディングツールとの違いは？

単一エージェントではなく、**自動トポロジ・ライブストリーム・品質ゲート・本番向け基盤** を備えます。

## オープンソース？

はい、MIT。

## API キーは複数必要？

いいえ。**1 つで十分**。複数設定するとフェイルオーバーが働きます。

## オフラインは？

Ollama / vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## CI で使える？

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

詳細は [英語 FAQ](/guide/faq)。
