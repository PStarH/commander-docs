# 本番準備

| 能力 | 実装 |
|------|------|
| Circuit breakers | プロバイダー単位 |
| DLQ | 再送可能 |
| Saga | ミューテーション補償 |
| Checkpoints | SQLite WAL |
| Semantic cache | SHA-256 + 類似度 |
| Multi-tenant | クォータ / 分離 |
| Metrics | Prometheus |

```bash
curl http://localhost:4000/health/detailed
curl http://localhost:4000/metrics
```

6700+ tests in CI.

[デプロイ](/ja/deployment) · [レジリエンス](/ja/architecture/resilience)
