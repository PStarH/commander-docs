# Por qué Commander

Commander es para ingenieros que se niegan a tratar los sistemas multi-agente como una caja negra.

**Sin constructores de grafos. Sin YAML. Sin «rezar para que los agentes funcionen».**  
Una API key → clasificar la tarea → elegir topología → transmitir cada decisión → verificar cada salida.

## De un vistazo

| Dimensión | Commander | Frameworks multi-agente típicos |
|-----------|-----------|----------------------------------|
| **Cómo empiezas** | Tarea en lenguaje natural + una API key | Montar un grafo, escribir flujos YAML/JSON |
| **Topología** | 5 topologías canónicas elegidas automáticamente (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW) | Tú cableas las aristas |
| **Visibilidad** | SSE en vivo: pensamientos, herramientas, puertas de calidad | Logs a posteriori o ejecuciones opacas |
| **Calidad** | 5 capas (alucinación, consistencia, completitud, exactitud, seguridad) | Opcional / casero |
| **Proveedores** | 25 con auto-detección y failover | A menudo 1–2 de primera clase |
| **Producción** | Circuit breakers, DLQ, saga, checkpoints WAL, multi-tenant | Primero demo; ops después |
| **Integración** | CLI, SDK TypeScript, API HTTP, cliente Python | Suele ser una sola superficie |
| **Tests** | 6700+ | Muy variable |

## Cuándo elegir Commander

**Elige Commander si:**

- Necesitas **ver** qué hacen los agentes mientras corren  
- Quieres que la topología y el número de agentes se elijan por ti  
- Te importan el **failover**, los checkpoints y la auditoría en producción  
- Prefieres CLI / SDK a un constructor visual de grafos  
- Trabajas con cargas sensibles o multi-tenant  

**Considera otra cosa si:**

- Solo necesitas un chat completion con tools  
- Quieres SaaS gestionado sin autoalojamiento (la nube sigue en el [roadmap](/es/community))  
- Prefieres frameworks 100 % Python en proceso, sin runtime Node  

## Frente a enfoques habituales

### Frente a asistentes «un agente + tools»

Los asistentes de código optimizan un modelo y un hilo. Commander optimiza **equipos de agentes**, escala automática (1–20) y trabajo multi-paso **verificado**. Usa el asistente para ediciones rápidas; usa Commander cuando haga falta investigación paralela, revisión u orquestación.

### Frente a orquestadores basados en grafos (estilo LangGraph)

Los grafos brillan cuando **quieres** diseñar cada arista. Commander ofrece a cambio:

1. Deliberación que elige topología según clase de tarea y complejidad  
2. Observabilidad por streaming por defecto  
3. Primitivas de ops (breakers, DLQ, compensación) sin otra capa de plataforma  

Siempre puedes forzar topología y número de agentes.

### Frente a librerías tipo «crew»

Las crews destacan en roles y colaboración. Commander añade:

- Topologías canónicas con árbol de decisión  
- Failover entre 25 backends  
- Puertas de calidad y rutas de recuperación en producción  
- Consola web + API HTTP para ops, no solo scripts  

## Afirmaciones honestas

| Afirmación | Dónde vive |
|------------|------------|
| 25 proveedores | [Proveedores](/es/guide/providers), `providerRegistry.ts` |
| 5 topologías | [Árbol de topología](/es/guide/usage/topology-decision-tree) |
| 18 tools integradas | [Tools](/es/architecture/tools) |
| 6700+ tests | CI / [Benchmarks](/es/guide/benchmarks) |
| Streaming | [Agent Runtime](/es/architecture/agent-runtime), `run --stream` |
| Postura de seguridad | [Seguridad](/es/guide/security) |

Los benchmarks son scripts reproducibles en el monorepo, no capturas de marketing. Ver [Benchmarks](/es/guide/benchmarks).

## Prueba de 60 segundos

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

Éxito: clasificación → topología → pasos de agentes → puertas de calidad en el stream.

## Siguiente

- [Inicio rápido](/es/guide/getting-started)  
- [Cookbook](/es/guide/cookbook/)  
- [Arquitectura](/es/architecture/overview)  
