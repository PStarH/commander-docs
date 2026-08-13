# クイックスタート

約 5 分で Commander を動かします。API キーは 1 つ。グラフビルダーも YAML も不要です。

## 成功条件

1. `pnpm install` がエラーなく終わる  
2. タスクを実行し **審議 (deliberation) + トポロジ** が見える  
3. プロセスが正常終了する（または `doctor` が明確なエラーを返す）

## 前提条件

- **Node.js** 18+（22 推奨）  
- **pnpm** 8+（9+ 推奨）  
- いずれか 1 つの LLM API キー  

> monorepo のため **pnpm** を使ってください。

## 5 分チェックリスト

### 1. クローンとインストール

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### 2. API キー

```bash
export OPENAI_API_KEY=sk-...
# または ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

### 3. plan（安全）

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

### 4. stream 実行

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

### 5. Web コンソール（任意）

```bash
pnpm gui
# API :4000 · Web 開発時は多くが :5173
```

### 6. Docker（任意）

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

## 失敗したら

| 症状 | 対処 |
|------|------|
| Provider not available | 現在の shell で key を `export`、`doctor` を実行 |
| モジュール解決エラー | リポジトリルートで pnpm install / build |
| ハング | まず `plan`、`COMMANDER_DEBUG=true` |
| オフライン | `export OLLAMA_BASE_URL=http://localhost:11434` |

## 次へ

- [なぜ Commander か](/ja/guide/why-commander)  
- [英語ドキュメント全文](/guide/getting-started)  
- [アーキテクチャ](/ja/architecture/overview)  
