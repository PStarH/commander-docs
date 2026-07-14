# エージェントランタイム

各エージェントで **LLM → tools → 検証 → リトライ** ループを実行します。

## ループ

1. メッセージ構築  
2. LLM 呼び出し  
3. tool call 解析  
4. ポリシー / サンドボックス下で tool 実行  
5. 結果をコンテキストへ  
6. 品質ゲート  
7. 完了またはリトライ  

## ストリーミング

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
npx tsx packages/core/src/cliEntry.ts watch "task"
```

## 信頼性

tool タイムアウト · 結果キャッシュ · サーキットブレーカー · チェックポイント。

[プロバイダー](/ja/guide/providers) · [Tools](/ja/architecture/tools) · [検証](/ja/architecture/verification)
