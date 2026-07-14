# Benchmarks

**Benchmarks.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Suite | Coverage | Result (as documented) |
|-------|----------|------------------------|
| Chaos Engineering | 255 synthetic + 55 mutation | 55.7% pass rate |
| Red Team | 47 scenarios, 8 attack categories | 100% defense |
| AgentDojo | 12 security test cases | 100% defense |
| RealWorld | 50 production-like cases | 96% pass rate |
| GAIA Spine | Core capability | Running daily |
| SLO | API success / latency | Measured daily |


## 主な節

### Headline matrix (product README)

**Headline matrix (product README)** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Reliability SLO Targets

**Reliability SLO Targets** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Health Check Components

**Health Check Components** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Chaos Engineering Benchmark

**Chaos Engineering Benchmark** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Topology Performance

**Topology Performance** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Provider Latency

**Provider Latency** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Test Suite

**Test Suite** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Reproducing Benchmarks

**Reproducing Benchmarks** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```bash
pnpm benchmark:all          # multi-suite readiness
pnpm benchmark:redteam      # 47 scenarios
pnpm benchmark:agentdojo    # injection suite
pnpm benchmark:chaos        # chaos (simulated default)
pnpm bench:slo              # SLO baseline
pnpm check:readiness        # baseline freshness
```
```bash
# Run full 255-case benchmark
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=bench --duration=300

# Run specific domain
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=bench --fault-types=payment_timeout,rate_limit
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
