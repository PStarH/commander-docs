# マルチエージェント編成

| トポロジ | パターン |
|----------|----------|
| SINGLE | 1 エージェント |
| CHAIN | 順次パイプライン |
| DISPATCH | 並列 + 合成 |
| ORCHESTRATOR | リード + workers |
| REVIEW | 生産 + 批評 |

```bash
npx tsx packages/core/src/cliEntry.ts run "audit" --topology dispatch --stream
```

メッセージバス · ハンドオフ · トークン予算 · 合成。

[トポロジエクスプローラー](/ja/guide/topology-explorer) · [ランタイム](/ja/architecture/agent-runtime)
