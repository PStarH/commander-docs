# Consola web

La consola web es la superficie visual de Commander: chat con agentes en streaming, topología en vivo, gobernanza y vistas de ops.

## Arranque

### Dev (monorepo)

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
pnpm gui
```

| Servicio | URL típica |
|----------|------------|
| API | http://localhost:4000 |
| Web (Vite dev) | http://localhost:5173 |

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

| Servicio | URL |
|----------|-----|
| API | http://localhost:4000 |
| Web (Nginx) | http://localhost:3000 |

## Qué obtienes

| Área | Propósito |
|------|-----------|
| **Dashboard** | Informe de batalla, tokens, topología en vivo, roster de agentes |
| **Chat** | Ejecuciones conversacionales con stream en tiempo real |
| **Governance** | Cola de aprobaciones, políticas, auditoría |
| **DLQ** | Cola de cartas muertas: inspeccionar y reenviar |
| **Security** | Postura de cumplimiento (orientada ISO 42001 / NIST AI RMF) |
| **Execution** | Feed de ejecución, panel de riesgo de alucinación |
| **Agents** | Roster y árbol de linaje |

Las etiquetas exactas pueden evolucionar con `apps/web`.

Rutas en vivo (paquete `apps/web`): `/`, `/agents`, `/missions`, `/execution`, `/memory`, `/governance`, `/security`, `/slo`, `/chat`, `/dlq`, `/audit`, `/cost`, `/knowledge`, `/alerts`, `/onboarding`, `/users`, `/settings`, `/settings/sso`, `/workflows`, `/poc`, `/research` y `/actions` (Action Gateway).

## Health checks

Servidor de salud ops — puerto por defecto `8081`, override con `COMMANDER_OPS_HEALTH_PORT`:

```bash
curl http://localhost:8081/health   # → 200 {"status":"ok"}
curl http://localhost:8081/ready    # → 200 (ready) / 503 (fail-closed)
```

El cliente console usa la base de API en `:4000` (por defecto, `VITE_API_BASE_URL`).

## Auth

La consola firma las peticiones API con un token bearer persistido en `localStorage` bajo `commander.auth.token`. Cuando hay token, un interceptor fetch global añade:

```http
Authorization: Bearer <token>
```

Una respuesta `401` borra el token almacenado y notifica a la app para re-autenticar. Nunca subas tokens al git; rótalos si se filtran.

## Consola vs CLI

| Usa la consola cuando… | Usa la CLI cuando… |
|------------------------|--------------------|
| Quieres topología visual y aprobaciones | Scripts, CI, solo SSH |
| Depuras runs largos multi-agente | `plan` / `run --stream` de un disparo |
| Ops (DLQ, auditoría) | Automatización y empaquetado |

## Solución de problemas

| Problema | Arreglo |
|----------|---------|
| UI en blanco | Confirma API en `:4000`; CORS en la consola del navegador |
| 401 | Re-autentícate en la consola — el token almacenado se borra automáticamente |
| Sin modelos | Exporta la key del proveedor en la shell que lanzó `pnpm gui` |
| Puerto ocupado | Libera 4000/5173/3000 |

Más: [Solución de problemas](/es/guide/troubleshooting) · [Despliegue](/es/deployment).
