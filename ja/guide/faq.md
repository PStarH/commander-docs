# FAQ

## Commander とは？

5 つの正規トポロジで複数 AI エージェントを編成するエンジンです。25 プロバイダー、18 組み込みツール、6700+ テスト。

## 普通の AI コーディングツールとの違いは？

単一エージェントではなく、**自動トポロジ・ライブ SSE・品質ゲート・本番向け基盤** を備えます。

## API キーは複数必要？

いいえ。**1 つで十分**。複数設定するとフェイルオーバーが働きます。

## オフラインは？

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## ファイルを編集する？

モードで制御: `plan` / `read-only` / `suggest` / `auto-edit` / `full-auto`。

## CI では？

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

## 5 トポロジ

SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW — [決定木](/ja/guide/usage/topology-decision-tree)

[トラブルシューティング](/ja/guide/troubleshooting) · [セキュリティ](/ja/guide/security)
