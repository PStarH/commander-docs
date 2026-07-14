# Puntos de extensión

Documentación en español de **Puntos de extensión**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentComplete` | Agent run finished |
| `onError` | Run failed |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
