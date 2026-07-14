# Instalación

::: tip Monorepo primero
Commander se entrega como **monorepo** open source. Hoy el camino soportado es **clonar + pnpm**. Los paquetes npm públicos (`@commander/core`, `@commander/sdk`) **aún no** son la vía principal — no uses `pnpm add @commander/*` como checklist de éxito.
:::

## Requisitos previos

- **Node.js** 18+ (LTS recomendado)
- **pnpm** 8+ (`npm install -g pnpm`)
- Una API key de proveedor LLM (ver [Proveedores](/es/guide/providers))

## Desarrollo local

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### Consola web (dev)

```bash
# API :4000 + Web :5173 + abrir navegador
pnpm gui
```

### CLI desde el código fuente

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

Tras compilar el core (`pnpm --filter @commander/core build`), el binario `commander` queda disponible desde el paquete.

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:      http://localhost:4000
# Web GUI:  http://localhost:3000
```

El stack Docker incluye build multi-etapa multi-arquitectura, proxy Nginx, health checks, volúmenes persistentes y tini.

## Producción (VM / VPS)

```bash
cp .env.example .env.production
# Edita claves y ajustes
./scripts/deploy-vm.sh your-vm-ip --env-file .env.production

# O manualmente:
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

### Overlay de producción

| Función         | Ajuste                                   |
| --------------- | ---------------------------------------- |
| Límites CPU/RAM | 2 CPU / 4GB API, 0.5 CPU / 256MB web     |
| Logs            | driver json-file, 10MB máx, 3 rotaciones |
| Restart         | `always`                                 |
| Health checks   | intervalo 30s, timeout 10s, 5 reintentos |
| Rate limiting   | configurable por tenant                  |
| Multi-tenant    | opcional `TENANT_PROVIDER=simple`        |

## CI/CD

El pipeline (`.github/workflows/ci.yml`) corre en cada push/PR:

| Job         | Comprueba                                |
| ----------- | ---------------------------------------- |
| **quality** | TypeScript, 6700+ tests, CLI, build core |
| **docker**  | `docker compose build`                   |
| **web-gui** | build Vite de producción                 |

## Verificar instalación

```bash
curl http://localhost:4000/health
cd packages/core
npx tsx --test tests/*.test.ts
npx tsc --noEmit
```

## Siguiente

- [Inicio rápido](/es/guide/getting-started)
- [Comandos](/es/guide/commands)
- [Despliegue](/es/deployment)
