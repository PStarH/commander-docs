# Configuration

Commander is configured through environment variables and configuration files.

## Environment Variables

### Core

| Variable | Default | Description |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | Approval mode: `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Enable verbose debug logging |
| `COMMANDER_LOG_LEVEL` | `info` | Log level: `debug`, `info`, `warn`, `error` |

### Server

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `4000` | HTTP server port |
| `HOST` | `0.0.0.0` | HTTP server host |
| `CORS_ORIGIN` | `*` | CORS allowed origins |
| `RATE_LIMIT_WINDOW_MS` | `60000` | Rate limit window (ms) |
| `RATE_LIMIT_MAX` | `100` | Max requests per window |

### Multi-Tenancy

| Variable | Default | Description |
|----------|---------|-------------|
| `TENANT_PROVIDER` | `null` | `null` (single-tenant) or `simple` (multi-tenant) |
| `TENANT_PROVIDER_CONFIG` | — | JSON config for tenant mapping |

## CLI Configuration

Commander supports a `.commander.json` config file in your project root:

```json
{
  "defaultProvider": "openai",
  "maxTokens": 100000,
  "topology": "auto",
  "approvalMode": "auto-edit",
  "theme": "dark",
  "customTools": ["./tools/my-tool.ts"]
}
```

## Provider Config

Set **any single** provider key. Commander auto-detects and chains fallbacks:

```bash
export OPENAI_API_KEY=sk-...        # Primary: OpenAI | Fallback: DeepSeek → GLM → MiMo
export ANTHROPIC_API_KEY=sk-ant-... # Anthropic Claude
export GOOGLE_API_KEY=...           # Google Gemini
```

See the full [providers list](/guide/providers).
