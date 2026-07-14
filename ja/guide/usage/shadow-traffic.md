# シャード・トラフィック（Shadow Traffic）

シャード・トラフィックは本番に影響を与えず、Commander の 2 バージョンを **並べて比較** します。シャード・プロキシが本番リクエストをシャード端点へミラーし、status・latency・cost のドリフトを報告します。

## 用途

- **デプロイ前検証** — 現行 vs 候補
- **プロバイダー移行** — OpenAI → Anthropic などを低リスクで試験
- **設定変更** — 新しいトポロジ・ルーティングの検証
- **回帰検知** — 性能・品質の劣化を早期発見

## クイックスタート

### 1. 設定

```bash
cat > .commander/shadow-config.json <<EOF
{
  "enabled": true,
  "endpoint": "http://localhost:9999",
  "sampleRate": 0.1,
  "scrubPii": true,
  "diffMode": "status_cost_latency",
  "timeoutMs": 5000
}
EOF
```

### 2. シャード・ランナー

```bash
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &
```

### 3. 本番でプロキシ有効化

```bash
export COMMANDER_SHADOW_ENABLED=true
npx tsx packages/core/src/cli/index.ts serve
```

### 4. ドリフト報告

```bash
npx tsx packages/core/src/cli/commands/shadow.ts drift
```

> monorepo のパスは製品版で変わることがあります。最新の入口は `packages/core/src/cliEntry.ts` と monorepo ドキュメントを確認してください。

## 設定の要点

| フィールド   | 意味                         |
| ------------ | ---------------------------- |
| `endpoint`   | シャード先 URL               |
| `sampleRate` | ミラー比率 (0–1)             |
| `scrubPii`   | PII スクラブ                 |
| `diffMode`   | status / cost / latency 比較 |
| `timeoutMs`  | タイムアウト                 |

## 運用上の注意

- mutation 付きリクエストはサンプル率を下げるか除外
- コストが二重になるため `sampleRate` は保守的に
- ドリフトが大きい場合は候補をロールバックし、トポロジ・プロバイダーを見直す

## 関連

- [デプロイ](/ja/deployment)
- [本番準備](/ja/architecture/production-readiness)
- [ベンチマーク](/ja/guide/benchmarks)
- [トラブルシューティング](/ja/guide/troubleshooting)
