# 에이전트 팀

Commander는 장기·협업 워크플로를 위해 **영속 인박스 메시징**이 있는 에이전트 팀을 지원합니다.

## 개요

에이전트 팀은 여러 에이전트가 긴 시간 동안 복잡한 작업을 함께 하도록 합니다. 각 에이전트는 자체 인박스를 가지며 비동기로 메시지를 주고받습니다.

## 팀 생성

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

> `@commander/core`는 monorepo workspace에서 가져옵니다. npm 공개가 주 경로가 되기 전까지 clone + pnpm을 사용하세요.

## 통신

영속 인박스를 통해 메시지를 보냅니다.

```typescript
await team.sendMessage({
  from: leadId,
  to: backendId,
  subject: "Design API endpoints",
  body: "Need a REST API for the user module. Design the endpoints.",
  priority: "high",
});
```

에이전트는 인박스를 폴링하거나 이벤트 버스를 구독해 작업을 이어갑니다. 핸드오프와 artifact 참조는 정보 손실을 줄입니다.

## 언제 쓰나

| 상황             | 추천                                         |
| ---------------- | -------------------------------------------- |
| 짧은 일회 작업   | 토폴로지 자동 선택 (DISPATCH / ORCHESTRATOR) |
| 며칠에 걸친 협업 | Agent Teams + 영속 인박스                    |
| 고위험 검증      | REVIEW 토폴로지 + 팀 리뷰 역할               |

## 관련

- [멀티 에이전트](/ko/architecture/multi-agent)
- [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree)
- [Agent Runtime](/ko/architecture/agent-runtime)
- [SDK](/ko/guide/sdk)
