# エンタープライズ・セキュリティゲートウェイ

`EnterpriseSecurityGateway` は、すべての LLM 呼び出しとツール実行に適用される **7 層の防衛深度** です。迂回できません。コスト検査は LLM 呼び出しの **前後両方** で実行されます。

## 7 層防衛

| 層  | 名前                 | 役割                                     |
| --- | -------------------- | ---------------------------------------- |
| 1   | Zero-Trust Signature | 完全性検証 + リプレイ防止                |
| 2   | Authentication       | タイミング安全な API Key 検証            |
| 3   | Rate Limiting        | グローバルトークンバケット + IP 階層制限 |
| 4   | Input Scanning       | インジェクション検出 + 入力検証          |
| 5   | Cost Pre-Check       | 請求爆発の防止（事前見積もり）           |
| 6   | Request Processing   | ビジネスロジック実行                     |
| 7   | Output Scanning      | DLP 漏洩防止 + コスト記録                |

### 設計原則

- **防衛深度** — 独立した層、責任分離
- **Fail fast** — 最も安い層で早期拒否
- **観測可能** — すべての決定にセキュリティメタデータをログ
- **テナント隔離** — 検査はテナント単位
- **迂回不可** — コスト検査は呼び出し前後

## DLP（Data Loss Prevention）

`dataLossPrevention.ts` がすべての egress を 5 段パイプラインでスキャンします。

### 検出パターン（12+）

API Key · JWT · PEM 秘密鍵 · クレジットカード（Luhn）· SSN · Email/Phone · 内部 IP · DB 接続文字列 · クラウド資格情報 · その他。

### リダクション戦略

| 戦略     | 動作                |
| -------- | ------------------- |
| `REDACT` | `[REDACTED]` に置換 |
| `MASK`   | 部分マスク          |
| `HASH`   | SHA-256             |
| `ALLOW`  | 通過（ログのみ）    |

適用点: API 応答 · ログ · ツール結果 · エージェント出力 · SSE ストリーム。

ツール入力は実行前に API Key / Private Key / AWS / GitHub Token / JWT / Password をスキャンします。

## Capability Tokens

`capabilityToken.ts` が短命 HMAC 署名トークンを発行します。短い TTL · スコープ束縛 · 改ざん耐性 · 期限前失効。ツール実行点で検証必須。

## Audit Chain Ledger

`auditChainLedger.ts` がセキュリティイベントをハッシュ鎖で記録し、改ざん検知を可能にします。

## 運用

```bash
export COMMANDER_API_KEY="long-random-secret"
npx tsx packages/core/src/cliEntry.ts doctor
curl -s http://localhost:4000/health/detailed
```

TLS・認証なしで `:4000` を公開しないでください。メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

## 関連

- [セキュリティ](/ja/guide/security)
- [本番準備](/ja/architecture/production-readiness)
- [マルチテナント](/ja/architecture/multi-tenancy)
- [Sandbox](/ja/architecture/sandbox)
