# アーキテクチャ概要

Commander is a multi-agent orchestration engine that transforms a single task description into a structured execution plan across multiple agents, tools, and LLM providers. If you are new, this is enough to understand the system:

本ページは Commander における **アーキテクチャ概要** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         Task analysis & topology selection
  ├─ effortScaler.ts         Scale agents (1-20) by complexity
  ├─ topologyRouter.ts       Route to optimal topology (5 canonical + 9 legacy)
  ├─ atomizer.ts             ROMA task decomposition
  │
  ├─ agentRuntime.ts         LLM → tools → verification → retry
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
