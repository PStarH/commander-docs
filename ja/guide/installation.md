# インストール

## 前提

- Node.js 18+  
- pnpm 8+  
- LLM API キー 1 つ  

## ローカル

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

[英語 Deployment](/deployment) · [クイックスタート](/ja/guide/getting-started)
