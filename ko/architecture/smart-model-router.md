# 스마트 모델 라우터

Smart Model Router는 **능력 기반 모델 선택**과 사용자 정의 라우팅 규칙을 제공합니다. 코어 `ModelRouter` 위에 모델 풀·규칙·예산 제약을 얹습니다.

## 능력 태그

| Capability | 설명 |
|------------|------|
| `code` | 코드 생성·이해 |
| `reasoning` | 논리·CoT |
| `analysis` | 데이터 분석 |
| `creative` | 창작·브레인스토밍 |
| `math` | 수학 |
| `multimodal` / `vision` / `image_generation` | 멀티모달·비전·이미지 생성 |
| `long_context` | 긴 컨텍스트 |
| `low_cost` / `fast` / `high_quality` | 비용·지연·품질 |
| `function_calling` / `json_mode` / `streaming` | 도구·JSON·스트림 |
| `translation` / `summarization` / `extraction` | 번역·요약·추출 |

## 설정

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
    {
      id: 'claude-sonnet-4-20250514',
      provider: 'anthropic',
      capabilities: ['code', 'reasoning', 'long_context', 'function_calling'],
      costPer1MInput: 3,
      costPer1MOutput: 15,
      contextWindow: 200000,
      tier: 'power',
    },
  ],
});
```

## 모드

- **auto** — 능력·비용·지연으로 자동 선택  
- **manual** — 고정 모델  
- **cascade** — 규칙 우선, 실패 시 폴백 체인  

## 운영

키 하나만 있어도 기본 라우터가 동작합니다. 풀·예산을 세밀히 쓰려면 monorepo 설정과 연동하세요.

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 관련

- [프로바이더](/ko/guide/providers)  
- [Resilience](/ko/architecture/resilience)  
- [인텔리전스](/ko/architecture/intelligence)  
