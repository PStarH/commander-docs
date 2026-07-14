# Tools

**Tools.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `read` | `file_read` | File reading with line/offset support |
| `write` | `file_write` | File creation and overwrite |
| `edit` | `file_edit` | Exact string replacement |
| `glob` / `file_search` | `file_search` | Pattern-based file discovery |
| `grep` / `file_list` | `file_list` | Content search and directory listing |


## Contenu principal

### Filesystem Operations

En pratique, **Filesystem Operations** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Code Intelligence

En pratique, **Code Intelligence** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Web & Research

En pratique, **Web & Research** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Code Execution

En pratique, **Code Execution** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Memory & Persistence

En pratique, **Memory & Persistence** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Version Control

En pratique, **Version Control** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Media & Analysis

En pratique, **Media & Analysis** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Orchestration

En pratique, **Orchestration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Production Features

En pratique, **Production Features** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

### Custom Tools

En pratique, **Custom Tools** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/tools) pour le détail exhaustif.

## Exemples (code inchangé)

```typescript
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    return { success: true, data: ... };
  }
}

runtime.registerTool('my-tool', new MyCustomTool());
```

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
