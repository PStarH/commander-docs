# Extension Points

Commander is designed to be extended at every layer.

## Plugin System (19 Hook Points)

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentComplete` | Agent run finished |
| `onError` | Run failed |

Hooks can block, modify, or observe the execution.

## Extension Interfaces

### Custom LLM Provider
```typescript
class MyProvider implements LLMProvider {
  async call(messages: Message[], options: CallOptions): Promise<LLMResponse> {
    // Your implementation
  }
}
runtime.registerProvider('my-provider', new MyProvider());
```

### Custom Tool
```typescript
class MyTool implements Tool {
  name = 'my-tool';
  async execute(ctx: ToolContext, args: any): Promise<ToolResult> {
    // Your implementation
  }
}
runtime.registerTool('my-tool', new MyTool());
```

### Custom Topology
Add a new case in `topologyRouter.ts` to define a new orchestration pattern.

### Channel Adapter
```typescript
class TelegramAdapter implements ChannelAdapter {
  // Telegram integration
}
```

### Plugin
```typescript
class MyPlugin implements CommanderPlugin {
  hooks = {
    beforeLLMCall: async (params) => { /* modify params */ },
    afterToolCall: async (result) => { /* observe result */ },
  };
}
getHookManager().register(new MyPlugin());
```

## Meta-Learner

Commander includes a self-evolution system based on **Thompson Sampling + Reflexion**:

- Tracks which strategies work best over time
- Automatically adjusts topology selection
- Learns from failures and successes across runs
