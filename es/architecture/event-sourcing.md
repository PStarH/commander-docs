# Event sourcing y recuperación

Commander puede registrar eventos de ejecución en un log append-only (WAL + hash chain) para:

- Replay determinista  
- Auditoría  
- Recuperación tras crash  

El bootstrap de recovery detecta runs zombi y reanuda cuando es seguro.

[ATR](/es/architecture/atr) · [Producción](/es/architecture/production-readiness)
