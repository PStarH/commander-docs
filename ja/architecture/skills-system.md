# スキル・システム

Commander のスキル・システムは、エージェントが必要に応じて読み込む **ドメイン専門知識パッケージ** です。

## 構造

```
skills/
├── skillManager / skillCurator / skillInjector
├── skillStore / skillQualityScorer / skillSecurityScanner
├── skillViewTool / metaLearnerBridge
└── types / index
```

## スキルとは

指示・例・制約を束ね、特定タスクのやり方を教えるパッケージです。

- **Built-in** · **User-defined** · **Community** · **Learned**（MetaLearner）

## CLI

```bash
npx tsx packages/core/src/cliEntry.ts skill list
npx tsx packages/core/src/cliEntry.ts skill view <skill-name>
npx tsx packages/core/src/cliEntry.ts skill create <skill-name>
npx tsx packages/core/src/cliEntry.ts skill pin <skill-name>
```

ビルド後は `commander skill …`。monorepo 導入が主経路です。

## 品質とセキュリティ

自動スコアリングとコンテンツ・スキャン。注入前にインジェクションやシークレットを検査します。

## ランタイム注入

`skillInjector` がプロンプトへ注入。pin は常時ロード。MetaLearner が成功パターンをスキル化することもあります。

## 関連

- [自己進化](/ja/architecture/self-evolution)  
- [インテリジェンス](/ja/architecture/intelligence)  
- [CLI コマンド](/ja/guide/commands)  
