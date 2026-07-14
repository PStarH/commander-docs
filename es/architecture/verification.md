# Pipeline de verificación

Antes de devolver un resultado, Commander aplica **cinco puertas de calidad**.

| Puerta | Comprueba |
|--------|-----------|
| Hallucination | Hechos inventados (LLM-as-judge / señales) |
| Consistency | Acuerdo entre agentes, sin contradicciones |
| Completeness | Dimensiones requeridas cubiertas |
| Accuracy | Alineación con material fuente |
| Safety | Contenido, inyección, secretos |

Si una puerta falla: reintento con contexto o informe de fallo explícito.

## Relacionado

- [Runtime](/es/architecture/agent-runtime)  
- [Seguridad](/es/guide/security)  
