# Smart Model Router

The Smart Model Router provides **capability-based model selection** with user-configurable routing rules. It wraps the core `ModelRouter` with an extended API for defining model pools, routing rules, and budget constraints. Models are tagged with capability types for matching:

本ページは Commander における **Smart Model Router** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
