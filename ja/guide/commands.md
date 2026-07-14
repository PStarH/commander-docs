# CLI コマンド

ビルド後は `commander`。ソースからは:

```bash
npx tsx packages/core/src/cliEntry.ts
```

## 実行

| コマンド | 説明 |
|----------|------|
| `commander run <task>` | フル multi-agent 実行 |
| `commander plan <task>` | 審議プラン表示 |
| `commander run <task> --stream` | SSE ストリーム |
| `commander run --file tasks.json` | バッチ |
| `swarm` / `drive` / `goal` / `company` | 高度モード |

## UI

`gui` · `tui` · `web`

## 設定・診断

`mode` · `config` · `doctor` · `budget` · `status` · `cost` · `--debug`

## 承認モード

`plan` · `read-only` · `suggest` · `auto-edit` · `full-auto`

```bash
export COMMANDER_MODE=plan
commander mode plan
```
