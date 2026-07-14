# セキュリティ

Commander is designed for multi-agent workloads that touch code, tools, and untrusted model output. This page is the operator-facing summary. Deep dives: [Security Gateway](/architecture/security-gateway), [Sandbox](/architecture/sandbox), [Multi-Tenancy](/architecture/multi-tenancy). **Do not open public GitHub issues for security bugs.**

本ページは Commander における **セキュリティ** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
export COMMANDER_MODE=read-only
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
