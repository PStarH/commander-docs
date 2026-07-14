# Tools

Commander expone **18 tools integradas** al LLM por defecto (hay más clases en el código) en varias categorías, pensadas para producción: caché, errores y rollback cuando aplica.

## Filesystem

| Tool                   | Nombre interno | Uso                             |
| ---------------------- | -------------- | ------------------------------- |
| `read`                 | `file_read`    | Lectura con offset/líneas       |
| `write`                | `file_write`   | Crear/sobrescribir              |
| `edit`                 | `file_edit`    | Reemplazo exacto                |
| `glob` / `file_search` | `file_search`  | Descubrimiento por patrón       |
| `grep` / `file_list`   | `file_list`    | Búsqueda de contenido / listado |

## Inteligencia de código

| Tool              | Uso                                         |
| ----------------- | ------------------------------------------- |
| `ast_grep_search` | Búsqueda AST                                |
| `patches`         | Aplicar parches estructurados               |
| `refine` / `fix`  | Refinado y fixes con IA                     |
| `lsp_*`           | Diagnósticos, símbolos, referencias, rename |

## Web e investigación

| Tool                     | Uso                |
| ------------------------ | ------------------ |
| `websearch` / `webfetch` | Búsqueda y fetch   |
| `browser_*`              | Render vía browser |
| `context7_*`             | Docs de librerías  |

## Ejecución

| Tool                        | Uso               |
| --------------------------- | ----------------- |
| `bash` / `shell_execute`    | Shell con sandbox |
| `python` / `execute_script` | Ejecución aislada |

## Memoria y orquestación

Tools de memoria, delegación a sub-agentes y utilidades de runtime completan el set. El número **18** es el expuesto por defecto al modelo; el monorepo puede contener más implementaciones.

## Principios

- Resultados cacheables cuando es seguro
- Errores tipados y reintentos controlados
- Mutaciones con compensación cuando está registrada
- Sandbox / límites de tiempo en ejecución de código

## Relacionado

- [Agent Runtime](/es/architecture/agent-runtime)
- [Extensiones](/es/architecture/extension-points)
- [Custom tools](/es/guide/advanced/custom-tools)
