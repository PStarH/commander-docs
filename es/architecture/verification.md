# Pipeline de verificación

Toda salida de agente pasa por **5 puertas de calidad** antes de devolverse al caller. No es un check opcional: forma parte del bucle de reintento del runtime.

## Arquitectura

```
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  ├─ Gate 2: Consistency Check
  ├─ Gate 3: Completeness Verification
  ├─ Gate 4: Accuracy Validation
  ├─ Gate 5: Safety Scanning
  └─ → Pass / Fail → retry o informe con contexto
```

## UnifiedVerificationPipeline

```typescript
const pipeline = new UnifiedVerificationPipeline();
const result = await pipeline.verify(output, context, { tenantId });

result.gates.forEach((gate) => {
  if (!gate.passed) {
    // reintento con gate.feedback
  }
});
```

## Puertas

1. **Alucinación** — señales (no juez LLM circular): claims sin soporte de tools, números inconsistentes, contradicciones
2. **Consistencia** — sin contradicciones lógicas; terminología estable
3. **Completitud** — salidas pedidas presentes; sin placeholders TODO/FIXME
4. **Exactitud** — frente a restricciones y resultados de tools
5. **Seguridad** — inyección, fugas tipo secretos, comandos peligrosos

Umbrales configurables por tenant. Tras fallos reiterados se reporta el modo de fallo al caller.

## Relacionado

- [Agent Runtime](/es/architecture/agent-runtime)
- [Production readiness](/es/architecture/production-readiness)
- [Seguridad](/es/guide/security)
