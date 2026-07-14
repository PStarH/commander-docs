# Event sourcing & récupération

Le système d’event sourcing de Commander offre une exécution **tolérante aux crashs**, des pistes d’audit inviolables, un replay déterministe et la récupération automatique des runs zombies.

## EventSourcingEngine

`EventSourcingEngine` implémente le contrat IEventSourcingEngine (Pillar I) avec un WAL (Write-Ahead Log) et une chaîne de hash SHA-256.

### Write-Ahead Log

Chaque événement est append atomiquement dans `.commander_state/event-sourcing.wal` (chemin via `COMMANDER_EVENT_SOURCING_WAL`) :

```
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

Un verrou d’écriture sérialise les appends pour ne pas corrompre la chaîne.

### Intégrité de la chaîne

Chaque hash inclut le précédent. `verifyIntegrity()` recalcule tout pour détecter une altération.

### Entrées non déterministes

Enregistrées pour le replay (pas de recomputation) :

- Horodatages · aléas (UUID, salt) · réponses LLM · résultats de tools  

Contrainte IF-05 : rejouer le log produit les mêmes transitions d’état.

### Snapshot & compaction

- `snapshot()` — restauration rapide sans replay complet  
- `compact()` — retire les événements avant un snapshot, réécrit le WAL  
- `readFrom(snapshotId)` — flux d’événements après le snapshot  

### Santé

| Métrique | Degraded | Unhealthy |
|----------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | Toute rupture |

Exposé via `/health/detailed`.

### EventSourcingSubscriber

S’abonne au MessageBus sans envahir la boucle principale ; écriture WAL async ; dégradation gracieuse si WAL indisponible.

## RecoveryBootstrapper

Au démarrage, scan des runs zombies :

1. **RunLedger** — EXECUTING / VERIFYING / PAUSED  
2. **Lease** — baux expirés  
3. **Fencing lease** — holder `recovery-{pid}`, TTL 30s  
4. **Décision**  
   - PAUSED + checkpoint récupérable → resume  
   - EXECUTING/VERIFYING → abort + compensate  
   - Déjà traité → skip  
5. **DLQ** · événements MessageBus  

### Idempotence

Deux processus au démarrage : le second voit le lease et skip. `forceAbort` pour CI.

```typescript
interface RecoveryResult {
  scanned: number;
  recovered: number;
  aborted: number;
  skipped: number;
  details: RecoveryDetail[];
}
```

## Priorité de récupération

1. **Replay d’événements** (le plus exact)  
2. **Checkpoint** (rapide, état récent éventuellement perdu)  
3. **Abort + compensate** (fallback sûr)  

## Intégrations

| Composant | Rôle |
|-----------|------|
| `RunLedger` | Source de vérité des runs |
| `LeaseManager` | Tokens de fencing |
| `CheckpointStore` | Checkpoints SQLite |
| `DeadLetterQueue` | Runs récupérés/abortés |
| `MessageBus` | Événements de recovery |
| `CompensationBridge` | Rollback des runs abortés |

## Voir aussi

- [Production readiness](/fr/architecture/production-readiness)  
- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Migration V2](/fr/guide/migration-v2)  
