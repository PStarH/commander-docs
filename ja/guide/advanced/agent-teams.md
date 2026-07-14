# エージェント・チーム

Commander は、長期・協調ワークフロー向けに **永続インボックス・メッセージング** 付きのエージェント・チームをサポートします。

## 概要

エージェント・チームは、複数エージェントが長時間にわたって複雑な作業を協力できるようにします。各エージェントは独自のインボックスを持ち、非同期でメッセージを送受信します。

## チーム作成

```typescript
import { AgentTeamManager } from "@commander/core";

const team = new AgentTeamManager("team-1");

const leadId = team.registerAgent({
  id: "lead",
  name: "Lead Architect",
  role: "architect",
  capabilities: ["system-design", "code-review"],
});

const backendId = team.registerAgent({
  id: "backend",
  name: "Backend Specialist",
  role: "engineer",
  capabilities: ["api-design", "database"],
});

const frontendId = team.registerAgent({
  id: "frontend",
  name: "Frontend Specialist",
  role: "engineer",
  capabilities: ["ui", "react"],
});
```

> `@commander/core` は monorepo workspace から。npm 公開が主経路になるまでは clone + pnpm を使ってください。

## 通信

永続インボックス経由でメッセージを送ります。

```typescript
await team.sendMessage({
  from: leadId,
  to: backendId,
  subject: "Design API endpoints",
  body: "Need a REST API for the user module. Design the endpoints.",
  priority: "high",
});
```

エージェントはインボックスをポーリングするかイベントバスを購読して作業を続けます。ハンドオフと artifact 参照で情報損失を減らします。

## いつ使うか

| 状況             | 推奨                                        |
| ---------------- | ------------------------------------------- |
| 短い一回限り     | トポロジ自動選択（DISPATCH / ORCHESTRATOR） |
| 数日にわたる協調 | Agent Teams + 永続インボックス              |
| 高リスク検証     | REVIEW トポロジ + チーム・レビュー役割      |

## 関連

- [マルチエージェント](/ja/architecture/multi-agent)
- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)
- [Agent Runtime](/ja/architecture/agent-runtime)
- [SDK](/ja/guide/sdk)
