# Plugin System

Commander's plugin system provides **19 hook points** to observe, modify, or block execution at any stage. Third-party plugins receive a **sandboxed load context** that strictly limits their permissions. Plugin permissions must never exceed main system permissions.

本ページは Commander における **Plugin System** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { CommanderPlugin } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';

  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] Calling ${params.provider} with ${params.messages.length} messages`);
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
