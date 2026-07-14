# セキュリティ

Commander はコード・ツール・信頼できないモデル出力を扱うマルチエージェント負荷向けです。運用者向け要約。深掘り: [Security Gateway](/ja/architecture/security-gateway)、[Sandbox](/ja/architecture/sandbox)、[マルチテナント](/ja/architecture/multi-tenancy)。

## 脆弱性の報告

**セキュリティバグを公開 GitHub Issue にしないでください。**

**sampan090611@gmail.com** に次を送ってください。

- 種類と影響
- パス / コミット
- 再現手順
- 可能なら PoC

**48 時間以内** の受領確認を目指します（製品 [SECURITY.md](https://github.com/PStarH/Commander/blob/master/SECURITY.md)）。

## 脅威モデル（要約）

| 脅威                    | 緩和                                                    |
| ----------------------- | ------------------------------------------------------- |
| プロンプト / ツール注入 | ツール出力スキャン、sanitizer、不可逆ツールの可逆ゲート |
| シークレット漏洩        | DLP、シークレットを出さない構造化ログ                   |
| 暴走エージェント        | 承認モード、トークン予算、タイムアウト、ブレーカー      |
| プロバイダー障害 / 乱用 | フェイルオーバー、rate limit、テナントクォータ          |
| クロステナント          | ストレージ・メモリ・キャッシュ・rate limit 隔離         |
| サプライチェーン        | CI npm audit；キーを git に入れない                     |

## 設定すべきコントロール

### 1. 承認モード

| モード      | 用途                   |
| ----------- | ---------------------- |
| `plan`      | プレビューのみ         |
| `read-only` | 分析 / 監査            |
| `suggest`   | 人が書き込み承認       |
| `auto-edit` | 信頼できるローカル開発 |
| `full-auto` | PR レビュー付き CI     |

```bash
export COMMANDER_MODE=read-only
```

### 2. API 認証

```bash
export COMMANDER_API_KEY="long-random-secret"
```

Bearer 必須。TLS・認証なしで `:4000` を公開しない。

### 3. ネットワーク

API は localhost 寄り。本番はリバースプロキシで TLS・認証（[デプロイ](/ja/deployment)）。

### 4. 機微コード

**Ollama / vLLM** でコードを外に出さない:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
```

### 5. マルチテナント本番

テナントプロバイダーとクォータ — [マルチテナント](/ja/architecture/multi-tenancy)。

## セキュリティベンチマーク

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

詳細: [ベンチマーク](/ja/guide/benchmarks)。

## 関連

- [本番準備](/ja/architecture/production-readiness)
- [Web コンソール](/ja/guide/web-console)
- [FAQ](/ja/guide/faq)
