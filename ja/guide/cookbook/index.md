# クックブック

エンドツーエンドのレシピです。各ページの型: **ゴール → コマンド → 期待シグナル → 失敗モード**。

| レシピ                                                             | 時間   | 練習すること                            |
| ------------------------------------------------------------------ | ------ | --------------------------------------- |
| [リポジトリのセキュリティ監査](/ja/guide/cookbook/security-audit)  | ~10 分 | DISPATCH 型分析、ストリーミング、ゲート |
| [モジュールを安全にリファクタ](/ja/guide/cookbook/refactor-module) | ~15 分 | Plan → run → review                     |
| [CI フルオート lint 修正](/ja/guide/cookbook/ci-full-auto)         | ~15 分 | 非対話モード、exit code                 |

## 共通前提

すべてのレシピは `pnpm install` 後の Commander モノレポルートにいて、API キー 1 つが export 済みだと仮定します。

```bash
# ソースチェックアウト
npx tsx packages/core/src/cliEntry.ts <command>

# @commander/core ビルド後
commander <command>
```

初めてなら [クイックスタート](/ja/guide/getting-started) から。
