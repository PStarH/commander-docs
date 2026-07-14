# Pipeline de vérification

Avant de renvoyer un résultat, Commander applique **cinq portes de qualité**.

| Porte | Vérifie |
|-------|---------|
| Hallucination | Faits inventés (signaux / LLM-as-judge) |
| Consistency | Accord entre agents, pas de contradiction |
| Completeness | Dimensions requises couvertes |
| Accuracy | Alignement avec le matériel source |
| Safety | Contenu, injection, secrets |

Si une porte échoue : **retry avec contexte** ou rapport d’échec explicite — jamais un « succès silencieux » incorrect.

## Où le voir

- Stream CLI / watch : lignes `[gate] …`  
- Console web : panneau d’exécution  
- Métriques / logs selon configuration  

## Lié

- [Runtime](/fr/architecture/agent-runtime)  
- [Sécurité](/fr/guide/security)  
- [Cookbook audit](/fr/guide/cookbook/security-audit)
