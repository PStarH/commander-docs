# Web Console

The Web Console is Commander's visual control surface: chat with streaming agents, live topology, governance, and ops views.

## Start

### Dev (monorepo)

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...   # or other provider
pnpm gui
```

| Service | Typical URL |
|---------|-------------|
| API | http://localhost:4000 |
| Web (Vite dev) | http://localhost:5173 |

`pnpm gui` starts API + Web and tries to open the browser.

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

| Service | URL |
|---------|-----|
| API | http://localhost:4000 |
| Web (Nginx) | http://localhost:3000 |

## What you get

| Area | Purpose |
|------|---------|
| **Dashboard** | Battle report, token trends, live topology, agent roster, mission board |
| **Chat** | Conversational runs with real-time agent streaming |
| **Governance** | Approval queue, policy configuration, audit log |
| **DLQ** | Dead letter queue inspect + replay |
| **Security** | Compliance / posture views (ISO 42001 / NIST AI RMF oriented) |
| **Execution** | Live execution feed, hallucination risk panel |
| **Agents** | Roster + lineage tree |

Exact labels may evolve with the `apps/web` package — treat this as the product map, not a pixel-perfect UI spec.

## Health checks

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Auth

If `COMMANDER_API_KEY` is set, API clients (including the console) must send:

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

Never commit the key. Rotate if leaked.

## When to use Console vs CLI

| Use Console when… | Use CLI when… |
|-------------------|---------------|
| You want visual topology and approvals | Scripts, CI, SSH-only hosts |
| Debugging long multi-agent runs | One-shot `plan` / `run --stream` |
| Ops (DLQ, audit) | Automation and packaging |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Blank UI | Confirm API is up on `:4000`; check browser console CORS |
| 401 | Set matching `COMMANDER_API_KEY` on API and client |
| No models | Export a provider key in the shell that started `pnpm gui` |
| Port conflict | Stop other services on 4000/5173/3000 |

More: [Troubleshooting](/guide/troubleshooting) · [Deployment](/deployment).

## Related

- [Quick Start](/guide/getting-started)  
- [Installation](/guide/installation)  
- [Agent SDK](/guide/sdk) (programmatic alternative)  
