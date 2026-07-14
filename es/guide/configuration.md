# Configuración

Commander se configura con variables de entorno y un archivo de proyecto opcional.

## Variables de entorno

### Core

| Variable | Default | Descripción |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Logging verbose |
| `COMMANDER_LOG_LEVEL` | `info` | `debug`, `info`, `warn`, `error` |
| `COMMANDER_MAX_CONCURRENCY` | `5` | Máx. ejecuciones concurrentes de agentes |
| `COMMANDER_TIMEOUT_MS` | `120000` | Timeout por defecto (ms) |

### Servidor

| Variable | Default | Descripción |
|----------|---------|-------------|
| `PORT` | `4000` | Puerto HTTP |
| `HOST` | `0.0.0.0` | Host HTTP |
| `CORS_ORIGIN` | `*` | Orígenes CORS |
| `RATE_LIMIT_WINDOW_MS` | `60000` | Ventana de rate limit |
| `RATE_LIMIT_MAX` | `100` | Máx. requests por ventana |

### Multi-tenant y seguridad

| Variable | Default | Descripción |
|----------|---------|-------------|
| `TENANT_PROVIDER` | `null` | `null` o `simple` |
| `COMMANDER_SECURITY_PROFILE` | `standard` | `strict`, `standard`, `permissive`, `hardened` |
| `COMMANDER_API_KEY` | — | Bearer del API server |

### Proveedores

Cualquier key de la [lista de proveedores](/es/guide/providers) (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, …).

## Archivo `.commander.json`

En la raíz del proyecto:

```json
{
  "provider": "auto",
  "model": "auto",
  "mode": "balanced",
  "topology": "auto",
  "budget": "auto",
  "mcpServers": []
}
```

| Campo | Default | Descripción |
|-------|---------|-------------|
| `provider` | `auto` | Proveedor LLM primario |
| `model` | `auto` | Modelo |
| `mode` | `balanced` | `fast`, `balanced`, `thorough` |
| `topology` | `auto` | `auto`, `single`, `chain`, `dispatch`, `orchestrator`, `review` |
| `budget` | `auto` | Presupuesto de tokens |

## CLI

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts config
npx tsx packages/core/src/cliEntry.ts mode read-only
```

## Relacionado

- [Proveedores](/es/guide/providers)  
- [Instalación](/es/guide/installation)  
- [Seguridad](/es/guide/security)
