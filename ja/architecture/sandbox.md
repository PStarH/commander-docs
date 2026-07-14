# セキュリティサンドボックス

**セキュリティサンドボックス.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

本ページは Commander における **セキュリティサンドボックス** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
sandbox/
├── execPolicy.ts           ← Execution policy definitions
├── approval.ts             ← Approval workflow for sensitive operations
├── profiles.ts             ← Security profiles (READ_ONLY, WORKSPACE_WRITE, FULL_ACCESS, HARDENED)
├── platforms.ts            ← Platform-specific sandbox configurations
├── manager.ts              ← Sandbox lifecycle management
├── executionRouter.ts      ← Route executions to appropriate backends
├── lane.ts                 ← Execution lane management
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
