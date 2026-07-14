# Web 控制台

可视化控制面：流式对话、实时拓扑、治理与运维视图。

## 启动

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
pnpm gui
```

| 服务 | 常见地址 |
|------|----------|
| API | http://localhost:4000 |
| Web（Vite 开发） | http://localhost:5173 |

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## 能力地图

| 区域 | 用途 |
|------|------|
| **Dashboard** | 战报、Token 趋势、拓扑、代理名册 |
| **Chat** | 带实时流的对话执行 |
| **Governance** | 审批队列、策略、审计 |
| **DLQ** | 死信查看与重放 |
| **Security** | 合规 / 态势 |
| **Execution** | 执行流、幻觉风险面板 |
| **Agents** | 名册与谱系 |

## 健康检查

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics
```

若设置了 `COMMANDER_API_KEY`，请求需带：

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

## 控制台 vs CLI

| 用控制台 | 用 CLI |
|----------|--------|
| 可视化拓扑与审批 | 脚本 / CI / 仅 SSH |
| 长任务调试 | 一次性 `plan` / `run --stream` |
| 运维（DLQ、审计） | 自动化打包 |

英文完整版：[Web Console](/guide/web-console)。
