# SDKs and API

> This page is synchronized from the canonical English documentation. 简体中文 navigation is available; commands and product limits are identical in every locale.

## CLI and HTTP API

The Local CLI is the primary supported interface. For local server use, the API
base URL is `http://localhost:4000`. The `/v1` Gateway is alpha.

## Python SDK

The Python package contains both a legacy client and a Gateway client. Use the
Gateway client with `COMMANDER_API_URL=http://127.0.0.1:4000` for the current
server path. Do not use port `3001` as a Commander API endpoint; that port is
reserved for Grafana in the observability profile.

Confirm supported endpoints in the running server's OpenAPI document:

```bash
curl http://localhost:4000/openapi.json
```

Treat legacy API material as a compatibility-only implementation detail, not a
public integration contract.