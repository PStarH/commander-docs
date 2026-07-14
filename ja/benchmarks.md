# ベンチマーク

**ベンチマーク.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

本ページは Commander における **ベンチマーク** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
