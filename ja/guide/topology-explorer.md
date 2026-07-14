# 対話型トポロジエクスプローラー

Pick a task shape. Commander’s deliberation engine maps similar signals onto one of **five canonical topologies**. This page is a decision aid — not a substitute for `plan`. Answer mentally, then confirm with `plan`:

本ページは Commander における **対話型トポロジエクスプローラー** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Is the task a single clear question with one owner?
  YES → SINGLE
  NO  ↓
Does work form a strict pipeline (A then B then C)?
  YES → CHAIN
  NO  ↓
Can specialists work in parallel then merge?
  YES → DISPATCH
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
