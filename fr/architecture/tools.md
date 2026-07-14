# Tools

Commander expose **18 tools intégrés** au LLM par défaut (davantage de classes dans le codebase).

## Catégories typiques

Filesystem · recherche de code · git · shell/sandbox · web · browser · handoff · exécution de code · utilitaires agent.

## Propriétés production

| Capacité | Pourquoi |
|----------|----------|
| Schema d’arguments | Moins de tool calls invalides |
| Timeouts | Évite les runs bloqués |
| Politiques / approbation | Tools dangereuses sous contrôle |
| Compensation | Rollback si mutation |
| Cache de résultats | Moins de travail redondant |

## Custom

Voir [Tools custom](/fr/guide/advanced/custom-tools) et `ToolRegistry` dans le monorepo.

## Lié

- [Runtime](/fr/architecture/agent-runtime) · [MCP](/fr/architecture/mcp) · [Sandbox](/fr/architecture/sandbox)
