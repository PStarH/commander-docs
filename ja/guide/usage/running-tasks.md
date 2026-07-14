# タスク実行

必要に応じて複数の実行方法があります。

> **monorepo CLI:** `npx tsx packages/core/src/cliEntry.ts …`  
> **ビルド後:** `commander …`

## クイックタスク

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

分析 → トポロジ選択 → 実行 → 結果を一括で返します。

## フルパイプライン

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

1. 審議（複雑度）  
2. 努力スケール（エージェント数）  
3. トポロジ  
4. 原子化（サブタスク）  
5. 実行（tools）  
6. 検証（5 品質ゲート）  

## プラン

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

ファイルを変更せず、複雑度・トポロジ・エージェント・予算を表示します。

## ウォッチ（SSE）

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

## 承認モード

| モード | 挙動 |
|--------|------|
| `plan` | 計画のみ |
| `read-only` | 読み取り |
| `auto-edit` | 自動編集 |
| `full-auto` | 完全自律（CI） |
| `suggest` | 提案して待機 |

```bash
export COMMANDER_MODE=auto-edit
```

## 関連

- [プランモード](/ja/guide/usage/plan-mode)  
- [ウォッチ](/ja/guide/usage/watch-mode)  
- [コマンド](/ja/guide/commands)
