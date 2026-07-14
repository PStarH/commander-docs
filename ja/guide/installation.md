# インストール

::: tip モノレポ優先
Commander はオープンソース **モノレポ** として提供されます。現在サポートされる導入は **clone + pnpm** です。公開 npm（`@commander/core` / `@commander/sdk`）はまだ主経路ではありません。
:::

## 前提

- **Node.js** 18+（22 推奨）  
- **pnpm** 8+  
- LLM API キー 1 つ  

## ローカル

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Web コンソール

```bash
pnpm gui
# API :4000 · Web 開発は多くが :5173
```

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## ビルド後のバイナリ

```bash
pnpm --filter @commander/core build
# workspace の bin パスに commander が出る場合あり
```

## 検証

```bash
curl http://localhost:4000/health
npx tsx packages/core/src/cliEntry.ts doctor
```

## 次へ

- [クイックスタート](/ja/guide/getting-started)  
- [コマンド](/ja/guide/commands)  
- [デプロイ](/ja/deployment)  
