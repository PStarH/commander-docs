# 検証パイプライン

結果返却前に **5 品質ゲート** を適用します。

| ゲート | 内容 |
|--------|------|
| Hallucination | 捏造 |
| Consistency | 矛盾なし |
| Completeness | 必要次元の充足 |
| Accuracy | ソース整合 |
| Safety | 注入・秘密情報など |

失敗時はコンテキスト付きリトライ、または明示的失敗報告。

[ランタイム](/ja/architecture/agent-runtime) · [セキュリティ](/ja/guide/security)
