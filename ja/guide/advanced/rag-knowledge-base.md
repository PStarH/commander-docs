# RAG ナレッジベース

Commander には、外部サービスなしで知識検索を提供する任意の **RAG（Retrieval-Augmented Generation）** プラグインが含まれます。

## 概要

`builtin-rag` はカテゴリ `integration` の `CommanderPlugin` で、**既定は無効**です。

- ドキュメント取り込み（チャンク + 埋め込み）
- 高速類似検索用 HNSW ベクトルインデックス
- （任意）LLM 呼び出し前のコンテキスト自動注入
- OpenAI またはローカル埋め込み（ゼロ依存 fallback）

## 有効化

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag

# または .commander.json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
}
```

## 設定

| オプション       | 既定                         | 説明                         |
| ---------------- | ---------------------------- | ---------------------------- |
| `kbPath`         | `.commander/knowledge-base/` | ドキュメント・ベクトル保存先 |
| `embeddingModel` | `text-embedding-3-small`     | OpenAI 埋め込みモデル        |
| `chunkSize`      | `512`                        | チャンク文字数               |
| `chunkOverlap`   | `50`                         | オーバーラップ               |
| `maxResults`     | `5`                          | 最大検索件数                 |
| `autoInject`     | `false`                      | LLM 前の自動注入             |

## 埋め込み戦略

1. **OpenAI** — `OPENAI_API_KEY` があるとき
2. **ローカル** — オフライン用ゼロ依存 fallback

## ベクトル検索

`memory/hnswIndex.ts` の HNSW を使用。

- **1000+** エンティティ: 近似最近傍
- それ以下: brute-force 厳密検索
- `bruteForceThreshold` 既定 1000

## 取り込み

```
Document → Chunk (512, overlap 50) → Embed → Index (HNSW) → Persist
```

- `kb-documents.json` — メタデータ
- `kb-vectors.json` — チャンク + 埋め込み
- 書き込みは temp + rename で atomic

## API（有効時）

| Endpoint                     | Method   | 用途         |
| ---------------------------- | -------- | ------------ |
| `/api/knowledge-base`        | `GET`    | 一覧         |
| `/api/knowledge-base`        | `POST`   | アップロード |
| `/api/knowledge-base/:id`    | `DELETE` | 削除         |
| `/api/knowledge-base/search` | `POST`   | 検索         |

## 関連

- [プラグインシステム](/ja/guide/advanced/plugin-system)
- [Three-layer memory](/ja/api/three-layer-memory)
- [セキュリティ](/ja/guide/security)
