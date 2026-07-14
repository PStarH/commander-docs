# 検証パイプライン

Every agent output passes through a 5-gate quality verification pipeline before it is returned to the caller. This is not a "nice-to-have" check — it is an integral part of the runtime retry loop. The `UnifiedVerificationPipeline` orchestrates all 5 gates:

本ページは Commander における **検証パイプライン** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ Signal-based detector with configurable thresholds
  │
  ├─ Gate 2: Consistency Check
  │   └─ Internal consistency and contradiction detection
  │
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
