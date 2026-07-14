# 安装

::: tip 优先 monorepo
Commander 以开源 **monorepo** 交付。当前支持的安装路径是 **clone + pnpm**。公开 npm 包（`@commander/core`、`@commander/sdk`）**尚不是**主路径 — 不要把 `pnpm add @commander/*` 当成快速成功标准。
:::

## 前置

- **Node.js** 18+（推荐 LTS）
- **pnpm** 8+（`npm install -g pnpm`）
- 一把 LLM API Key（见 [Providers](/guide/providers)）

## 本地开发

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### Web 控制台

```bash
pnpm gui
# API :4000 · Web 开发态多为 :5173
```

### 源码 CLI

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API: http://localhost:4000
# Web: http://localhost:3000
```

## 生产（VM）

```bash
cp .env.example .env.production
# 编辑密钥
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
# 或
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

## 验证

```bash
curl http://localhost:4000/health
cd packages/core && npx tsx --test tests/*.test.ts
```

## 更多

- [快速开始](/zh/guide/getting-started)
- [英文 Deployment](/deployment)
