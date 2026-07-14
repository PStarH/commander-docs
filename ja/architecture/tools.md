# ツール (Tools)

Commander はコードベースにさらに多くのクラスがあっても、LLM には既定で **18 の組み込みツール** を公開します。キャッシュ・エラー処理・ロールバックを前提にした本番向け設計です。

## ファイルシステム

| Tool | 内部名 | 用途 |
|------|--------|------|
| `read` | `file_read` | ファイル読み（行/オフセット） |
| `write` | `file_write` | 作成・上書き |
| `edit` | `file_edit` | 完全一致置換 |
| `glob` / `file_search` | `file_search` | パターン検索 |
| `grep` / `file_list` | `file_list` | 内容検索・一覧 |

## コードインテリジェンス

| Tool | 用途 |
|------|------|
| `ast_grep_search` | AST 検索 |
| `patches` | 構造化パッチ |
| `refine` / `fix` | AI 洗練・修正 |
| `lsp_*` | 診断・シンボル・参照・rename |

## Web & リサーチ

| Tool | 用途 |
|------|------|
| `websearch` / `webfetch` | 検索・URL fetch |
| `browser_*` | ブラウザ描画 |
| `context7_*` | ライブラリ docs |

## コード実行

| Tool | 用途 |
|------|------|
| `bash` / `shell_execute` | サンドボックスシェル |
| `python` / `execute_script` | 隔離実行 |

## メモリ & 永続化

| Tool | 用途 |
|------|------|
| `memory_store` / `memory_recall` / `memory_list` | 永続メモリ |
| `knowledge_search` | RAG 検索（builtin-rag） |

## VCS · メディア

| Tool | 用途 |
|------|------|
| `git` | status, diff, log, commit |
| `look_at` / `vision_analyze` | 画像解析 |
| `pdf_extract` / `screenshot` | PDF・画面 |

## オーケストレーション

| Tool | 用途 |
|------|------|
| `task` / `agent` | サブエージェント委譲 |
| `a2a_delegate` | A2A 委譲 |
| `skill` / `meta` / `verify` | スキル・メタ・検証 |
| `todowrite` / `question` | タスク追跡・質問 |
| `mcp` / `saga` / `checkpoint` | MCP・サガ・チェックポイント |

## 本番機能

- **SHA-256 結果キャッシュ**（テナント隔離）  
- **Compensation registry**  
- **Circuit breaker**  
- **Step error boundary**  
- **Tool call repair**  
- **DLP スキャン**（入力 6 パターン）  

## カスタムツール

```typescript
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    return { success: true, data: {} };
  }
}

runtime.registerTool('my-tool', new MyCustomTool());
```

> monorepo workspace が主経路。  
> CLI: `npx tsx packages/core/src/cliEntry.ts`

## 関連

- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [カスタムツール](/ja/guide/advanced/custom-tools)  
- [MCP](/ja/architecture/mcp)  
- [セキュリティ](/ja/guide/security)  
