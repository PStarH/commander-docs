# Extension Points

**Extension Points.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentComplete` | Agent run finished |
| `onError` | Run failed |


## Contenu principal

### Plugin System (19 Hook Points)

En pratique, **Plugin System (19 Hook Points)** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/extension-points) pour le détail exhaustif.

### Extension Interfaces

En pratique, **Extension Interfaces** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/extension-points) pour le détail exhaustif.

### Meta-Learner

En pratique, **Meta-Learner** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/extension-points) pour le détail exhaustif.

## Exemples (code inchangé)

```typescript
class MyProvider implements LLMProvider {
  async call(messages: Message[], options: CallOptions): Promise<LLMResponse> {
    // Your implementation
  }
}
runtime.registerProvider('my-provider', new MyProvider());
```

```typescript
class MyTool implements Tool {
  name = 'my-tool';
  async execute(ctx: ToolContext, args: any): Promise<ToolResult> {
    // Your implementation
  }
}
runtime.registerTool('my-tool', new MyTool());
```

```typescript
class TelegramAdapter implements ChannelAdapter {
  // Telegram integration
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
