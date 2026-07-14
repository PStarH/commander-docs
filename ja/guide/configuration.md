# 設定

Commander は環境変数と設定ファイルで構成します。

## 環境変数

### コア

| 変数 | 既定 | 説明 |
|------|------|------|
| `COMMANDER_MODE` | `auto-edit` | `plan` / `read-only` / `auto-edit` / `full-auto` / `suggest` |
| `COMMANDER_DEBUG` | `false` | 詳細ログ |
| `COMMANDER_LOG_LEVEL` | `info` | `debug`…`error` |
| `COMMANDER_MAX_CONCURRENCY` | `5` | 同時エージェント上限 |
| `COMMANDER_TIMEOUT_MS` | `120000` | 実行タイムアウト (ms) |

### サーバー

| 変数 | 既定 | 説明 |
|------|------|------|
| `PORT` | `4000` | HTTP ポート |
| `HOST` | `0.0.0.0` | バインド |
| `CORS_ORIGIN` | `*` | CORS |
| `RATE_LIMIT_*` | — | レート制限 |

### マルチテナント · セキュリティ · 観測

| 変数 | 説明 |
|------|------|
| `TENANT_PROVIDER` | `null` または `simple` |
| `COMMANDER_API_KEY` | API Bearer |
| `COMMANDER_SECURITY_PROFILE` | サンドボックス・プロファイル |
| `COMMANDER_EVENT_SOURCING_WAL` | WAL パス |
| `OTEL_*` | OpenTelemetry |

### プロバイダー

`OPENAI_API_KEY` 等 — [プロバイダー](/ja/guide/providers)。ローカルは `OLLAMA_BASE_URL`。

## ファイル

`.commander.json` / `.env` / monorepo の `.env.example` を参照。秘密は git に入れない。

## 例

```bash
export COMMANDER_MODE=plan
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## 関連

- [インストール](/ja/guide/installation)  
- [セキュリティ](/ja/guide/security)  
- [デプロイ](/ja/deployment)  
