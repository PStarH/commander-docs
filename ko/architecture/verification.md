# 검증 파이프라인

모든 에이전트 출력은 호출자에게 반환되기 전 **5개 품질 게이트**를 통과합니다. “있으면 좋은” 검사가 아니라 런타임 재시도 루프의 핵심입니다.

## 구조

```
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ 설정 가능한 임계값의 신호 기반 탐지
  │
  ├─ Gate 2: Consistency Check
  │   └─ 내부 일관성·모순 탐지
  │
  ├─ Gate 3: Completeness Verification
  │   └─ 필수 필드·단계 존재
  │
  ├─ Gate 4: Accuracy Validation
  │   └─ 알려진 제약 대비 사실 정확성
  │
  ├─ Gate 5: Safety Scanning
  │   └─ 인젝션 탐지, 민감 데이터 유출
  │
  └─ → Pass: 결과 반환
     → Fail: 전체 컨텍스트와 함께 재시도 또는 보고
```

## UnifiedVerificationPipeline

`UnifiedVerificationPipeline`이 5개 게이트를 조율합니다.

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
    // 게이트 실패 시 gate.feedback을 컨텍스트로 재시도
  }
});
```

## 게이트 상세

### 1. 환각 탐지

LLM이 LLM을 심판하는 순환을 피하고 **신호 기반** 탐지를 씁니다.

- 도구 출력으로 뒷받침되지 않는 주장
- 수치 불일치
- 같은 응답 안의 모순
- 증거와 맞지 않는 신뢰도 표현

임계값은 테넌트별로 조절해 민감도와 오탐을 균형 잡습니다.

### 2. 일관성

- 섹션 간 논리 모순 없음
- 용어·참조 일관
- 실행 가능 항목이 전제와 일치

### 3. 완전성

- 요청한 출력이 모두 있음
- 필수 필드 채워짐
- “TODO” / “FIXME” 같은 플레이스홀더 없음

### 4. 정확성

알려진 제약·도구 결과·태스크 목표에 대해 사실 검증.

### 5. 안전

인젝션 패턴, 시크릿 유사 유출, 위험한 명령 제안 등을 스캔.

## 실패 시

게이트 실패는 대개 **재시도**로 이어지며, 피드백이 다음 LLM 호출 컨텍스트에 들어갑니다. 한도를 넘으면 실패 모드와 함께 호출자에게 보고합니다.

## 관련

- [에이전트 런타임](/ko/architecture/agent-runtime)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
