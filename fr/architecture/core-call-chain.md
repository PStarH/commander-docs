# Chaîne d’appels core

Chaque exécution Commander suit un pipeline structuré.

## 1. Délibération

```
CLI / HTTP / API → deliberation.ts → TaskComplexityAnalyzer
```

Complexité, dépendances et domaine → stratégie d’exécution.

## 2. Effort scaling

```
effortScaler.ts  ← 1–20 agents
```

## 3. Routage topologique

```
topologyRouter.ts  ← SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW
```

## 4. Atomisation

```
atomizer.ts  ← décomposition style ROMA
```

## 5. Exécution

```
agentRuntime.execute
  → slot / tenant / storage
  → retry: LLM → tools → 5 portes → checkpoint
  → release / traces
```

## 6. Vérification & synthèse

Après les portes, synthèse du résultat. Échec → retry, DLQ, compensation.

## Suivre en local

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)  
- [Multi-agent](/fr/architecture/multi-agent)  
- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Vérification](/fr/architecture/verification)  
