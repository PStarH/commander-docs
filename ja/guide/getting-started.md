# クイックスタート

約 5 分で Commander を動かします。API キーは 1 つ。グラフビルダーも YAML も不要です。

## 成功条件

次の **3 つすべて** が真なら完了です。

1. `pnpm install` がエラーなく終わる
2. タスクを実行し **審議 (deliberation) + トポロジ** が見える（plan または stream）
3. プロセスが結果付きで終了する（または `doctor` の明確なエラー — 無言のハングではない）

## 前提条件

- **Node.js** 18+（22 推奨）
- **pnpm** 8+（9+ 推奨 — monorepo workspaces）
- LLM API キー 1 つ（OpenAI、Anthropic、DeepSeek、Groq、…）

> **pnpm** を使ってください。npm だけではマルチパッケージ monorepo に足りません。

## 5 分チェックリスト

### 1. クローンとインストール

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

インストール後の推奨:

```bash
pnpm -r build
```

### 2. API キー

```bash
export OPENAI_API_KEY=sk-...
# または: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander はプロバイダーを **自動検出** します。一覧: [プロバイダー](/ja/guide/providers)。

### 3. Plan（ゼロリスク）

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

ファイルを変更せずに複雑度・トポロジ・エージェント配分が見えるはずです。

### 4. stream 実行

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

ライブの思考、ツール呼び出し、品質ゲートが見えるはずです。

### 5. （任意）Web コンソール

```bash
pnpm gui
```

- API: `http://localhost:4000`
- Web: 多くは `http://localhost:5173`（dev）または `http://localhost:3000`（Docker）

[Web コンソール](/ja/guide/web-console)。

### 6. （任意）Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## ビルド後: `commander` バイナリ（任意）

npm 公開が主経路になるまでは monorepo エントリを使ってください。

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

ローカル core ビルド後、workspace の bin が使える場合があります。

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## 失敗したとき

| 症状                             | 対処                                                               |
| -------------------------------- | ------------------------------------------------------------------ |
| `Provider not available`         | `echo $OPENAI_API_KEY` — **この** シェルに export。続けて `doctor` |
| `Cannot find module` / workspace | リポジトリルートで **pnpm**、`pnpm install` と `pnpm -r build`     |
| ハング / 出力なし                | まず `plan`；`COMMANDER_DEBUG=true`；ネットワーク/プロバイダー     |
| Rate limited                     | 待機、`COMMANDER_MAX_CONCURRENCY=1`、または 2 つ目のキー           |
| Circuit breaker open             | ~30 秒待つ、または `doctor --reset`                                |
| オフラインのみ                   | Ollama: `export OLLAMA_BASE_URL=http://localhost:11434`            |

詳細: [トラブルシューティング](/ja/guide/troubleshooting)。

## いま何が起きたか

1. タスクを **分類**（CODING / RESEARCH / ANALYSIS / FACTUAL）
2. トポロジを **選択**（SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW）
3. ツール付きで 1 つ以上のエージェントを **実行**
4. 5 品質ゲートで出力を **検証**

詳細: [トポロジ決定木](/ja/guide/usage/topology-decision-tree) · [アーキテクチャ](/ja/architecture/overview)。

## 次の道

| ゴール              | 移動先                                                              |
| ------------------- | ------------------------------------------------------------------- |
| 実戦レシピ          | [クックブック](/ja/guide/cookbook/)                                 |
| なぜこの枠組みか    | [なぜ Commander](/ja/guide/why-commander)                           |
| TypeScript 埋め込み | [Agent SDK](/ja/guide/sdk)                                          |
| VM へ               | [デプロイ](/ja/deployment) · [インストール](/ja/guide/installation) |
| CLI リファレンス    | [コマンド](/ja/guide/commands)                                      |
