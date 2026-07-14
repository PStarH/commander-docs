# Custom Tools

**Custom Tools.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 主な内容

### Tool Interface

運用では **Tool Interface** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-tools)を参照してください。

### Example: Webhook Tool

運用では **Example: Webhook Tool** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-tools)を参照してください。

### Registering a Tool

運用では **Registering a Tool** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-tools)を参照してください。

### Tool Features

運用では **Tool Features** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-tools)を参照してください。

### Loading Tools from Files

運用では **Loading Tools from Files** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-tools)を参照してください。

## 例（コードは英語のまま）

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

## 運用

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
