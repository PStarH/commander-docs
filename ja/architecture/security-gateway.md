# Enterprise Security Gateway

Commander's `EnterpriseSecurityGateway` provides a 7-layer defense-in-depth architecture that is invoked during all LLM calls and tool executions. It cannot be bypassed — cost checks execute both before and after LLM calls. - **Defense in depth** — Multiple independent layers, each with distinct responsibility

本ページは Commander における **Enterprise Security Gateway** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
entry_1 → SHA256(prev_hash | entry_1) → hash_1
entry_2 → SHA256(hash_1 | entry_2) → hash_2
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
