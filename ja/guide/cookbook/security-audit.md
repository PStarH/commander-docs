# Cookbook: Security audit a repository

**Goal:** Run a multi-agent security-oriented audit with live streaming and readable findings. **Time:** ~10 minutes · **Risk:** read-heavy (prefer `read-only` or `plan` first)

本ページは Commander における **Cookbook: Security audit a repository** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
cd /path/to/Commander   # monorepo root
export OPENAI_API_KEY=sk-...   # or any supported key
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
