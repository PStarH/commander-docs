# Agent Transaction Runtime (ATR)

**Agent Transaction Runtime (ATR).** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Setting | Default | Description |
|---------|---------|-------------|
| `idempotency.ttlSeconds` | `3600` | How long to retain idempotency records |
| `lease.ttlMs` | `30000` | Lease time-to-live |
| `lease.heartbeatMs` | `5000` | Heartbeat interval |
| `compensation.timeoutMs` | `10000` | Max time per compensation handler |


## 主な節

### Why ATR

**Why ATR** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Core Concepts

**Core Concepts** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### GitHub Adapter

**GitHub Adapter** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### HTTP API

**HTTP API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Configuration

**Configuration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Architecture

**Architecture** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```
Agent Decision → ATR Settlement Layer → External System
                    ├── Idempotency (no duplicates)
                    ├── Recovery (compensable rollback)
                    ├── Leasing (single-owner runs)
                    └── Fencing (zombie process protection)
```
```
PENDING → EXECUTING → VERIFYING → COMMITTED
               │            │
               │            └──→ ABORTED → COMPENSATED
               └───────────────────→ ABORTED → COMPENSATED
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
