# Custom Tools

**Custom Tools.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 주요 내용

### Tool Interface

운영 시 **Tool Interface** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-tools)를 보세요.

### Example: Webhook Tool

운영 시 **Example: Webhook Tool** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-tools)를 보세요.

### Registering a Tool

운영 시 **Registering a Tool** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-tools)를 보세요.

### Tool Features

운영 시 **Tool Features** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-tools)를 보세요.

### Loading Tools from Files

운영 시 **Loading Tools from Files** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-tools)를 보세요.

## 예제 (코드는 영어 유지)

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
