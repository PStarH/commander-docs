# アーキテクチャ概要

Commander はタスク記述を、複数エージェント・tools・LLM プロバイダーにまたがる構造化実行計画へ変換する multi-agent オーケストレーションエンジンです。

## まずこの 5 ページ

1. **本ページ** — 全体フロー  
2. [コア呼び出しチェーン](/ja/architecture/core-call-chain)  
3. [マルチエージェント](/ja/architecture/multi-agent)  
4. [エージェントランタイム](/ja/architecture/agent-runtime)  
5. [検証パイプライン](/ja/architecture/verification)  

## ハイレベルフロー

```
CLI / HTTP / SDK
  → 審議 (分類・複雑度)
  → 努力スケール (1–20 agents)
  → トポロジ (SINGLE…REVIEW)
  → ランタイム (LLM ↔ tools)
  → 品質ゲート (5 層)
  → 合成・永続化・メトリクス
```

## 設計原則

1. トポロジ優先  
2. プロバイダー非依存 (25 + fallback)  
3. クラッシュ安全 (SQLite WAL)  
4. デフォルトで観測可能 (SSE / metrics)  
5. マルチテナント設計  
6. デフォルトセキュア  
7. 可逆 (event sourcing / 補償)  

## 関連

- [本番準備](/ja/architecture/production-readiness)  
- [セキュリティ](/ja/guide/security)  
- [クイックスタート](/ja/guide/getting-started)
