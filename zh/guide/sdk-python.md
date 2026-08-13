# Python SDK

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/guide/sdk-python)



Commander provides a Python SDK for integrating multi-agent orchestration into Python applications. It is a thin **HTTP client** against a running Commander API server — not an in-process runtime.

## 安装


### From the monorepo (recommended today)


```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

### When published to PyPI


```bash
pip install commander-ai
```

> Package name: `commander-ai` · import: `from commander import CommanderClient`

## 快速开始


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

## API 参考


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

## Streaming


```python
async for event in client.stream(session_id):
    if event.event == "output.delta":
        print(event.data["content"], end="", flush=True)
    elif event.event == "agent.status":
        print(f"\n[{event.data['status']}]")
    elif event.event == "tool_call.started":
        print(f"\n[Tool: {event.data['toolName']}]")
```

### Event Types


| Event | Description |
|-------|-------------|
| `output.delta` | Streaming text output chunk |
| `output.completed` | Output stream finished |
| `agent.status` | Agent status change |
| `reasoning.delta` | Agent reasoning chunk |
| `tool_call.started` | Tool call initiated |
| `tool_call.completed` | Tool call finished |
| `tool_call.delta` | Tool call streaming output |
| `tool_call.timeout` | Tool call timed out |
| `tool_call.retry` | Tool call retried |
| `tool_call.blocked` | Tool call blocked by approval gate |
| `error.occurred` | Error during execution |
| `state.sync` | State synchronization |
| `cost.update` | Token cost update |
| `compensation.update` | Compensation status update |

## Sync Wrapper


For scripts and non-async contexts:

```python
from commander import CommanderClientSync

client = CommanderClientSync(
    api_key="cmd-...",
    base_url="http://localhost:4000",
)
result = client.run("analyze this")
client.close()
```

> Not for Jupyter/notebooks — use `CommanderClient` with `asyncio` there.

## 配置


| Env var | Default | Description |
|---------|---------|-------------|
| `COMMANDER_API_KEY` | — | API key for Bearer auth |
| — | `http://localhost:4000` | Commander server base URL |

## Architecture


```
Python SDK → HTTP → Commander Server → Runtime
```

The SDK is a thin `httpx` client — no Python-side runtime porting.

## Development


```bash
git clone https://github.com/PStarH/Commander.git
cd packages/python-sdk
pip install -e ".[dev]"
python -m pytest tests/ -v
```
