# Tools

Commander ships with **25+ built-in tools**, each designed for production use with caching, error handling, and rollback support.

## Tool Categories

### Filesystem Operations
| Tool | Purpose |
|------|---------|
| `read` | File reading with line/offset support |
| `write` | File creation and overwrite |
| `edit` | Exact string replacement |
| `glob` | Pattern-based file discovery |
| `grep` | Content search across files |

### Code Intelligence
| Tool | Purpose |
|------|---------|
| `ast_grep_search` | AST-aware code pattern search |
| `ast_grep_replace` | AST-aware code transformation |
| `lsp_diagnostics` | Language server diagnostics |
| `lsp_symbols` | Document and workspace symbols |
| `lsp_find_references` | Reference search |
| `lsp_rename` | Safe symbol renaming |

### Web & Research
| Tool | Purpose |
|------|---------|
| `websearch` | Real-time web search |
| `webfetch` | URL content fetching |
| `context7_query_docs` | Library documentation queries |
| `context7_resolve_library_id` | Library ID resolution |

### Orchestration
| Tool | Purpose |
|------|---------|
| `task` | Sub-agent delegation (recursive) |
| `skill` | Domain expertise loading |
| `todowrite` | Multi-step task tracking |
| `question` | User clarification |

### Media & Analysis
| Tool | Purpose |
|------|---------|
| `look_at` | Media file analysis |
| `lazyweb_*` | Screenshot similarity search |

### Session & Utilities
| Tool | Purpose |
|------|---------|
| `session_*` | Session history management |
| `bash` | Shell execution with sandbox |

## Production Features

Every tool comes with:

- **SHA-256 result caching** — per-tenant key isolation
- **Compensation registry** — rollback failed mutation tools
- **Circuit breaker** — protect downstream services
- **Step error boundary** — skip/retry/abort per tool

## Custom Tools

Implement the `Tool` interface and register it:

```typescript
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    // Your implementation
    return { success: true, data: ... };
  }
}

runtime.registerTool('my-tool', new MyCustomTool());
```
