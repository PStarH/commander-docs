# Plugin System

Commander's plugin system provides **19 hook points** to observe, modify, or block execution at any stage.

## Hook Points

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentStart` | Agent begins work |
| `onAgentComplete` | Agent finishes work |
| `onSubtaskCreate` | New subtask created |
| `onSubtaskComplete` | Subtask finished |
| `onCheckpoint` | State checkpoint saved |
| `onError` | Error occurred (non-fatal) |
| `onRetry` | Retry attempt starting |
| `beforeVerification` | Before quality gate check |
| `afterVerification` | After quality gate check |
| `onTokenUsage` | Token budget updated |
| `onMetricsEmit` | Metrics collected |
| `beforeRun` | Execution run starts |
| `afterRun` | Execution run completes |
| `onHandoff` | Agent-to-agent handoff |
| `onStreamEvent` | SSE event emitted |

## Creating a Plugin

```typescript
import { CommanderPlugin } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';

  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] Calling ${params.provider} with ${params.messages.length} messages`);
      return params; // Return modified params, or throw to block
    },

    afterToolCall: async (result) => {
      console.log(`[Tool] ${result.tool} completed in ${result.durationMs}ms`);
      return result; // Return modified result, or throw to block
    },

    onError: async (error) => {
      console.error(`[Error] ${error.message}`);
      // Don't return — errors are fire-and-forget
    },

    onMetricsEmit: async (metrics) => {
      // Forward metrics to external monitoring
      await fetch('https://monitor.example.com/metrics', {
        method: 'POST',
        body: JSON.stringify(metrics),
      });
    },
  };
}
```

## Registering a Plugin

```typescript
import { getHookManager } from '@commander/core';

const hookManager = getHookManager();
hookManager.register(new LoggingPlugin());
```

## Use Cases

- **Audit logging** — Record every LLM call and tool execution
- **Rate limiting** — Custom rate limiting beyond built-in controls
- **Cost tracking** — Monitor token usage across teams
- **Custom metrics** — Send metrics to Datadog, Grafana, etc.
- **Security scanning** — Scan tool inputs/outputs for sensitive data
- **Approval workflows** — Block certain tools or actions pending human approval
