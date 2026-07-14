# Intelligence Layer

**Intelligence Layer.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

이 문서는 Commander에서 **Intelligence Layer** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();

const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
