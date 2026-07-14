# Tools

Commander incluye **18 tools integradas** expuestas al LLM por defecto (más clases de tools en el codebase).

Categorías típicas: filesystem, búsqueda de código, git, shell/sandbox, web, browser, handoff, ejecución de código, etc.

Cada tool puede llevar:

- Validación de argumentos  
- Timeouts  
- Políticas de aprobación  
- Compensación si es mutante  
- Caché de resultados  

## Custom tools

Ver [Tools custom](/es/guide/advanced/custom-tools) y el registro `ToolRegistry` en el monorepo.

## Relacionado

- [Runtime](/es/architecture/agent-runtime)  
- [MCP](/es/architecture/mcp)  
