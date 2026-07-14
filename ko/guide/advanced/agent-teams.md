# Agent Teams

Commander supports persistent agent teams with inbox messaging for long-running, collaborative workflows. Agent teams allow multiple agents to work together on complex tasks over extended periods. Each agent has its own inbox and can send/receive messages asynchronously.

이 문서는 Commander에서 **Agent Teams** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
import { AgentTeamManager } from '@commander/core';

const team = new AgentTeamManager('team-1');

// Register agents
const leadId = team.registerAgent({
  id: 'lead',
  name: 'Lead Architect',
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
