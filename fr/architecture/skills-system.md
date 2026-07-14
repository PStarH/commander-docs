# Système de skills

Le système de skills fournit une **expertise de domaine empaquetée** que les agents chargent à la demande.

## Architecture

```
skills/
├── skillManager / skillCurator / skillInjector
├── skillStore / skillQualityScorer / skillSecurityScanner
├── skillViewTool / metaLearnerBridge
└── types / index
```

## Qu’est-ce qu’un skill ?

Instructions, exemples et contraintes pour un type de tâche.

- **Built-in** · **User-defined** · **Community** · **Learned** (MetaLearner)

## CLI

```bash
npx tsx packages/core/src/cliEntry.ts skill list
npx tsx packages/core/src/cliEntry.ts skill view <skill-name>
npx tsx packages/core/src/cliEntry.ts skill create <skill-name>
npx tsx packages/core/src/cliEntry.ts skill pin <skill-name>
```

Après build : `commander skill …`. Install monorepo en premier.

## Qualité & sécurité

Scoring auto + scan de contenu avant injection (injection / secrets).

## Injection runtime

`skillInjector` enrichit le prompt. Les skills pinés sont toujours chargés. Le MetaLearner peut promouvoir des patterns en skills.

## Voir aussi

- [Self-evolution](/fr/architecture/self-evolution)  
- [Intelligence](/fr/architecture/intelligence)  
- [Commandes CLI](/fr/guide/commands)  
