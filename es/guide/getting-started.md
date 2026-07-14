# Inicio rápido

Pon Commander en marcha en unos cinco minutos. Una sola API key. Sin constructores de grafos. Sin YAML.

## Criterios de éxito

Has terminado cuando se cumplen **las tres**:

1. `pnpm install` termina sin errores  
2. Ejecutaste una tarea y viste **deliberación + topología** (plan o stream)  
3. El proceso salió con un resultado (o un error claro de `doctor`, no un cuelgue silencioso)

## Requisitos previos

- **Node.js** 18+ (se recomienda 22)  
- **pnpm** 8+ (preferible 9+ — monorepo con workspaces)  
- Cualquier API key de un proveedor LLM (OpenAI, Anthropic, DeepSeek, Groq, …)

> Usa **pnpm**, no solo npm: este proyecto es un monorepo multipaquete.

## Lista de 5 minutos

### 1. Clonar e instalar

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

Opcional pero recomendado:

```bash
pnpm -r build
```

### 2. Configura una API key

```bash
export OPENAI_API_KEY=sk-...
# o: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander **detecta automáticamente** el proveedor. Lista completa: [Proveedores](/es/guide/providers).

### 3. Plan (sin riesgo)

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

Deberías ver complejidad, topología y asignación de agentes **sin modificar archivos**.

### 4. Ejecutar con stream

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

Deberías ver en vivo pensamientos de agentes, llamadas a herramientas y puertas de calidad.

### 5. (Opcional) Consola web

```bash
pnpm gui
```

- API: `http://localhost:4000`  
- Web: suele ser `http://localhost:5173` (dev) o `http://localhost:3000` (Docker)

Ver [Consola web](/es/guide/web-console).

### 6. (Opcional) Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## Tras el build: binario `commander`

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## Si algo falla

| Síntoma | Solución |
|---------|----------|
| `Provider not available` | `echo $OPENAI_API_KEY` — la key debe estar exportada en **esta** shell. Luego `npx tsx packages/core/src/cliEntry.ts doctor` |
| `Cannot find module` / errores de workspace | Ejecuta desde la raíz del repo con **pnpm**, luego `pnpm install` y `pnpm -r build` |
| Cuelgue / sin salida | Prueba `plan` primero; `COMMANDER_DEBUG=true`; revisa red y estado del proveedor |
| Rate limit | Espera, baja concurrencia (`COMMANDER_MAX_CONCURRENCY=1`) o añade una segunda key |
| Circuit breaker abierto | Espera ~30s o `npx tsx packages/core/src/cliEntry.ts doctor --reset` |
| Solo offline | Ollama: `export OLLAMA_BASE_URL=http://localhost:11434` |

Guía completa: [Solución de problemas](/es/guide/troubleshooting).

## ¿Qué acaba de pasar?

1. **Clasificó** la tarea (CODING / RESEARCH / ANALYSIS / FACTUAL)  
2. **Eligió** una topología (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)  
3. **Ejecutó** uno o más agentes con herramientas  
4. **Verificó** la salida con cinco puertas de calidad  

Detalles: [Árbol de decisión de topología](/es/guide/usage/topology-decision-tree) · [Arquitectura](/es/architecture/overview).

## Siguientes pasos

| Objetivo | Ir a |
|----------|------|
| Recetas reales | [Cookbook](/es/guide/cookbook/) |
| ¿Por qué no el framework X? | [Por qué Commander](/es/guide/why-commander) |
| Integrar en TypeScript | [Agent SDK](/es/guide/sdk) |
| Desplegar en una VM | [Despliegue](/es/deployment) · [Instalación](/es/guide/installation) |
| Referencia CLI | [Comandos](/es/guide/commands) |
