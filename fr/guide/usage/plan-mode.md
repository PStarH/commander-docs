# Mode plan

**Mode plan.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Pourquoi

- **Sécurité** — revue du plan avant toute écriture  
- **Apprentissage** — comprendre la décomposition  
- **Debug** — topologie, agents, tools prévus  
- **Collaboration** — partager le plan avec l’équipe  

## Usage

```bash
npx tsx packages/core/src/cliEntry.ts mode plan
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## Sortie type

```
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃ → Subtasks: analyze → design → implement → verify
```

Indicateur de mode plan dans le terminal quand actif.

## Lié

- [Exécuter des tâches](/fr/guide/usage/running-tasks)  
- [Explorateur de topologie](/fr/guide/topology-explorer)
