# Base de conocimiento RAG

Documentación en español de **Base de conocimiento RAG**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

```
Document → Chunk (512 chars, 50 overlap) → Embed → Index (HNSW) → Persist
```

```typescript
// Tool parameters
{
  query: string,      // Search query
  topK: number        // Results to return (1-50, default 5)
}
```

| Option | Default | Description |
|--------|---------|-------------|
| `kbPath` | `.commander/knowledge-base/` | Storage directory for documents and vectors |
| `embeddingModel` | `text-embedding-3-small` | OpenAI embedding model (when API key available) |
| `chunkSize` | `512` | Document chunk size in characters |
| `chunkOverlap` | `50` | Overlap between chunks |
| `maxResults` | `5` | Maximum search results returned |
| `autoInject` | `false` | Auto-inject relevant context before LLM calls |


| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/knowledge-base` | `GET` | List all documents |
| `/api/knowledge-base` | `POST` | Upload a document |
| `/api/knowledge-base/:id` | `DELETE` | Remove a document |
| `/api/knowledge-base/search` | `POST` | Search the knowledge base |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
