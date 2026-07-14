# マルチエージェント編成

Commander's core differentiator is its ability to orchestrate multiple agents across **5 canonical topologies**, aligned with Anthropic's "Building effective agents" ontology. Nine legacy topology names remain as aliases for backward compatibility during a 2-version migration window. The deliberation engine (`deliberation.ts`) classifies every task and selects the optimal topology:

本ページは Commander における **マルチエージェント編成** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
