# Vérificateur de consensus

Votes multi-modèles pour décisions à haut risque.

> **Couche 2** du runtime (`@commander/core`). Pour la plupart des applications, préférez [`CommanderClient`](/fr/guide/sdk) (couche 1).

## Rôle dans le pipeline

1. La délibération / l’analyse peut s’appuyer sur ce composant  
2. Le runtime orchestre ensuite agents et tools  
3. Les résultats passent les portes de qualité  

## Exemple d’orientation

```typescript
import { /* composant correspondant */ } from '@commander/core';
// Voir monorepo pour les signatures exactes et getGlobal*()
```

## Quand l’utiliser

- Étendre le runtime ou instrumenter le planner  
- Tests unitaires d’un sous-système  
- Recherche / expérimentation  

## Quand ne pas l’utiliser

- « Lance simplement cette tâche » → `CommanderClient.run()`  
- Client polyglotte distant → API HTTP  

## Lié

- [Vue d’ensemble API](/fr/api/overview)  
- [Architecture](/fr/architecture/overview)  
- [Délibération / multi-agents](/fr/architecture/multi-agent)
