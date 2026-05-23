# Tools

Commander ships with **28 built-in tools** across 8 categories, each designed for production use with caching, error handling, and rollback support.

## Filesystem Operations

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `read` | `file_read` | File reading with line/offset support |
| `write` | `file_write` | File creation and overwrite |
| `edit` | `file_edit` | Exact string replacement |
| `glob` / `file_search` | `file_search` | Pattern-based file discovery |
| `grep` / `file_list` | `file_list` | Content search and directory listing |

## Code Intelligence

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `ast_grep_search` | `code_search` | AST-aware code pattern search |
| `patches` | `apply_patch` | Apply structured patches to files |
| `refine` | `refine_code` | AI-powered code refinement |
| `fix` | `fix_code` | Automatic code fix suggestions |
| `lsp_diagnostics` | — | Language server diagnostics |
| `lsp_symbols` | — | Document and workspace symbols |
| `lsp_find_references` | — | Reference search across workspace |
| `lsp_rename` | — | Safe symbol renaming |

## Web & Research

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `websearch` | `web_search` | Real-time web search |
| `webfetch` | `web_fetch` | URL content fetching |
| `browser_search` | `browser_search` | Browser-based web search |
| `browser_fetch` | `browser_fetch` | Browser-based page rendering |
| `context7_query_docs` | — | Library documentation queries |
| `context7_resolve_library_id` | — | Library ID resolution |

## Code Execution

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `bash` / `shell_execute` | `shell_execute` | Shell execution with sandbox |
| `python` | `python_execute` | Isolated Python execution |
| `execute_script` | `execute_script` | Run scripts from files |

## Memory & Persistence

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `memory_store` | `memory_store` | Store data in persistent memory |
| `memory_recall` | `memory_recall` | Recall stored memories by query |
| `memory_list` | `memory_list` | List all stored memories |

## Version Control

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `git` | `git` | Git operations (status, diff, log, commit) |

## Media & Analysis

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `look_at` / `vision_analyze` | `vision_analyze` | Image/vision analysis |
| `pdf_extract` | `pdf_extract` | PDF text extraction |
| `screenshot` | `screenshot_capture` | Screen capture |
| `lazyweb_*` | — | Screenshot similarity search |

## Orchestration

| Tool | Internal Name | Purpose |
|------|--------------|---------|
| `task` / `agent` | `agent` | Sub-agent delegation (recursive) |
| `a2a_delegate` | `a2a_delegate` | Agent-to-Agent (A2A) delegation |
| `skill` | `skill_view` | Domain expertise loading |
| `meta` | `meta_tool` | Meta-tool for multi-step workflows |
| `verify` | `verify_answer` | Answer format and quality verification |
| `todowrite` | — | Multi-step task tracking |
| `question` | — | User clarification |
| `mcp` | `mcp_tool_adapter` | MCP server tool integration |

## Production Features

Every tool comes with:

- **SHA-256 result caching** — per-tenant key isolation
- **Compensation registry** — rollback failed mutation tools
- **Circuit breaker** — protect downstream services
- **Step error boundary** — skip/retry/abort per tool
- **Tool call repair** — automatically fix malformed tool calls
- **Tool output management** — structured output parsing and validation

## Custom Tools

Implement the `Tool` interface and register it:

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
