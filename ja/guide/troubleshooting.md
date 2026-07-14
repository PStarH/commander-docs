# トラブルシューティング

よくある問題と対処。

> **CLI:** monorepo チェックアウトでは  
> `npx tsx packages/core/src/cliEntry.ts <command>`  
> `@commander/core` ビルド後は `commander <command>`。

## インストール

### `pnpm install` 失敗

```bash
pnpm install
pnpm build
```

リポジトリ **ルート** で全 workspace を入れてください。

### インストール後の TypeScript エラー

```bash
pnpm build
npx tsc --noEmit
```

## プロバイダー

### Provider not available

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

キーは **今のシェル** に export されている必要があります。

### Rate limited

- 待って再試行（自動 backoff）
- 複数プロバイダー fallback
- `export COMMANDER_MAX_CONCURRENCY=1`

### Timeout

- ネットワーク / プロバイダー
- より速いプロバイダー（Groq, Together）
- `export COMMANDER_TIMEOUT_MS=120000`

## 実行

### ハング

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor
```

### Circuit breaker open

~30 秒待つか:

```bash
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

### 結果がおかしい

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Docker

```bash
docker info
docker compose build --no-cache
```

## デバッグ

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 関連

- [クイックスタート](/ja/guide/getting-started)
- [インストール](/ja/guide/installation)
- [プロバイダー](/ja/guide/providers)
