# 投機実行 (Speculative Execution)

Commander は LLM の思考時間中に次のツール呼び出しを先実行する **PASTE 風投機実行**（Pattern-Aware Speculative Execution）を実装します。研究ではタスク完了時間を最大約 48.5% 短縮できるとされます。

## 動作

LLM が考えているあいだに、観測パターンから次ツールを予測して先に実行します。モデルが実際に同じ呼び出しをすれば結果は既にあり（待ち 0）、外れた予測は副作用なく破棄します。

```
LLM Call → Pattern Tracker → Speculative Executor → Pre-executed results (cache)
```

## 安全

**読み取り専用** ツールだけを投機実行します。

- 例: `file.read`, `web.search`, `web.fetch`, `code.search`, `git.status`

**状態変更** ツールは絶対に投機実行しません。

- 例: `file.write`, `file.edit`, `shell.execute`, `git.commit`, `apply_patch`

## PatternTracker

```typescript
import { PatternTracker } from '@commander/core';

const tracker = new PatternTracker();
tracker.recordSequence(['file.read', 'code.search', 'file.read']);
const predictions = tracker.predictNext(['file.read']);
// → [{ toolName: 'code.search', confidence: 0.8 }]
```

### ライフサイクル

1. **観測** — n-gram（2, 3, 4）  
2. **信頼度** — `min(1, frequency / 10)`  
3. **剪定** — 出現 &lt;2 または 5 分未使用  

## 運用

内部最適化です。ユーザーは `run --stream` で通常どおりツール呼び出しを見ます。

```bash
npx tsx packages/core/src/cliEntry.ts run "explain this repo" --stream
```

## 関連

- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [ツール](/ja/architecture/tools)  
- [キャッシュ](/ja/architecture/caching)  
