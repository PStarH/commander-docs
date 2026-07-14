# ツール

Commander ships with **18 built-in tools** (exposed to the LLM by default, out of 48 tool classes available in the codebase) across 8 categories, each designed for production use with caching, error handling, and rollback support. Every tool comes with:

本ページは Commander における **ツール** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    return { success: true, data: ... };
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
