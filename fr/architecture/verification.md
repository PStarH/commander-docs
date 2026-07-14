# Pipeline de vérification

**Pipeline de vérification.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Architecture

```
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ Détecteur signal-based à seuils configurables
  │
  ├─ Gate 2: Consistency Check
  │   └─ Cohérence interne et contradictions
  │
  ├─ Gate 3: Completeness Verification
  │   └─ Champs et étapes requis présents
  │
  ├─ Gate 4: Accuracy Validation
  │   └─ Exactitude factuelle vs contraintes connues
  │
  ├─ Gate 5: Safety Scanning
  │   └─ Injection, fuite de données sensibles
  │
  └─ → Pass: renvoyer le résultat
     → Fail: retry ou rapport avec contexte complet
```

## UnifiedVerificationPipeline

`UnifiedVerificationPipeline` orchestre les 5 portes.

```typescript
interface UVPTaskContext {
  goal: string;
  availableTools: string[];
  steps: Step[];
  // ... full execution context
}

const pipeline = new UnifiedVerificationPipeline();
const result = await pipeline.verify(output, context, { tenantId });

result.gates.forEach((gate) => {
  if (!gate.passed) {
    // Échec → retry avec gate.feedback comme contexte
  }
});
```

## Détail des portes

### 1. Hallucination

Détection **par signaux**, pas un juge LLM (circulaire).

- Affirmations non supportées par les sorties d’outils
- Incohérences numériques
- Contradictions dans la même réponse
- Confiance qui ne matche pas les preuves

Seuils configurables par tenant (sensibilité vs faux positifs).

### 2. Cohérence

- Pas de contradiction logique entre sections
- Terminologie et références stables
- Items actionnables alignés sur leurs préconditions

### 3. Complétude

- Toutes les sorties demandées présentes
- Champs requis peuplés
- Pas de placeholders (« TODO », « FIXME »)

### 4. Exactitude

Validation factuelle contre contraintes connues, résultats d’outils et objectif de tâche.

### 5. Sécurité

Injection, fuites type secrets, suggestions de commandes dangereuses.

## En cas d’échec

Un échec de porte mène en général à un **retry**, le feedback entrant dans le contexte LLM suivant. Au-delà des limites, l’appelant reçoit un échec avec mode de panne.

## Voir aussi

- [Agent Runtime](/fr/architecture/agent-runtime)
- [Production readiness](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
