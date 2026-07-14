# 검증 파이프라인

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/verification)



Every agent output passes through a 5-gate quality verification pipeline before it is returned to the caller. This is not a "nice-to-have" check — it is an integral part of the runtime retry loop.

## Architecture


```
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ Signal-based detector with configurable thresholds
  │
  ├─ Gate 2: Consistency Check
  │   └─ Internal consistency and contradiction detection
  │
  ├─ Gate 3: Completeness Verification
  │   └─ All required fields and steps present
  │
  ├─ Gate 4: Accuracy Validation
  │   └─ Factual accuracy against known constraints
  │
  ├─ Gate 5: Safety Scanning
  │   └─ Injection detection, sensitive data leakage
  │
  └─ → Pass: return result
     → Fail: retry or report with full context
```

## UnifiedVerificationPipeline


The `UnifiedVerificationPipeline` orchestrates all 5 gates:

```typescript
interface UVPTaskContext {
  goal: string;
  availableTools: string[];
  steps: Step[];
  // ... full execution context
}

const pipeline = new UnifiedVerificationPipeline();
const result = await pipeline.verify(output, context, { tenantId });

result.gates.forEach(gate => {
  if (!gate.passed) {
    // Gate failure triggers retry with gate.feedback as context
  }
});
```

## Gate Details


### 1. Hallucination Detection


Uses signal-based detection rather than LLM-judging (which is circular). Checks for:

- Claims unsupported by tool outputs
- Numerical inconsistencies
- Contradictory statements within the same response
- Confidence estimates that don't match evidence

Thresholds are configurable per tenant to balance sensitivity vs false positives.

### 2. Consistency Check


Verifies that the output is internally consistent:

- No logical contradictions between sections
- Consistent terminology and references
- Actionable items match their preconditions

### 3. Completeness Verification


Ensures the output satisfies the original task requirements:

- All requested outputs are present
- Required fields are populated
- No placeholder content ("TODO", "FIXME")

### 4. Accuracy Validation


Checks factual claims against available context:

- Tool outputs support the assertions made
- No fabricated citations or references
- Claims match known constraints from the task context

### 5. Safety Scanning


The final gate prevents unsafe outputs:

- Prompt injection detection
- Sensitive data leakage (API keys, credentials)
- Policy violations
- Content policy compliance

## Integration with Retry Loop


When a gate fails, the runtime retries with the gate's feedback injected into the LLM context:

```
Gate failure → feedback → retry LLM → re-verify
              (maxRetries attempts)
                ↓
All retries exhausted → Dead Letter Queue + error report
```

The `llmRetry.ts` module classifies verification failures as retryable, and the `StepErrorBoundary` handles per-step recovery policies.
