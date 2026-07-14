# Préparation production

**Préparation production.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Matrice de capacités

| Capacité            | Statut Commander                                                          |
| ------------------- | ------------------------------------------------------------------------- |
| **Sûreté de types** | TypeScript strict, **zéro** `as any` / `@ts-ignore` (erreur ESLint)       |
| **Erreurs**         | **Zéro** catch vide sur 100+ modules                                      |
| **Métriques**       | MetricsCollector unifié Prometheus/OpenMetrics + labels tenant            |
| **Tracing**         | Spans persistés, export OpenTelemetry                                     |
| **Crash safety**    | Checkpoints SQLite WAL atomiques + hash chain d’event sourcing            |
| **Circuit breaker** | 5 échecs → 30s open → half-open, registre par provider                    |
| **DLQ**             | 7 catégories, 15 modes de panne, stockage persistant + replay             |
| **Multi-tenant**    | Rate limits, quotas de concurrence, isolation storage/cache               |
| **Sécurité**        | EnterpriseSecurityGateway 7 couches, DLP, capability tokens, Bearer, CORS |
| **Observabilité**   | Health, readiness, OpenAPI, SSE, dashboards Grafana                       |
| **Event sourcing**  | WAL SHA-256, snapshots, replay déterministe                               |
| **Sandbox plugins** | Contexte de load restreint ; permissions ≤ système principal              |

## Mécanismes de sûreté

### Circuit breaker

Après 5 échecs consécutifs, ouverture 30s puis half-open. `CircuitBreakerRegistry` gère les providers actifs.

### Dead letter queue

Erreurs non récupérables persistées (llm, tool, execution, verification, circuit_breaker, compensation, semantic_drift) avec 15 modes standard. Replay après correction de cause racine.

### Compensation registry

Outils de mutation en échec → rollback via actions enregistrées, intégré au coordinateur Saga.

### State checkpointer

Checkpoint atomique à chaque étape (SQLite WAL, synchronous=NORMAL, busy_timeout=5000).

### Event sourcing

WAL à chaîne de hash SHA-256. Entrées non déterministes (timestamps, aléas, réponses LLM, résultats tools) enregistrées pour replay déterministe.

### Recovery bootstrapper

Au démarrage : scan des runs zombies (EXECUTING/VERIFYING/PAUSED), lease de fencing, reprise ou abort avec compensation.

## Observabilité

```typescript
getMetricsCollector().exportOpenMetrics();
```

Endpoints : `/health`, `/ready`, `/metrics`, `/health/detailed`.

Dashboards Grafana développeur (succès, P95, coût tokens) et mécanistique (WAL, DLQ, breakers, contentions SQLite).

## Tests

**Tolérance zéro aux échecs :** 6700+ tests unit/integration/chaos/e2e, isolation multi-tenant, permissions plugins, stress 10K messages / 50 appels concurrents.

```
npx tsx --test tests/*.test.ts
npx tsc --noEmit
```

## Voir aussi

- [Agent Runtime](/fr/architecture/agent-runtime)
- [Vérification](/fr/architecture/verification)
- [Déploiement](/fr/deployment)
