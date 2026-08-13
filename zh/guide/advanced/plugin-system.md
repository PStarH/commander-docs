# 插件系统

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/guide/advanced/plugin-system)



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

## Plugin Security


Third-party plugins receive a **sandboxed load context** that strictly limits their permissions. Plugin permissions must never exceed main system permissions.

### Sandboxed Load Context


The `buildSandboxedLoadContext()` method constructs a restricted context for third-party plugins:

```typescript
// Third-party plugins only receive:
const sandboxContext = {
  registerHook: enforcer.wrapRegisterHook(...),
  readFile: enforcer.wrapReadFile(...),
  writeFile: enforcer.wrapWriteFile(...),  // files written with mode 0o600
  fetch: enforcer.wrapFetch(...),          // domain + port checked
  getEnvVar: enforcer.wrapGetEnvVar(...),
  getConfig: enforcer.wrapGetConfig(...),
  log: enforcer.wrapLog(...),
};
// The raw HookManager is NOT included — prevents privilege escalation
```

Built-in plugins (without an enforcer) still receive the full `HookManager`.

### Permission Enforcement


| Mechanism | Behavior |
|-----------|----------|
| `register()` | Third-party plugins get sandboxed context, not raw HookManager |
| `updateConfig()` | Routes through same sandboxed context as `register()` |
| `withTimeout()` | Uses `Math.min(plugin.maxExecutionTimeMs, globalTimeoutMs)` — stricter value wins |
| Network requests | URL-parsed, hostname/port checked via `enforcer.checkNetwork()` |
| File writes | Enforced to mode `0o600` |
| Failures | Reported via `reportSilentFailure` (never throws to plugin) |

### Security Hardening (v0.2.1)


Three privilege escalation vulnerabilities were identified and fixed:

1. **GAP-1**: `register()` leaked raw `HookManager` → sandbox bypass → Fixed with `buildSandboxedLoadContext()`
2. **GAP-2**: `updateConfig()` bypassed sandbox entirely → Fixed by reusing sandboxed context
3. **GAP-3**: `withTimeout()` ignored plugin's `maxExecutionTimeMs` → DoS risk → Fixed with `Math.min()` enforcement

47 test scenarios in `tests/pluginPermissions.test.ts` verify the sandbox is enforced.

## Use Cases


- **Audit logging** — Record every LLM call and tool execution
- **Rate limiting** — Custom rate limiting beyond built-in controls
- **Cost tracking** — Monitor token usage across teams
- **Custom metrics** — Send metrics to Datadog, Grafana, etc.
- **Security scanning** — Scan tool inputs/outputs for sensitive data
- **Approval workflows** — Block certain tools or actions pending human approval
- **RAG integration** — Built-in `builtin-rag` plugin provides knowledge base search
