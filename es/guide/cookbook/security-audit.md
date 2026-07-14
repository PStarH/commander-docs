# Cookbook: auditoría de seguridad de un repositorio

**Objetivo:** auditoría multi-agente con streaming y hallazgos legibles.  
**Tiempo:** ~10 min · **Riesgo:** sobre todo lectura

## 1. Setup

```bash
cd /path/to/Commander
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=read-only
```

## 2. Plan primero

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**Espera:** clasificación (a menudo ANALYSIS), complejidad, topología (DISPATCH o REVIEW), roles.

## 3. Ejecutar con stream

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**Espera:** banner de deliberación, tools (grep, audit…), líneas de gates, síntesis de hallazgos.

## 4. Topología más estricta

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream --topology review
```

## 5. Checklist de éxito

- [ ] Plan con topología, sin crash  
- [ ] Stream con agentes/tools  
- [ ] Resumen final concreto o «ninguno en alcance»  
- [ ] Sin hang >2 min sin eventos  

## Fallos

| Problema | Acción |
|----------|--------|
| Sin proveedor | `doctor`; env en esta shell |
| Auditoría superficial | Ruta real + prompt más específico |
| Gate SAFETY | Señal si hay patrones de secreto |

## Relacionado

- [Seguridad](/es/guide/security) · [Topología](/es/guide/usage/topology-decision-tree)
