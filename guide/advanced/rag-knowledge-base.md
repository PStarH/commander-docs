# RAG Knowledge Base

Commander includes a built-in optional RAG (Retrieval-Augmented Generation) plugin that provides knowledge base search capabilities without requiring external services.

## Overview

The `builtin-rag` plugin is a `CommanderPlugin` with category `integration`, **disabled by default**. It provides:

- Document ingestion with chunking and embedding
- HNSW vector index for fast similarity search
- Automatic context injection before LLM calls (optional)
- OpenAI or local embedding (zero-dependency fallback)

## Enabling the Plugin

```bash
# Enable via CLI
commander plugin enable rag

# Or in .commander.json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
}
```

## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `kbPath` | `.commander/knowledge-base/` | Storage directory for documents and vectors |
| `embeddingModel` | `text-embedding-3-small` | OpenAI embedding model (when API key available) |
| `chunkSize` | `512` | Document chunk size in characters |
| `chunkOverlap` | `50` | Overlap between chunks |
| `maxResults` | `5` | Maximum search results returned |
| `autoInject` | `false` | Auto-inject relevant context before LLM calls |

## Embedding Strategy

The plugin automatically selects the embedding backend:

1. **OpenAI embeddings** — Used when `OPENAI_API_KEY` is set. Model: `text-embedding-3-small`
2. **Local embedding** — Zero-dependency fallback for offline use. No API key required.

## Vector Search

Search uses the existing HNSW index (`memory/hnswIndex.ts`):

- Datasets with **1000+ entities** use HNSW for approximate nearest neighbor search
- Smaller datasets fall back to brute-force search for exact results
- The `bruteForceThreshold` defaults to 1000

## Document Ingestion

Documents are processed through a chunk → embed → index → persist pipeline:

```
Document → Chunk (512 chars, 50 overlap) → Embed → Index (HNSW) → Persist
```

Storage layout:
- `kb-documents.json` — Document metadata
- `kb-vectors.json` — Chunk payloads with embeddings

Writes are atomic (temp file + rename) to prevent corruption.

## API Endpoints

When enabled, the following API endpoints become available:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/knowledge-base` | `GET` | List all documents |
| `/api/knowledge-base` | `POST` | Upload a document |
| `/api/knowledge-base/:id` | `DELETE` | Remove a document |
| `/api/knowledge-base/search` | `POST` | Search the knowledge base |

## Knowledge Search Tool

The plugin registers a `knowledge_search` tool that LLM agents can call:

```typescript
// Tool parameters
{
  query: string,      // Search query
  topK: number        // Results to return (1-50, default 5)
}
```

## Auto-Inject Mode

When `autoInject` is enabled, the plugin installs a `beforeLLMCall` hook that:

1. Extracts the query context from the current conversation
2. Searches the knowledge base for relevant chunks
3. Assembles a system message with retrieved context
4. Injects it at the front of the message list

This provides RAG capabilities without requiring the LLM to explicitly call the `knowledge_search` tool.

## Web Interface

When the plugin is enabled, a Knowledge Base management page appears in the web GUI:

- Upload documents (drag-and-drop)
- View document list with metadata
- Delete documents
- Test search queries

The page is hidden when the plugin is disabled.

## Shared Store

The `KnowledgeBaseStore` uses a process-level singleton (`getSharedKnowledgeBaseStore()`), ensuring that API endpoints and the plugin itself access the same instance.
