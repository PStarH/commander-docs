# Event sourcing y recuperación

Documentación en español de **Event sourcing y recuperación**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Metric | Degraded | Unhealthy |
|--------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | Any break |


| Component | Role |
|-----------|------|
| `RunLedger` | Source of truth for run states |
| `LeaseManager` | Fencing tokens for exclusive ownership |
| `CheckpointStore` | SQLite-backed checkpoint persistence |
| `DeadLetterQueue` | Records recovered/aborted runs |
| `MessageBus` | Publishes recovery events for subscribers |
| `CompensationBridge` | Triggers rollback for aborted runs |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
