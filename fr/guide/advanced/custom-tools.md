# Custom Tools

**Custom Tools.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Contenu principal

### Tool Interface

En pratique, **Tool Interface** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-tools) pour le détail exhaustif.

### Example: Webhook Tool

En pratique, **Example: Webhook Tool** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-tools) pour le détail exhaustif.

### Registering a Tool

En pratique, **Registering a Tool** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-tools) pour le détail exhaustif.

### Tool Features

En pratique, **Tool Features** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-tools) pour le détail exhaustif.

### Loading Tools from Files

En pratique, **Loading Tools from Files** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-tools) pour le détail exhaustif.

## Exemples (code inchangé)

```typescript
interface Tool {
  name: string;
  description: string;
  parameters?: Record<string, ParameterSchema>;

  execute(context: ToolContext, args: any): Promise<ToolResult>;
}
```

```typescript
import { Tool, ToolContext } from '@commander/core';

interface WebhookArgs {
  url: string;
  payload: Record<string, any>;
}

class WebhookTool implements Tool {
  name = 'webhook';
  description = 'Send data to a webhook URL';

  parameters = {
    url: { type: 'string', required: true, description: 'Webhook URL' },
    payload: { type: 'object', required: true, description: 'JSON payload' },
  };

  async execute(context: ToolContext, args: WebhookArgs): Promise<ToolResult> {
    try {
      const response = await fetch(args.url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(args.payload),
      });

      return {
        success: response.ok,
        data: await response.text(),
        error: response.ok ? undefined : `HTTP ${response.status}`,
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
      };
    }
  }
}
```

```typescript
import { CommanderRuntime } from '@commander/core';

const runtime = new CommanderRuntime();
runtime.registerTool('webhook', new WebhookTool());
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
