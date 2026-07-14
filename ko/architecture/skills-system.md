# Skills System

Commander's skills system provides domain-specific expertise that agents can load on demand. A skill is a packaged set of instructions, examples, and constraints that teaches an agent how to perform a specific type of task. Skills can be:

이 문서는 Commander에서 **Skills System** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
skills/
├── skillManager.ts       ← Skill lifecycle management
├── skillCurator.ts       ← Skill curation and organization
├── skillInjector.ts      ← Inject skills into agent prompts
├── skillStore.ts         ← Persistent skill storage
├── skillQualityScorer.ts ← Quality scoring for skills
├── skillSecurityScanner.ts ← Security scanning for skill content
├── skillViewTool.ts      ← Tool for viewing/loading skills
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
