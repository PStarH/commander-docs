# Pipeline de verificación

Antes de devolver un resultado, Commander aplica **cinco puertas de calidad**.

| Puerta | Comprueba |
|--------|-----------|
| Hallucination | Hechos inventados (señales / LLM-as-judge) |
| Consistency | Acuerdo entre agentes, sin contradicciones |
| Completeness | Dimensiones requeridas cubiertas |
| Accuracy | Alineación con material fuente |
| Safety | Contenido, inyección, secretos |

Si una puerta falla: **reintento con contexto** o informe de fallo explícito — no un “éxito silencioso” incorrecto.

## Dónde se ve

- Stream CLI / watch: líneas `[gate] …`  
- Consola web: panel de ejecución  
- Métricas / logs según config  

## Relacionado

- [Runtime](/es/architecture/agent-runtime)  
- [Seguridad](/es/guide/security)  
- [Cookbook auditoría](/es/guide/cookbook/security-audit)
