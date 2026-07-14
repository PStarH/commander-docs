# Skills System

Commander's skills system provides domain-specific expertise that agents can load on demand. A skill is a packaged set of instructions, examples, and constraints that teaches an agent how to perform a specific type of task. Skills can be:

本ページは Commander における **Skills System** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

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

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
