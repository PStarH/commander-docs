# 設定

Commander is configured through environment variables and configuration files. Commander supports a `.commander.json` config file in your project root:

本ページは Commander における **設定** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
| Field | Default | Description |
|-------|---------|-------------|
| `provider` | `auto` | Primary LLM provider |
| `model` | `auto` | Model name |
| `mode` | `balanced` | Execution mode: `fast`, `balanced`, `thorough` |
| `topology` | `auto` | Orchestration topology: `auto`, `single`, `chain`, `dispatch`, `orchestrator`, `review` |
| `budget` | `auto` | Token budget (integer ≥1000 or `auto`) |
| `mcpServers` | `[]` | MCP server configurations |
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
