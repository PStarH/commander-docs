# Exécution spéculative

Commander implémente une **exécution spéculative style PASTE** (Pattern-Aware Speculative Execution) : pendant que le LLM « réfléchit », les prochains appels d’outils probables sont pré-exécutés. La recherche rapporte jusqu’à ~48,5 % de réduction du temps de tâche.

## Fonctionnement

Pendant le thinking LLM, un Pattern Tracker prédit les tools suivants et les exécute à l’avance. Si le modèle les demande vraiment, le résultat est déjà là (attente nulle). Les mauvaises prédictions sont jetées sans effet de bord.

```
LLM Call → Pattern Tracker → Speculative Executor → résultats pré-exécutés (cache)
```

## Sécurité

Seuls les tools **en lecture seule** sont spéculés :

- ex. `file.read`, `web.search`, `web.fetch`, `code.search`, `git.status`

Les tools **mutateurs** ne le sont **jamais** :

- ex. `file.write`, `file.edit`, `shell.execute`, `git.commit`, `apply_patch`

## PatternTracker

```typescript
import { PatternTracker } from '@commander/core';

const tracker = new PatternTracker();
tracker.recordSequence(['file.read', 'code.search', 'file.read']);
const predictions = tracker.predictNext(['file.read']);
// → [{ toolName: 'code.search', confidence: 0.8 }]
```

### Cycle de vie

1. **Observation** — n-grammes (2, 3, 4)  
2. **Confiance** — `min(1, frequency / 10)`  
3. **Élagage** — &lt;2 occurrences ou inutilisé &gt;5 min  

## Ops

Optimisation interne. L’utilisateur voit le stream normal :

```bash
npx tsx packages/core/src/cliEntry.ts run "explain this repo" --stream
```

## Voir aussi

- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Tools](/fr/architecture/tools)  
- [Cache](/fr/architecture/caching)  
