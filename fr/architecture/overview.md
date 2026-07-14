# Vue d’ensemble de l’architecture

Commander est un moteur d’orchestration multi-agents qui transforme une description de tâche en plan d’exécution structuré entre agents, tools et fournisseurs LLM.

## Lisez d’abord ces cinq pages

Si vous débutez, cela suffit pour comprendre le système :

1. **Cette page** — flux haut niveau et carte des paquets  
2. [Chaîne d’appels core](/fr/architecture/core-call-chain) — de la requête au résultat  
3. [Orchestration multi-agents](/fr/architecture/multi-agent) — topologies et coordination  
4. [Runtime agents](/fr/architecture/agent-runtime) — LLM → tools → vérifier → réessayer  
5. [Pipeline de vérification](/fr/architecture/verification) — cinq portes de qualité  

Le reste (fiabilité, sécurité, systèmes) est optionnel — replié dans la sidebar.

## Flux haut niveau

```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         Analyse de tâche et choix de topologie
  ├─ effortScaler.ts         Scale agents (1-20) selon complexité
  ├─ topologyRouter.ts       Route vers la topologie optimale
  ├─ atomizer.ts             Décomposition de tâches ROMA
  │
  ├─ agentRuntime.ts         LLM → tools → vérification → retry
  │   ├─ providers/          25 fournisseurs LLM + chaînes de fallback
  │   ├─ toolResultCache.ts  Cache SHA-256 par tenant
  │   ├─ stateCheckpointer.ts Snapshots crash-safe (SQLite WAL)
  │   ├─ circuitBreaker.ts   Seuil d’erreurs → circuit ouvert
  │   ├─ deadLetterQueue.ts  7 catégories, rejeu
  │   ├─ compensationRegistry.ts Rollback des tools mutantes
  │   ├─ verificationLoop.ts Portes de qualité (5 étapes)
  │   └─ eventSourcingEngine.ts Journal WAL + hash chain
  │
  ├─ enterpriseSecurityGateway.ts  Défense en profondeur (7 couches)
  ├─ messageBus.ts           Pub/sub
  ├─ metricsCollector.ts     Métriques unifiées (Prometheus)
  ├─ threeLayerMemory.ts     Working / Episodic / Long-term
  ├─ metaLearner.ts          Thompson Sampling + Reflexion
  └─ pluginManager.ts        Hooks et plugins sandboxed
```

## Structure des paquets

```
packages/core/src/
├── runtime/             ← Moteur d’exécution
├── ultimate/            ← Orchestration
├── security/            ← Gateway de sécurité
├── tools/               ← 18 tools intégrés
├── sandbox/             ← Profils de sécurité
├── atr/                 ← Agent Task Recovery
├── selfEvolution/       ← Méta-apprentissage
├── saga/                ← Compensation distribuée
├── mcp/                 ← Model Context Protocol
└── plugins/builtin/     ← ex. RAG
```

## Principes de conception

1. **Topologie d’abord** — analyser la structure avant d’exécuter  
2. **Agnostique fournisseur** — 25 backends, interface unifiée + fallback  
3. **Crash-safe** — checkpoint atomique à chaque étape (SQLite WAL)  
4. **Observable par défaut** — métriques, traces, SSE  
5. **Multi-tenant by design** — isolation storage, mémoire, quotas, cache  
6. **Sécurisé par défaut** — gateway 7 couches, DLP, tokens de capacité  
7. **Réversible** — event sourcing, compensation, DLQ, recovery bootstrap  

## Lié

- [Chaîne d’appels](/fr/architecture/core-call-chain)  
- [Multi-agents](/fr/architecture/multi-agent)  
- [Runtime](/fr/architecture/agent-runtime)  
- [Prêt production](/fr/architecture/production-readiness)  
