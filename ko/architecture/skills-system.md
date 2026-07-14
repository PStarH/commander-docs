# 스킬 시스템

Commander 스킬 시스템은 에이전트가 필요할 때 로드하는 **도메인 전문 지식 패키지**입니다.

## 구조

```
skills/
├── skillManager.ts / skillCurator.ts / skillInjector.ts
├── skillStore.ts / skillQualityScorer.ts / skillSecurityScanner.ts
├── skillViewTool.ts / metaLearnerBridge.ts
├── types.ts / index.ts
```

## 스킬이란?

지시·예시·제약을 묶어 특정 작업 수행 방법을 가르치는 패키지입니다.

- **Built-in** — 제품과 함께 제공  
- **User-defined** — 사용자가 작성·공유  
- **Community** — 레지스트리에서 다운로드  
- **Learned** — MetaLearner가 자동 생성  

## CLI

```bash
npx tsx packages/core/src/cliEntry.ts skill list
npx tsx packages/core/src/cliEntry.ts skill view <skill-name>
npx tsx packages/core/src/cliEntry.ts skill create <skill-name>
npx tsx packages/core/src/cliEntry.ts skill pin <skill-name>
```

빌드 후 `commander skill …` 도 가능합니다. monorepo 설치가 주 경로입니다.

## 품질 & 보안

스킬은 자동 품질 점수와 콘텐츠 보안 스캔을 거칩니다. 주입 전 프롬프트 인젝션·시크릿 패턴을 검사합니다.

## 런타임 주입

`skillInjector`가 에이전트 프롬프트에 스킬을 붙입니다. pin된 스킬은 항상 로드됩니다. MetaLearner 브릿지가 성공 패턴을 스킬로 승격할 수 있습니다.

## 관련

- [자기 진화](/ko/architecture/self-evolution)  
- [인텔리전스](/ko/architecture/intelligence)  
- [CLI 명령](/ko/guide/commands)  
