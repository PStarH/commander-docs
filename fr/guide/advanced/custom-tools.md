# Tools custom

Enregistrez vos tools dans `ToolRegistry` pour que les agents puissent les appeler.

```typescript
import { ToolRegistry } from '@commander/core';

class MyTool {
  name = 'my_tool';
  description = 'Does something useful';
  // schema + execute(...)
}
ToolRegistry.register(new MyTool(), 'custom');
```

## Bonnes pratiques

| Pratique | Pourquoi |
|----------|----------|
| Schema strict | Moins de tool calls invalides |
| Timeouts | Évite les runs bloqués |
| Idempotence | Retries sûrs |
| Compensation | Rollback si mutation |
| Approbation | Tools dangereuses sous `suggest` / policy |

```bash
npx tsx packages/core/src/cliEntry.ts run "use tools to inspect the repo" --stream
```

[Tools](/fr/architecture/tools) · [Plugins](/fr/guide/advanced/plugin-system) · [Sandbox](/fr/architecture/sandbox)
