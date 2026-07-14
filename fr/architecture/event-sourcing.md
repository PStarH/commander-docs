# Event Sourcing & Recovery

**Event Sourcing & Recovery.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Metric | Degraded | Unhealthy |
|--------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | Any break |


## Contenu principal

### EventSourcingEngine

En pratique, **EventSourcingEngine** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/event-sourcing) pour le détail exhaustif.

### RecoveryBootstrapper

En pratique, **RecoveryBootstrapper** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/event-sourcing) pour le détail exhaustif.

### Recovery Strategy Priority

En pratique, **Recovery Strategy Priority** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/event-sourcing) pour le détail exhaustif.

### Integration Points

En pratique, **Integration Points** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/event-sourcing) pour le détail exhaustif.

## Exemples (code inchangé)

```
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

```typescript
interface RecoveryResult {
  scanned: number;      // Total zombie runs found
  recovered: number;   // Successfully resumed
  aborted: number;      // Aborted with compensation
  skipped: number;      // Already handled by another process
  details: RecoveryDetail[];
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
