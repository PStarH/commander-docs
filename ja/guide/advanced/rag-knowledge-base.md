# RAG Knowledge Base

Commander includes a built-in optional RAG (Retrieval-Augmented Generation) plugin that provides knowledge base search capabilities without requiring external services. The `builtin-rag` plugin is a `CommanderPlugin` with category `integration`, **disabled by default**. It provides:

本ページは Commander における **RAG Knowledge Base** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# Enable via CLI
commander plugin enable rag

# Or in .commander.json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
