# Agent Teams

Commander supports persistent agent teams with inbox messaging for long-running, collaborative workflows. Agent teams allow multiple agents to work together on complex tasks over extended periods. Each agent has its own inbox and can send/receive messages asynchronously.

本ページは Commander における **Agent Teams** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { AgentTeamManager } from '@commander/core';

const team = new AgentTeamManager('team-1');

// Register agents
const leadId = team.registerAgent({
  id: 'lead',
  name: 'Lead Architect',
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
