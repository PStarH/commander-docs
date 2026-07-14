# Deployment

**Deployment.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Feature | Setting |
|---------|---------|
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web |
| Logging | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy | `always` (auto-restart) |
| Health checks | 30s interval, 10s timeout, 5 retries |
| Rate limiting | Configurable per-tenant window/max |
| Multi-tenancy | Optional `TENANT_PROVIDER=simple` with static config |


## 主な内容

### Local (Docker Compose)

運用では **Local (Docker Compose)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/deployment)を参照してください。

### Production (VM / VPS)

運用では **Production (VM / VPS)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/deployment)を参照してください。

### Observability Stack

運用では **Observability Stack** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/deployment)を参照してください。

### Configuration Reference

運用では **Configuration Reference** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/deployment)を参照してください。

## 例（コードは英語のまま）

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:     http://localhost:4000
# Web GUI: http://localhost:3000   (Docker / Nginx)
# Dev GUI: http://localhost:5173   (pnpm gui, no Docker)
```

```bash
# 1. Configure environment
cp .env.example .env.production
# Edit .env.production with your API keys and settings

# 2. Deploy to any Linux VM with Docker
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production
```

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

## 運用

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
