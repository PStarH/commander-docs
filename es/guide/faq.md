# Preguntas frecuentes

## General

### ¿Qué es Commander?

Un motor de orquestación multi-agente que coordina varios agentes de IA sobre 5 topologías canónicas (single, chain, dispatch, orchestrator, review), con 25 proveedores LLM y 18 tools integradas.

### ¿En qué se diferencia de otros tools de coding con IA?

La mayoría usan un solo agente y un solo modelo. Commander orquesta **varios agentes** sobre **cualquier topología**, eligiendo la estrategia según la complejidad, con streaming SSE, puertas de calidad y primitivas de producción (circuit breakers, multi-tenant, checkpoints).

### ¿Es open source?

Sí. Licencia MIT.

### ¿Qué significa «orquestación multi-agente»?

Commander puede lanzar varios agentes que colaboran en una tarea: en paralelo, revisándose entre sí, o con un arquitecto líder que delega en especialistas.

## Configuración

### ¿Necesito varias API keys?

No. **Con una basta**. Configura `OPENAI_API_KEY` (u otra) y Commander auto-detecta el proveedor. El failover entra en juego cuando configuras varias.

### ¿Puedo usarlo offline?

Sí, con Ollama o vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### ¿El paquete npm ya está publicado?

`@commander/core` y `@commander/sdk` se construyen para publicar; el release público está **en curso**. Mientras tanto, clona el monorepo. Ver [Agent SDK](/es/guide/sdk).

## Uso

### ¿Puede editar mis archivos?

Por defecto sí — controla con modos de aprobación:

- `plan` — solo plan
- `read-only` — lectura
- `suggest` — sugiere y espera
- `auto-edit` — edita solo
- `full-auto` — totalmente autónomo

### ¿En CI/CD?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

### ¿Cuántos agentes usa?

1–20 según complejidad. Tareas simples: 1. Investigación compleja: un equipo completo.

### ¿Cuáles son las cinco topologías?

| Topología | Cuándo |
|-----------|--------|
| **SINGLE** | Respuestas one-shot |
| **CHAIN** | Pipeline secuencial |
| **DISPATCH** | Especialistas en paralelo + síntesis |
| **ORCHESTRATOR** | Líder que delega |
| **REVIEW** | Producir y luego criticar / fusionar |

Ver [Árbol de topología](/es/guide/usage/topology-decision-tree).

## Rendimiento

### ¿Es rápido?

Las tareas simples suelen terminar en segundos. Los runs multi-agente complejos pueden llevar decenas de segundos a minutos. La caché semántica reduce trabajo LLM redundante.

## Empresa

### ¿Multi-tenant?

Sí. Ver [Multi-tenant](/es/architecture/multi-tenancy).

### ¿On-premise?

Sí, Docker en cualquier Linux VM. Ver [Despliegue](/es/deployment).

### ¿Hay plan de pago?

La versión open source es completa y gratuita. Cloud gestionado (SSO, API alojada, SLA) está en el [roadmap](/es/community).

## Datos y privacidad

### ¿Guarda mi código?

Commander corre en tu máquina (o servidor). No sube código a un cloud de Commander por defecto. Solo se envía a los proveedores LLM **que configures**.

### ¿Código sensible?

Sí. Prefiere Ollama/vLLM o despliegue en VPC.

## Relacionado

- [Solución de problemas](/es/guide/troubleshooting)
- [Instalación](/es/guide/installation)
- [Comunidad](/es/community)
