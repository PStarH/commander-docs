# CLI コマンド

例はビルド後の `commander` バイナリ。ソースでは次に置き換え:

```bash
npx tsx packages/core/src/cliEntry.ts
```

## タスク実行

| コマンド                                         | 説明                                     |
| ------------------------------------------------ | ---------------------------------------- |
| `commander <task>`                               | クイック分析                             |
| `commander run <task>`                           | フル multi-agent パイプライン            |
| `commander plan <task>`                          | 審議計画（トポロジ・エージェント・予算） |
| `commander run <task> --stream`                  | リアルタイム SSE                         |
| `commander run --file <tasks.json>`              | バッチ                                   |
| `commander swarm` / `drive` / `goal` / `company` | 高度な実行モード                         |

## インターフェース

`gui` · `tui` · `web`

## 分析・設定

`review` · `workers` · `status` · `cost` · `mode` · `config` · `doctor` · `budget` · `--debug`

## Skills / セッション / Saga

`skill *` · `history` · `share` · `saga` · `checkpoint` · `compensation` · `resume` · `undo`

## 例

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
npx tsx packages/core/src/cliEntry.ts doctor
```

## 関連

- [クイックスタート](/ja/guide/getting-started)
- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)
- [設定](/ja/guide/configuration)
