# Chaos Testing

**Chaos Testing.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Layer | Name | What it injects |
|-------|------|----------------|
| **L1** | LLM | Provider-level faults: rate limits, timeouts, context window overflow, malformed responses |
| **L2** | Tool | 10 failure modes: `http_5xx`, `http_4xx`, `disk_full`, `oom`, `process_crash`, `state_corrupt`, `dependency_unavailable`, `time_drift`, `auth_expired`, `http_timeout` |
| **L3** | System | Process/disk/CPU/memory faults: CPU throttle, memory pressure, disk full simulation |
| **L4** | Tenant | Multi-tenant blast radius enforcement: cross-tenant access attempts, resource exhaustion |


## 主な節

### Quick Start

**Quick Start** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Chaos Layers

**Chaos Layers** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Running Chaos Tests

**Running Chaos Tests** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Recovery Verification

**Recovery Verification** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Adding New Scenarios

**Adding New Scenarios** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Programmatic API

**Programmatic API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### CI Integration

**CI Integration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```bash
# Run a single-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Run multi-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# With recovery verification (default)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```
```bash
# LLM provider faults only
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1

# Tool failure injection
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L2

# System-level faults
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L3

# Tenant isolation testing (requires --tenant)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L4 --tenant=ci-staging
```

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
