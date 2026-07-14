# スマート・モデル・ルーター

Smart Model Router は **能力ベースのモデル選択** とユーザー定義ルーティングを提供します。コア `ModelRouter` の上にモデルプール・規則・予算制約を載せます。

## 能力タグ

| Capability | 説明 |
|------------|------|
| `code` / `reasoning` / `analysis` / `creative` / `math` | 主要タスク種 |
| `multimodal` / `vision` / `image_generation` | マルチモーダル |
| `long_context` / `low_cost` / `fast` / `high_quality` | 文脈・コスト・速度・品質 |
| `function_calling` / `json_mode` / `streaming` | ツール・JSON・ストリーム |
| `translation` / `summarization` / `extraction` | 翻訳・要約・抽出 |

## 設定

```typescript
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
      capabilities: ['code', 'reasoning', 'function_calling', 'streaming'],
      costPer1MInput: 2.5,
      costPer1MOutput: 10,
      contextWindow: 128000,
      tier: 'power',
    },
  ],
});
```

## モード

- **auto** — 能力・コスト・遅延で自動  
- **manual** — 固定モデル  
- **cascade** — 規則優先、失敗時フォールバック  

## 運用

キー 1 つでも基本ルーターは動きます。

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 関連

- [プロバイダー](/ja/guide/providers)  
- [Resilience](/ja/architecture/resilience)  
- [インテリジェンス](/ja/architecture/intelligence)  
