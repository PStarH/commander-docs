# 에이전트 팀

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/advanced/agent-teams)



Commander supports persistent agent teams with inbox messaging for long-running, collaborative workflows.

## 개요


Agent teams allow multiple agents to work together on complex tasks over extended periods. Each agent has its own inbox and can send/receive messages asynchronously.

## Creating a Team


```typescript
import { AgentTeamManager } from '@commander/core';

const team = new AgentTeamManager('team-1');

// Register agents
const leadId = team.registerAgent({
  id: 'lead',
  name: 'Lead Architect',
  role: 'architect',
  capabilities: ['system-design', 'code-review'],
});

const backendId = team.registerAgent({
  id: 'backend',
  name: 'Backend Specialist',
  role: 'engineer',
  capabilities: ['api-design', 'database'],
});

const frontendId = team.registerAgent({
  id: 'frontend',
  name: 'Frontend Specialist',
  role: 'engineer',
  capabilities: ['ui', 'react'],
});
```

## Agent Communication


Agents communicate via persistent inboxes:

```typescript
// Send a message to an agent
await team.sendMessage({
  from: leadId,
  to: backendId,
  subject: 'Design API endpoints',
  body: 'Need a REST API for the user module. Design the endpoints.',
  priority: 'high',
});

// Agent reads its inbox
const inbox = await team.getInbox(backendId);
const messages = inbox.getMessages();

// Agent replies
await team.sendMessage({
  from: backendId,
  to: leadId,
  subject: 'Re: Design API endpoints',
  body: 'Proposed endpoints:\nGET /users\nPOST /users\nGET /users/:id',
});
```

## Team Topologies


### Lead-Driven

One lead agent coordinates specialists. Best for most development workflows.

### Peer-to-Peer

Agents collaborate without a hierarchy. Best for research and analysis.

### Swarm

Multiple agents work on the same problem and vote on the solution. Best for critical decisions.

## Persistence


Agent teams persist across sessions:
- Messages are stored in the inbox store
- Agent states are checkpointed
- Teams can be resumed after restarts

```typescript
// Resume a team from a previous session
const existingTeam = await AgentTeamManager.load('team-1');
```
