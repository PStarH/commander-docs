# 설치

## 사전 요구

- Node.js 18+ (22 권장)  
- pnpm 8+  
- LLM API 키 하나  

## 로컬

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## 웹 콘솔 · Docker

```bash
pnpm gui
# API :4000 · Web :5173

export COMMANDER_API_KEY="your-secret-key"
docker compose up -d
# API :4000 · Web :3000
```

```bash
curl http://localhost:4000/health
```

[빠른 시작](/ko/guide/getting-started)
