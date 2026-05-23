# Custom Tools

Extend Commander with your own tools by implementing the `Tool` interface.

## Tool Interface

```typescript
interface Tool {
  name: string;
  description: string;
  parameters?: Record<string, ParameterSchema>;

  execute(context: ToolContext, args: any): Promise<ToolResult>;
}
```

## Example: Webhook Tool

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

## Registering a Tool

```typescript
import { CommanderRuntime } from '@commander/core';

const runtime = new CommanderRuntime();
runtime.registerTool('webhook', new WebhookTool());
```

## Tool Features

Every registered tool automatically gets:

- **SHA-256 caching** — Results are cached per-tenant, per-argument hash
- **Compensation registry** — Register a rollback action for mutations
- **Circuit breaker** — Protects downstream services from overload
- **Step error boundary** — Isolated failure handling (skip/retry/abort)

## Loading Tools from Files

```json
// .commander.json
{
  "customTools": [
    "./tools/webhook-tool.ts",
    "./tools/database-tool.ts"
  ]
}
```
