# Changelog

Resumen orientado a documentación. El detalle de commits vive en el monorepo del producto.

## v0.2.1-pre (sin publicar)

### Funciones destacadas

- **Persistencia SQLite**: `SqliteWarRoomStore` con WAL, índices y escrituras transaccionales (`WARROOM_STORAGE=sqlite`)
- **Event sourcing**: WAL con cadena SHA-256, recuperación por snapshot, replay determinista
- **Recovery bootstrapper**: al arrancar, detecta runs zombi y reanuda o aborta con compensación
- **Security gateway** de 7 capas + DLP (12+ patrones, 4 estrategias de redacción)
- **Plugins endurecidos**: sandbox de carga, timeouts por plugin
- **Plugin RAG** opcional (`builtin-rag`) con búsqueda vectorial
- **Audit log unificado** y wizard de onboarding web
- **Dashboards Grafana** (vista desarrollador + mecánica)
- **QualityGater** / Agent Capsules para degradación de calidad

### Mejoras

- 260+ tests nuevos · `no-explicit-any` como error · umbrales de cobertura subidos · Prettier/EditorConfig en CI

## v0.2.0 (2026-05-19)

- Agent War Room (GUI), OpenAPI 3.0, `/ready`, `/metrics`
- Multi-tenant, circuit breakers, DLQ, compensation, graceful shutdown
- 5 topologías canónicas + 9 alias legacy
- Comunicación por artefactos, protocolo A2A
- CLI ampliada: `company`, `swarm`, `drive`, `goal`, `review`, `saga`, `budget`, …

## v0.1.0 (2026-05-17)

- Topologías iniciales, proveedores LLM, tools, multi-tenant base
- Observabilidad Prometheus/SSE, plugins, meta-learning
- CLI: `run`, `plan`, `watch`, `gui`, `tui`

## Métricas actuales (docs)

25 proveedores · 5 topologías · 18 tools expuestas · 6700+ tests.

## Relacionado

- [Benchmarks](/es/guide/benchmarks)
- [Inicio rápido](/es/guide/getting-started)
- [Arquitectura](/es/architecture/overview)
