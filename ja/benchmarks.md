# ベンチマーク

Commander のベンチマークは monorepo 内の **再現可能なスクリプト** です。マーケティング用のスクリーンショットではありません。

## いまの製品メトリクス（ドキュメント基準）

- **25** LLM プロバイダー  
- **5** 正規トポロジ（SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW）  
- **18** 組み込み tools  
- **6700+** テスト  

正確なベンチ点数は monorepo で自分で走らせた結果を優先してください。

## monorepo で実行

```bash
# 製品リポジトリのルート（スクリプト名は package.json を確認）
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

セキュリティ系スイートの目的:

| スイート | 目的 |
|----------|------|
| Red Team | 攻撃カテゴリ vs 防御 |
| AgentDojo | 間接インジェクション耐性 |
| Tenant isolation | クロステナント隔離 |

## ローカル健全性

```bash
npx tsx packages/core/src/cliEntry.ts doctor
cd packages/core && npx tsx --test tests/*.test.ts
```

## 詳細ガイド

より長い説明は [ガイド: ベンチマーク](/ja/guide/benchmarks) を参照してください。

## 関連

- [セキュリティ](/ja/guide/security)  
- [本番準備](/ja/architecture/production-readiness)  
- [Changelog](/ja/guide/changelog)  
