# Web コンソール

Web コンソールは Commander の視覚的な制御面です。ストリーミングエージェントとのチャット、ライブトポロジ、ガバナンス、運用ビューを一箇所で扱います。

## 起動

### 開発（モノレポ）

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...   # または他プロバイダー
pnpm gui
```

| サービス         | 典型 URL              |
| ---------------- | --------------------- |
| API              | http://localhost:4000 |
| Web（Vite 開発） | http://localhost:5173 |

`pnpm gui` は API + Web を起動し、ブラウザを開こうとします。

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

| サービス     | URL                   |
| ------------ | --------------------- |
| API          | http://localhost:4000 |
| Web（Nginx） | http://localhost:3000 |

## できること

| 領域           | 目的                                                                             |
| -------------- | -------------------------------------------------------------------------------- |
| **Dashboard**  | バトルレポート、トークン推移、ライブトポロジ、エージェント名簿、ミッションボード |
| **Chat**       | リアルタイムエージェントストリーム付きの対話実行                                 |
| **Governance** | 承認キュー、ポリシー設定、監査ログ                                               |
| **DLQ**        | デッドレターキューの確認 + 再実行                                                |
| **Security**   | コンプライアンス / 姿勢ビュー（ISO 42001 / NIST AI RMF 志向）                    |
| **Execution**  | ライブ実行フィード、幻覚リスクパネル                                             |
| **Agents**     | 名簿 + 系譜ツリー                                                                |

ラベルは `apps/web` パッケージと共に変わることがあります。ピクセル完璧な UI 仕様ではなく **プロダクトマップ** として読んでください。

## プレビュー

![Commander Web コンソール — ミッションボード、ライブトポロジ、実行フィード、チャット](/console-mockup.svg)

## ヘルスチェック

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## 認証

`COMMANDER_API_KEY` が設定されている場合、API クライアント（コンソール含む）は次を送る必要があります。

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

キーをコミットしないでください。漏えいしたら直ちにローテーションします。

## コンソール vs CLI

| コンソールが向くとき                 | CLI が向くとき                   |
| ------------------------------------ | -------------------------------- |
| 視覚的トポロジと承認が欲しい         | スクリプト、CI、SSH のみのホスト |
| 長いマルチエージェント実行のデバッグ | 一発 `plan` / `run --stream`     |
| 運用（DLQ、監査）                    | 自動化とパッケージング           |

## トラブルシューティング

| 症状        | 対処                                                   |
| ----------- | ------------------------------------------------------ |
| 真っ白な UI | `:4000` の API 稼働を確認；ブラウザコンソールの CORS   |
| 401         | API とクライアントで同じ `COMMANDER_API_KEY`           |
| モデルなし  | `pnpm gui` を起動したシェルでプロバイダーキーを export |
| ポート競合  | 4000/5173/3000 を使っているプロセスを停止              |

詳細: [トラブルシューティング](/ja/guide/troubleshooting) · [デプロイ](/ja/deployment)。

## 関連

- [クイックスタート](/ja/guide/getting-started)
- [インストール](/ja/guide/installation)
- [Agent SDK](/ja/guide/sdk)（プログラマティックな代替）
