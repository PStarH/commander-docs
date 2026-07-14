# Extension Points

**Extension Points.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Hook | When It Fires |
|------|---------------|
| `beforeLLMCall` | Before every LLM request |
| `afterLLMCall` | After every LLM request |
| `beforeToolCall` | Before every tool execution |
| `afterToolCall` | After every tool execution |
| `onAgentComplete` | Agent run finished |
| `onError` | Run failed |


## 주요 내용

### Plugin System (19 Hook Points)

운영 시 **Plugin System (19 Hook Points)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/extension-points)를 보세요.

### Extension Interfaces

운영 시 **Extension Interfaces** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/extension-points)를 보세요.

### Meta-Learner

운영 시 **Meta-Learner** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/extension-points)를 보세요.

## 예제 (코드는 영어 유지)

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

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
