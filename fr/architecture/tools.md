# Tools

Commander expose par défaut **18 tools intégrés** au LLM (davantage de classes existent dans le monorepo). Conception production : cache, erreurs, rollback.

## Filesystem

| Tool | Nom interne | Rôle |
|------|-------------|------|
| `read` | `file_read` | Lecture (lignes/offset) |
| `write` | `file_write` | Création / écrasement |
| `edit` | `file_edit` | Remplacement exact |
| `glob` / `file_search` | `file_search` | Découverte par motif |
| `grep` / `file_list` | `file_list` | Recherche / listage |

## Intelligence de code

| Tool | Rôle |
|------|------|
| `ast_grep_search` | Recherche AST |
| `patches` | Patches structurés |
| `refine` / `fix` | Raffinement / fix IA |
| `lsp_*` | Diagnostics, symboles, refs, rename |

## Web & recherche

| Tool | Rôle |
|------|------|
| `websearch` / `webfetch` | Search & fetch |
| `browser_*` | Rendu navigateur |
| `context7_*` | Docs de librairies |

## Exécution

| Tool | Rôle |
|------|------|
| `bash` / `shell_execute` | Shell sandboxé |
| `python` / `execute_script` | Exécution isolée |

## Mémoire & persistance

| Tool | Rôle |
|------|------|
| `memory_store` / `memory_recall` / `memory_list` | Mémoire persistante |
| `knowledge_search` | Recherche RAG (builtin-rag) |

## VCS · média

| Tool | Rôle |
|------|------|
| `git` | status, diff, log, commit |
| `look_at` / `vision_analyze` | Vision |
| `pdf_extract` / `screenshot` | PDF / capture |

## Orchestration

| Tool | Rôle |
|------|------|
| `task` / `agent` | Délégation sous-agent |
| `a2a_delegate` | Délégation A2A |
| `skill` / `meta` / `verify` | Skills, meta, vérif |
| `todowrite` / `question` | Suivi / clarification |
| `mcp` / `saga` / `checkpoint` | MCP, saga, checkpoint |

## Fonctions production

- Cache résultats SHA-256 (isolation tenant)  
- Compensation registry  
- Circuit breaker  
- Step error boundary  
- Tool call repair  
- DLP sur 6 motifs d’entrée  

## Tools custom

```typescript
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    return { success: true, data: {} };
  }
}

runtime.registerTool('my-tool', new MyCustomTool());
```

> Workspace monorepo en premier.  
> CLI : `npx tsx packages/core/src/cliEntry.ts`

## Voir aussi

- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Custom tools](/fr/guide/advanced/custom-tools)  
- [MCP](/fr/architecture/mcp)  
- [Sécurité](/fr/guide/security)  
