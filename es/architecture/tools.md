# Tools

Commander expone **18 tools integradas** al LLM por defecto (hay más clases en el codebase).

## Categorías típicas

Filesystem · búsqueda de código · git · shell/sandbox · web · browser · handoff · ejecución de código · utilidades de agente.

## Propiedades de producción

| Capacidad | Por qué importa |
|-----------|-----------------|
| Schema de argumentos | Menos tool calls basura |
| Timeouts | Evita runs colgados |
| Políticas / aprobación | Tools peligrosas bajo control |
| Compensación | Rollback si muta estado |
| Caché de resultados | Menos trabajo redundante |

## Custom

Ver [Tools custom](/es/guide/advanced/custom-tools) y `ToolRegistry` en el monorepo.

## Relacionado

- [Runtime](/es/architecture/agent-runtime) · [MCP](/es/architecture/mcp) · [Sandbox](/es/architecture/sandbox)
