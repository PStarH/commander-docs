# 설치

## 사전 요구

- Node.js 18+  
- pnpm 8+  
- LLM API 키 하나  

## 로컬

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
```

[영문 Deployment](/deployment) · [빠른 시작](/ko/guide/getting-started)
