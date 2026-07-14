# Event sourcing et recovery

Journal append-only (WAL + chaîne de hash) pour :

- Replay déterministe  
- Auditabilité  
- Recovery des runs zombies au démarrage  

Bootstrap de recovery : détecte les runs incomplets et reprend quand c’est sûr.


## Lié

- [Vue d’ensemble](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
