# Resumen de arquitectura

Commander es un motor de orquestación multi-agente que convierte una descripción de tarea en un plan de ejecución estructurado entre agentes, tools y proveedores LLM.

## Lee primero estas cinco páginas

Si eres nuevo, con esto basta para entender el sistema:

1. **Esta página** — flujo de alto nivel y mapa de paquetes  
2. [Cadena de llamadas core](/es/architecture/core-call-chain) — del request al resultado  
3. [Orquestación multi-agente](/es/architecture/multi-agent) — topologías y coordinación  
4. [Runtime de agentes](/es/architecture/agent-runtime) — LLM → tools → verificar → reintentar  
5. [Pipeline de verificación](/es/architecture/verification) — cinco puertas de calidad  

El resto (fiabilidad, seguridad, sistemas) es profundidad opcional — colapsado en la barra lateral.

## Flujo de alto nivel

```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         Análisis de tarea y selección de topología
  ├─ effortScaler.ts         Escala agentes (1-20) por complejidad
  ├─ topologyRouter.ts       Enruta a la topología óptima (5 canónicas + legacy)
  ├─ atomizer.ts             Descomposición de tareas ROMA
  │
  ├─ agentRuntime.ts         LLM → tools → verificación → reintento
  │   ├─ providers/          25 proveedores LLM con cadenas de fallback
  │   ├─ toolResultCache.ts  Caché SHA-256 por tenant
  │   ├─ stateCheckpointer.ts Snapshots a prueba de crash (SQLite WAL)
  │   ├─ circuitBreaker.ts   Umbral de fallos → circuito abierto
  │   ├─ deadLetterQueue.ts  7 categorías, reenvío
  │   ├─ compensationRegistry.ts Rollback de tools mutantes
  │   ├─ contextCompactor.ts Compactación de mensajes por tokens
  │   ├─ tokenGovernor.ts    Presupuesto de tokens
  │   ├─ verificationLoop.ts Puertas de calidad (5 etapas)
  │   ├─ eventSourcingEngine.ts Log de eventos WAL + hash chain
  │   └─ qualityGater.ts     Detección de degradación
  │
  ├─ enterpriseSecurityGateway.ts  Defensa en profundidad (7 capas)
  ├─ agentHandoff.ts         Handoff entre agentes
  ├─ messageBus.ts           Pub/sub
  ├─ metricsCollector.ts     Métricas unificadas (Prometheus)
  ├─ threeLayerMemory.ts     Working / Episodic / Long-term
  ├─ metaLearner.ts          Thompson Sampling + Reflexion
  └─ pluginManager.ts        Hooks y plugins sandboxed
```

## Estructura de paquetes

```
packages/core/src/
├── runtime/             ← Motor de ejecución
├── ultimate/            ← Orquestación
├── security/            ← Gateway de seguridad
├── tools/               ← 18 tools integradas
├── sandbox/             ← Perfiles de seguridad
├── atr/                 ← Agent Task Recovery
├── selfEvolution/       ← Meta-aprendizaje
├── saga/                ← Compensación distribuida
├── mcp/                 ← Model Context Protocol
└── plugins/builtin/     ← p. ej. RAG
```

## Principios de diseño

1. **Topología primero** — se analiza la estructura de la tarea antes de ejecutar  
2. **Agnóstico al proveedor** — 25 proveedores, interfaz unificada y fallback  
3. **A prueba de crash** — cada paso con checkpoint atómico (SQLite WAL)  
4. **Observable por defecto** — métricas, trazas, SSE  
5. **Multi-tenant de diseño** — aislamiento en storage, memoria, límites y caché  
6. **Seguro por defecto** — gateway de 7 capas, DLP, tokens de capacidad  
7. **Reversible** — event sourcing, compensación, DLQ, recovery bootstrap  

## Relacionado

- [Cadena de llamadas](/es/architecture/core-call-chain)  
- [Multi-agente](/es/architecture/multi-agent)  
- [Runtime](/es/architecture/agent-runtime)  
- [Listo para producción](/es/architecture/production-readiness)  
