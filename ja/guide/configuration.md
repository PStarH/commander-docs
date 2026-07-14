# 設定

環境変数と任意の `.commander.json`。

## 主要環境変数

| 変数 | 既定 | 説明 |
|------|------|------|
| `COMMANDER_MODE` | `auto-edit` | plan / read-only / auto-edit / full-auto / suggest |
| `COMMANDER_DEBUG` | `false` | 詳細ログ |
| `COMMANDER_MAX_CONCURRENCY` | `5` | 同時エージェント数 |
| `COMMANDER_TIMEOUT_MS` | `120000` | タイムアウト |
| `PORT` | `4000` | API ポート |
| `COMMANDER_API_KEY` | — | Bearer |
| `TENANT_PROVIDER` | `null` | `simple` で multi-tenant |
| `COMMANDER_SECURITY_PROFILE` | `standard` | サンドボックスプロファイル |

プロバイダーキーは [プロバイダー](/ja/guide/providers) を参照。

## `.commander.json`

```json
{
  "provider": "auto",
  "model": "auto",
  "mode": "balanced",
  "topology": "auto",
  "budget": "auto"
}
```

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts config
```
