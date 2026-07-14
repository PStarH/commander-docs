# Skills System

**Skills System.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Metric | Description |
|--------|-------------|
| **Effectiveness** | How often using the skill improves outcomes |
| **Precision** | How accurately the skill guides the agent |
| **Completeness** | Whether the skill covers all necessary aspects |
| **Safety** | No harmful or insecure instructions |
| **Freshness** | How recently the skill was updated |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

### What is a Skill?

En pratique, **What is a Skill?** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

### Managing Skills

En pratique, **Managing Skills** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

### Skill Quality

En pratique, **Skill Quality** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

### Security Scanning

En pratique, **Security Scanning** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

### Creating a Skill

En pratique, **Creating a Skill** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/skills-system) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
