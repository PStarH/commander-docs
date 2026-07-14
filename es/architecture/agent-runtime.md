# Runtime de agentes

El runtime ejecuta el bucle **LLM → tools → verificación → reintento** para cada agente.

## Bucle

1. Construir mensajes (sistema + tarea + historial compactado)  
2. Llamar al proveedor LLM  
3. Parsear tool calls  
4. Ejecutar tools bajo política / sandbox  
5. Adjuntar resultados  
6. Pasar puertas de calidad  
7. Completar o reintentar  

## Streaming

Cada pensamiento, tool call y decisión de gate puede emitirse por **SSE** al terminal o a la consola web.

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## Fiabilidad en el runtime

- Timeouts por tool  
- Caché de resultados de tools  
- Circuit breakers por proveedor  
- Checkpoints de estado  

## Relacionado

- [Providers](/es/guide/providers)  
- [Tools](/es/architecture/tools)  
- [Verificación](/es/architecture/verification)  
