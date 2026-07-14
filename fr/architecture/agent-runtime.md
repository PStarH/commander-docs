# Runtime agents

Le runtime exécute la boucle **LLM → tools → vérification → retry**.

## Boucle

1. Construire les messages (système + tâche + historique compacté)  
2. Appeler le fournisseur LLM  
3. Parser les tool calls  
4. Exécuter les tools sous politique / sandbox  
5. Attacher les résultats  
6. Passer les portes de qualité  
7. Terminer ou réessayer  

## Streaming

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

Chaque pensée, tool call et décision de gate peut être émise en SSE.

## Fiabilité

Timeouts par tool · cache de résultats · circuit breakers · checkpoints.

## Lié

- [Fournisseurs](/fr/guide/providers) · [Tools](/fr/architecture/tools) · [Vérification](/fr/architecture/verification)
