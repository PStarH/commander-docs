# Sistema de skills

Documentación en español de **Sistema de skills**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
skills/
├── skillManager.ts       ← Skill lifecycle management
├── skillCurator.ts       ← Skill curation and organization
├── skillInjector.ts      ← Inject skills into agent prompts
├── skillStore.ts         ← Persistent skill storage
├── skillQualityScorer.ts ← Quality scoring for skills
├── skillSecurityScanner.ts ← Security scanning for skill content
├── skillViewTool.ts      ← Tool for viewing/loading skills
├── metaLearnerBridge.ts  ← Bridge to MetaLearner for skill optimization
├── types.ts              ← Shared types
└── index.ts              ← Public exports
```

```bash
# List available skills
npx tsx packages/core/src/cliEntry.ts skill list

# View a skill's content
npx tsx packages/core/src/cliEntry.ts skill view <skill-name>

# Create a new skill
npx tsx packages/core/src/cliEntry.ts skill create <skill-name>

# Pin a skill (always loaded)
npx tsx packages/core/src/cliEntry.ts skill pin <skill-name>
```

```typescript
// skills/my-domain-skill.json
{
  "name": "domain-expert",
  "version": "1.0.0",
  "description": "Expert knowledge for domain X",
  "instructions": [
    "When working with domain X, always follow these patterns...",
    "Preferred tools for domain X are: read, search, analyze"
  ],
  "constraints": [
    "Never use write tool on production files",
    "Always validate schema before making changes"
  ],
  "examples": [
    {
      "task": "analyze domain X component",
      "approach": "1. Read the component files\n2. Identify patterns\n3. Generate report"
    }
  ]
}
```

| Metric | Description |
|--------|-------------|
| **Effectiveness** | How often using the skill improves outcomes |
| **Precision** | How accurately the skill guides the agent |
| **Completeness** | Whether the skill covers all necessary aspects |
| **Safety** | No harmful or insecure instructions |
| **Freshness** | How recently the skill was updated |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
