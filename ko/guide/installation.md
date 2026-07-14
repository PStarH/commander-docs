# 설치

::: tip 모노레포 우선
Commander는 오픈소스 **모노레포**로 제공됩니다. 현재 지원 경로는 **clone + pnpm**입니다. 공개 npm 패키지(`@commander/core`, `@commander/sdk`)는 아직 주 경로가 아닙니다 — `pnpm add @commander/*`를 성공 기준으로 쓰지 마세요.
:::

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
