# Tools custom

Registra tools propias en `ToolRegistry` para que los agentes puedan invocarlas.

## Idea

```typescript
import { ToolRegistry } from '@commander/core';

class MyTool {
  name = 'my_tool';
  description = 'Does something useful';
  // schema de argumentos + execute(...)
}

ToolRegistry.register(new MyTool(), 'custom');
```

## Buenas prácticas

| Práctica | Por qué |
|----------|---------|
| Schema estricto | Evita tool calls basura del modelo |
| Timeouts | Tools colgadas matan el run |
| Idempotencia | Reintentos seguros |
| Compensación | Si muta estado, registra rollback |
| Aprobación | Tools peligrosas → modo `suggest` / policy |

## CLI

```bash
# Las tools built-in ya están registradas en el runtime
npx tsx packages/core/src/cliEntry.ts run "use tools to inspect the repo" --stream
```

## Relacionado

- [Tools (arquitectura)](/es/architecture/tools)  
- [Plugins](/es/guide/advanced/plugin-system)  
- [Sandbox](/es/architecture/sandbox)
