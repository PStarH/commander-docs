# 벤치마크

벤치마크는 monorepo의 **재현 가능한 스크립트**입니다. 마케팅 스크린샷이 아닙니다.

## 원칙

- 동일 커밋·동일 프롬프트로 재실행 가능  
- 지표: 성공률, 지연, 토큰, 비용, 품질 게이트  
- 제품 문서 `BENCHMARK.md` 와 스크립트가 소스 오브 트루스  

## monorepo에서 실행

```bash
# 제품 루트에서 (스크립트 이름은 monorepo package.json 확인)
pnpm benchmark:redteam
pnpm benchmark:agentdojo
# 기타 suite 는 monorepo 문서 참조
```

## 제품이 보고하는 예시 수치 (요약)

역사적 스냅샷은 EN changelog / product README에 있습니다. 문서 사이트는 **25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트** 를 현재 기준으로 사용합니다. 정확한 벤치 점수는 monorepo에서 직접 돌린 결과를 우선하세요.

## 보안 스위트

| 스위트 | 목적 |
|--------|------|
| Red Team | 공격 카테고리 vs 방어 |
| AgentDojo | 간접 인젝션 견고성 |
| Tenant isolation | 크로스 테넌트 |

## 관련

- [보안](/ko/guide/security)  
- [프로덕션 준비](/ko/architecture/production-readiness)  
- [Changelog](/ko/guide/changelog)  
