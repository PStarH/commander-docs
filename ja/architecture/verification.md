# 検証パイプライン

すべてのエージェント出力は呼び出し元に返る前に **5 つの品質ゲート** を通ります。「あると良い」チェックではなく、ランタイム再試行ループの一部です。

## 構造

```
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ 設定可能な閾値のシグナルベース検出
  │
  ├─ Gate 2: Consistency Check
  │   └─ 内部一貫性・矛盾検出
  │
  ├─ Gate 3: Completeness Verification
  │   └─ 必須フィールドと手順の存在
  │
  ├─ Gate 4: Accuracy Validation
  │   └─ 既知制約に対する事実精度
  │
  ├─ Gate 5: Safety Scanning
  │   └─ インジェクション検出、機微データ漏洩
  │
  └─ → Pass: 結果を返す
     → Fail: 全文脈付きで再試行または報告
```

## UnifiedVerificationPipeline

`UnifiedVerificationPipeline` が 5 ゲートを調整します。

```typescript
interface UVPTaskContext {
  goal: string;
  availableTools: string[];
  steps: Step[];
  // ... full execution context
}

const pipeline = new UnifiedVerificationPipeline();
const result = await pipeline.verify(output, context, { tenantId });

result.gates.forEach((gate) => {
  if (!gate.passed) {
    // 失敗時は gate.feedback を文脈に再試行
  }
});
```

## ゲート詳細

### 1. 幻覚検出

LLM が LLM を裁く循環を避け、**シグナルベース**検出を使います。

- ツール出力で裏付けられない主張
- 数値の不整合
- 同一応答内の矛盾
- 証拠と合わない確信度

閾値はテナント単位で調整し、感度と誤検知のバランスを取ります。

### 2. 一貫性

- セクション間の論理矛盾なし
- 用語・参照の一貫
- 実行項目が前提と一致

### 3. 完全性

- 要求された出力がすべてある
- 必須フィールドが埋まっている
- 「TODO」「FIXME」などのプレースホルダなし

### 4. 正確性

既知制約・ツール結果・タスク目標に対する事実チェック。

### 5. 安全

インジェクション、シークレット類似漏洩、危険なコマンド提案などを走査。

## 失敗時

ゲート失敗は多くの場合 **再試行** に繋がり、フィードバックが次の LLM 呼び出し文脈に入ります。上限超過時は失敗モード付きで呼び出し元に報告します。

## 関連

- [エージェントランタイム](/ja/architecture/agent-runtime)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
