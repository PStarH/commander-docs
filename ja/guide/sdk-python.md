# Python SDK

Commander provides a Python SDK for integrating multi-agent orchestration into Python applications. It is a thin **HTTP client** against a running Commander API server — not an in-process runtime. For scripts and non-async contexts:

本ページは Commander における **Python SDK** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
