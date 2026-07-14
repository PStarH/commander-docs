# Cookbook : audit de sécurité

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Cookbook : audit de sécurité**.

## Entrée rapide

```bash
cd /path/to/Commander
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=read-only
```

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

| Problema | Acción |
|----------|--------|
| Sin proveedor | `doctor`; env en esta shell |
| Auditoría superficial | Ruta real + prompt más específico |
| Gate SAFETY | Señal si hay patrones de secreto |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
