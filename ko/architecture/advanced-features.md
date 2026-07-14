# Advanced Engine Features

Commander includes several advanced engine components for sophisticated execution control. The speculative executor runs multiple execution paths in parallel and selects the best result:

이 문서는 Commander에서 **Advanced Engine Features** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();

// Run 3 speculative paths in parallel
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
