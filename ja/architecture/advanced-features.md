# Advanced Engine Features

**Advanced Engine Features.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

本ページは Commander における **Advanced Engine Features** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();

// Run 3 speculative paths in parallel
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
