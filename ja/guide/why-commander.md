# なぜ Commander か

Commander は、マルチエージェントを **ブラックボックスにしたくないエンジニア** 向けです。

**グラフビルダーなし。YAML なし。祈らない。**  
キー 1 つ → タスク分類 → トポロジ選択 → 全決定をストリーム → 出力を検証。

## 一覧

| 観点 | Commander | 典型的なフレームワーク |
|------|-----------|------------------------|
| 始め方 | 自然言語 + キー 1 つ | グラフ / YAML を組む |
| トポロジ | 5 種を自動選択 | 自分で辺を張る |
| 可視性 | ライブ SSE | 事後ログ |
| 品質 | 5 層ゲート | 任意 / DIY |
| プロバイダー | 25 + フェイルオーバー | 1–2 が中心 |
| 本番 | ブレーカー、DLQ、Saga、WAL | デモ優先 |

## 60 秒体験

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

- [クイックスタート](/ja/guide/getting-started)  
- [英語版 Why](/guide/why-commander)  
