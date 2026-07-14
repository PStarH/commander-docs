# Python SDK

**Python SDK.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Method | Description |
|--------|-------------|
| `client.run(prompt, ...)` | Execute an agent task |
| `client.plan(task, ...)` | Zero-cost deliberation (no LLM call) |
| `client.stream(session_id)` | SSE event stream for a running session |
| `client.memory_write(content, ...)` | Write to memory |
| `client.memory_query(...)` | Query memory |
| `client.memory_stats()` | Memory statistics |
| `client.health()` | Liveness probe |
| `client.health_detailed()` | Detailed component health |
| `client.system_status()` | System status |
| `client.metrics()` | OpenMetrics text |


## 主な内容

### Installation

運用では **Installation** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### Quick Start

運用では **Quick Start** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### API Reference

運用では **API Reference** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### Streaming

運用では **Streaming** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### Sync Wrapper

運用では **Sync Wrapper** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### 設定

運用では **Configuration** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### 構造

運用では **Architecture** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

### Development

運用では **Development** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/sdk-python)を参照してください。

## 例（コードは英語のまま）

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

```bash
pip install commander-ai
```

```python
import asyncio
from commander import CommanderClient

async def main():
    async with CommanderClient(
        api_key="cmd-...",
        base_url="http://localhost:4000",
    ) as client:
        # Zero-cost planning
        plan = await client.plan("audit repository for security vulnerabilities")
        print(f"Topology: {plan.topology}")
        print(f"Budget: ${plan.estimate.cost_budget_usd:.2f}")

        # Execute
        result = await client.run("list all Python files")
        print(f"Status: {result.status}")

asyncio.run(main())
```

## 運用

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
