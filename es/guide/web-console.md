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

## Health checks

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Auth

Si `COMMANDER_API_KEY` está definida, los clientes deben enviar:

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

Nunca subas la key al git. Rótala si se filtra.

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
| 401 | Misma `COMMANDER_API_KEY` en API y cliente |
| Sin modelos | Exporta la key del proveedor en la shell que lanzó `pnpm gui` |
| Puerto ocupado | Libera 4000/5173/3000 |

Más: [Solución de problemas](/es/guide/troubleshooting) · [Despliegue](/es/deployment).
