# Architecture V2 移行

レガシー V1 実行経路から **Architecture V2** 耐久カーネルへ移行します。コントロールプレーンが作業をスケジュールし、ワーカーがステップを実行し、状態は PostgreSQL に置きます。

> 運用の詳細は monorepo の [`docs/v2-migration-guide.md`](https://github.com/PStarH/Commander/blob/master/docs/v2-migration-guide.md)。このページは docs サイト向け要約です。

## メンタルモデル

| プレーン            | 責任                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| **Gateway（制御）** | run 受付、WorkGraph スケジュール、lifecycle（pause/resume/cancel）。純 V2 ではエージェントを実行しない |
| **Worker（実行）**  | ステップを claim し、エージェント/ツールを実行して結果を報告                                           |
| **Kernel storage**  | runs / steps / events の PostgreSQL テーブル                                                           |

## 機能フラグ / 環境変数

| 変数                         | 既定          | 意味                                  |
| ---------------------------- | ------------- | ------------------------------------- |
| `COMMANDER_V2_MODE`          | `0`           | `1` で V2（レガシールート無効）       |
| `NODE_ENV=production`        | —             | 多くの場合 V2 を強制                  |
| `COMMANDER_LEGACY_EXECUTION` | `0`           | 一時的にレガシーを再有効化            |
| `DATABASE_URL`               | —             | V2 カーネルに **必須**                |
| `COMMANDER_WORKER_*`         | monorepo 参照 | worker 種別・同時実行・認証・テナント |

## ルート対応

| Legacy                           | V2                                   |
| -------------------------------- | ------------------------------------ |
| `POST /api/runtime/execute`      | `POST /v1/runs`                      |
| `POST /api/orchestrator/execute` | `POST /v1/runs`（多段グラフ）        |
| `POST /api/chat`                 | `POST /v1/runs`（単一エージェント）  |
| pause / resume / cancel          | `/v1/runs/:id/{pause,resume,cancel}` |

### 主要 V2 エンドポイント

- `POST /v1/runs` · `GET /v1/runs/:id` · steps · events
- lifecycle · human-in-the-loop
- `/health` · `/metrics` · `/v1/slo`

## ストレージ移行

| Legacy                | V2                          |
| --------------------- | --------------------------- |
| SQLite / pod ローカル | PostgreSQL `commander_*`    |
| インメモリ chat       | イベントソーシング再構築    |
| 旧チェックポイント    | **移植不可** — run を再投入 |

```bash
# DATABASE_URL 設定後
pnpm db:migrate   # monorepo の product scripts 参照
```

## Worker スケッチ

```bash
export DATABASE_URL=postgres://...
export COMMANDER_WORKER_AUTH_TOKEN=...
export COMMANDER_WORKER_KIND=agent
# monorepo の worker-plane パッケージで起動
```

## ロールアウト

1. ステージングで dual-run（必要なら `COMMANDER_LEGACY_EXECUTION=1`）
2. カナリアテナントを `POST /v1/runs` へ
3. レガシー無効（`COMMANDER_V2_MODE=1`）
4. `/v1/slo` · DLQ · worker lease を監視

## いつ V1 風ローカル CLI のままか

単機開発の `cliEntry.ts` / SDK `CommanderClient` は最速のままです。V2 が必要になるのは **耐久マルチレプリカ実行** と gateway/worker 分離が要るときです。

## 関連

- [デプロイ](/ja/deployment)
- [本番準備](/ja/architecture/production-readiness)
- [イベントソーシング](/ja/architecture/event-sourcing)
