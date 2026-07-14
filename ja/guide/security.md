# セキュリティ

**脆弱性報告:** 公開 Issue 禁止 — **sampan090611@gmail.com**（目安 48 時間以内に受領）。

## 脅威と対策

| 脅威 | 対策 |
|------|------|
| プロンプト / tool 注入 | 出力スキャン、sanitizer、不可逆 tool ゲート |
| 秘密情報漏洩 | DLP、秘密を出さないログ |
| 暴走エージェント | 承認モード、トークン予算、timeout、breaker |
| プロバイダー障害 | フェイルオーバー、rate limit |
| テナント横断 | ストレージ / メモリ / キャッシュ分離 |

## 設定

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export OLLAMA_BASE_URL=http://localhost:11434
export COMMANDER_SECURITY_PROFILE=standard
```

## ベンチマーク

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

[ゲートウェイ](/ja/architecture/security-gateway) · [サンドボックス](/ja/architecture/sandbox)
