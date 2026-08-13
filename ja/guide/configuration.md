# 設定

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/configuration)



Commander is configured through environment variables and configuration files.

## Environment Variables


### Core


| Variable | Default | Description |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | Approval mode: `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Enable verbose debug logging |
| `COMMANDER_LOG_LEVEL` | `info` | Log level: `debug`, `info`, `warn`, `error` |
| `COMMANDER_LOG_PERSIST` | `false` | Enable log persistence to disk (auto-degrades to Error-only when backlog >10000) |
| `COMMANDER_MAX_CONCURRENCY` | `5` | Maximum concurrent agent executions |
| `COMMANDER_TIMEOUT_MS` | `120000` | Default execution timeout (ms) |

### Server


| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `4000` | HTTP server port |
| `HOST` | `0.0.0.0` | HTTP server host |
| `CORS_ORIGIN` | `*` | CORS allowed origins |
| `RATE_LIMIT_WINDOW_MS` | `60000` | Rate limit window (ms) |
| `RATE_LIMIT_MAX` | `100` | Max requests per window |

### マルチテナンシー


| Variable | Default | Description |
|----------|---------|-------------|
| `TENANT_PROVIDER` | `null` | `null` (single-tenant) or `simple` (multi-tenant) |
| `TENANT_PROVIDER_CONFIG` | — | JSON config for tenant mapping |

### セキュリティ


| Variable | Default | Description |
|----------|---------|-------------|
| `COMMANDER_SECURITY_PROFILE` | `standard` | Sandbox profile: `strict`, `standard`, `permissive`, `hardened` |
| `COMMANDER_EVENT_SOURCING_WAL` | `.commander_state/event-sourcing.wal` | Event sourcing WAL file path |
| `WARROOM_STORAGE` | `memory` | War Room storage backend: `memory` or `sqlite` |

### Observability


| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OpenTelemetry OTLP endpoint |
| `OTEL_SERVICE_NAME` | `commander` | OpenTelemetry service name |

## CLI Configuration


Commander supports a `.commander.json` config file in your project root:

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

| Field | Default | Description |
|-------|---------|-------------|
| `provider` | `auto` | Primary LLM provider |
| `model` | `auto` | Model name |
| `mode` | `balanced` | Execution mode: `fast`, `balanced`, `thorough` |
| `topology` | `auto` | Orchestration topology: `auto`, `single`, `chain`, `dispatch`, `orchestrator`, `review` |
| `budget` | `auto` | Token budget (integer ≥1000 or `auto`) |
| `mcpServers` | `[]` | MCP server configurations |
| `a2a` | — | Agent-to-Agent server and remote agent config |

API keys are never stored in the config file — they remain in environment variables or system keychain.

## Provider Config


Set **any single** provider key. Commander auto-detects and chains fallbacks:

```bash
export OPENAI_API_KEY=sk-...        # Primary: OpenAI | Fallback: DeepSeek → GLM → MiMo
export ANTHROPIC_API_KEY=sk-ant-... # Anthropic Claude
export GOOGLE_API_KEY=...           # Google Gemini
```

See the full [providers list](/ja/guide/providers).
