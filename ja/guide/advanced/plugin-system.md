# プラグイン・システム

Commander プラグインはランタイム・フックで挙動を拡張します。サードパーティは **サンドボックス読み込み文脈** で権限昇格を防ぎます。

## 概要

- **19 フック** — LLM 前後、ツール前後、run 前後など  
- **権限上限** — メインを超えない  
- **タイムアウト** — プラグインごと `maxExecutionTimeMs`  
- **内蔵例** — `builtin-rag`（既定オフ）  

## 有効化例 (RAG)

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
```

または `.commander.json` で `builtin-rag.enabled: true`。

## カスタム

`CommanderPlugin` を実装して登録。ロードはサンドボックス経由。ネットワーク・ファイル権限はプロファイルに従う。

## セキュリティ

スキャン · 権限宣言 · タイムアウト · 例外隔離。[Sandbox](/ja/architecture/sandbox) · [セキュリティ](/ja/guide/security)。

## 関連

- [RAG](/ja/guide/advanced/rag-knowledge-base)  
- [拡張ポイント](/ja/architecture/extension-points)  
- [本番準備](/ja/architecture/production-readiness)  
