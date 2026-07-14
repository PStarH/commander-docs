# Base de connaissances RAG

Plugin optionnel (recherche vectorielle / HNSW selon monorepo) pour ancrer les réponses dans votre corpus.

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
```

## Quand l’utiliser

- Runbooks, specs, politiques internes  
- Gros codebase hors fenêtre de contexte  
- Réponses qui doivent citer des sources  

## Bonnes pratiques

1. N’indexez que des documents de confiance  
2. Séparez les tenants  
3. Mesurez la qualité avec les gates  
4. Aucun secret dans l’index  

[Plugins](/fr/guide/advanced/plugin-system) · [Mémoire](/fr/api/three-layer-memory)
