# Configuration

**Configuration.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Variable | Default | Description |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | Approval mode: `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Enable verbose debug logging |
| `COMMANDER_LOG_LEVEL` | `info` | Log level: `debug`, `info`, `warn`, `error` |
| `COMMANDER_LOG_PERSIST` | `false` | Enable log persistence to disk (auto-degrades to Error-only when backlog >10000) |
| `COMMANDER_MAX_CONCURRENCY` | `5` | Maximum concurrent agent executions |
| `COMMANDER_TIMEOUT_MS` | `120000` | Default execution timeout (ms) |


## 主な節

### Environment Variables

**Environment Variables** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### CLI Configuration

**CLI Configuration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Provider Config

**Provider Config** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```json
{
  "provider": "auto",
  "model": "auto",
  "mode": "balanced",
  "topology": "auto",
  "budget": "auto",
  "mcpServers": [],
  "a2a": {
    "server": {
      "enabled": false,
      "port": 3002,
      "host": "127.0.0.1"
    },
    "remoteAgents": []
  }
}
```
```bash
export OPENAI_API_KEY=sk-...        # Primary: OpenAI | Fallback: DeepSeek → GLM → MiMo
export ANTHROPIC_API_KEY=sk-ant-... # Anthropic Claude
export GOOGLE_API_KEY=...           # Google Gemini
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
