# RAG Knowledge Base

**RAG Knowledge Base.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Option | Default | Description |
|--------|---------|-------------|
| `kbPath` | `.commander/knowledge-base/` | Storage directory for documents and vectors |
| `embeddingModel` | `text-embedding-3-small` | OpenAI embedding model (when API key available) |
| `chunkSize` | `512` | Document chunk size in characters |
| `chunkOverlap` | `50` | Overlap between chunks |
| `maxResults` | `5` | Maximum search results returned |
| `autoInject` | `false` | Auto-inject relevant context before LLM calls |


## Contenu principal

### Vue d’ensemble

En pratique, **Overview** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Enabling the Plugin

En pratique, **Enabling the Plugin** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Embedding Strategy

En pratique, **Embedding Strategy** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Vector Search

En pratique, **Vector Search** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Document Ingestion

En pratique, **Document Ingestion** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### API Endpoints

En pratique, **API Endpoints** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Knowledge Search Tool

En pratique, **Knowledge Search Tool** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Auto-Inject Mode

En pratique, **Auto-Inject Mode** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Web Interface

En pratique, **Web Interface** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

### Shared Store

En pratique, **Shared Store** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/rag-knowledge-base) pour le détail exhaustif.

## Exemples (code inchangé)

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
