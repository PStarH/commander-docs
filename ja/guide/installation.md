# Installation

**Installation.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

::: tip Monorepo first

## 参照表

| Feature           | Setting                                     |
| ----------------- | ------------------------------------------- |
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web        |
| Logging           | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy    | `always` (auto-restart)                     |
| Health checks     | 30s interval, 10s timeout, 5 retries        |
| Rate limiting     | Configurable per-tenant window/max          |
| Multi-tenancy     | Optional `TENANT_PROVIDER=simple`           |


## 主な節

### Prerequisites

**Prerequisites** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Local development (recommended)

**Local development (recommended)** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Docker

**Docker** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Production (VM / VPS)

**Production (VM / VPS)** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### CI/CD

**CI/CD** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Verify installation

**Verify installation** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Next

**Next** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```
```bash
# API :4000 + Web :5173 + open browser
pnpm gui
```

## 運用チェック

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
