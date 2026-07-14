# よくある質問 (FAQ)

## 一般

### Commander とは？

マルチエージェント編成エンジンです。5 正規トポロジ（SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW）、25 LLM プロバイダー、18 組み込みツール。

### 他の AI コーディングツールとの違いは？

多くは単一エージェント・単一モデル。Commander は **複数エージェント** を **トポロジ** で編成し、複雑度から戦略を選びます。ブレーカー・マルチテナント・WAL・Prometheus・SSE など本番志向。

### オープンソース？

はい。MIT。

### マルチエージェント編成とは？

1 タスクに複数 AI エージェントを走らせ、並列・レビュー・リード委譲などで協力させることです。

## セットアップ

### API キーは複数必要？

いいえ。**1 つで十分**。`OPENAI_API_KEY` 等を設定すれば自動検出。複数キーでフェイルオーバー。

### オフラインは？

Ollama / vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### npm は？

公開は **進行中**。今は monorepo を clone。[Agent SDK](/ja/guide/sdk)。

## 使い方

### ファイルを編集する？

既定は可能。承認モードで制御: `plan` / `read-only` / `suggest` / `auto-edit` / `full-auto`。

### CI/CD？

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

### エージェント数？

1–20。単純は 1、複雑はチーム。

### 5 トポロジ？

SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW。[トポロジ決定木](/ja/guide/usage/topology-decision-tree)。

## 関連

- [なぜ Commander](/ja/guide/why-commander)  
- [クイックスタート](/ja/guide/getting-started)  
- [クックブック](/ja/guide/cookbook/)  
- [トラブルシューティング](/ja/guide/troubleshooting)  
