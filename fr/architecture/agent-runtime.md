# Runtime agents

Le runtime exécute la boucle **LLM → tools → vérification → retry** pour chaque agent.

## Boucle

1. Construire les messages (système + tâche + historique compacté)  
2. Appeler le fournisseur LLM  
3. Parser les tool calls  
4. Exécuter les tools sous politique / sandbox  
5. Attacher les résultats au contexte  
6. Passer les **portes de qualité**  
7. Terminer ou réessayer avec contexte  

## Streaming SSE

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
# ou
npx tsx packages/core/src/cliEntry.ts watch "task"
```

Chaque pensée, tool call et décision de gate peut être émise vers le terminal ou la console web.

## Fiabilité intégrée

| Mécanisme | Rôle |
|-----------|------|
| Timeouts par tool | Évite les runs bloqués |
| Cache de résultats | Moins de travail redondant |
| Circuit breakers | Isole un fournisseur en panne |
| Checkpoints | Reprise après crash |

## Lié

- [Fournisseurs](/fr/guide/providers)  
- [Tools](/fr/architecture/tools)  
- [Vérification](/fr/architecture/verification)  
- [Multi-agents](/fr/architecture/multi-agent)
