# ベンチマーク

ベンチマークは monorepo の **再現可能なスクリプト** です。マーケ用スクショではありません。

## 原則

- 同じコミット・プロンプトで再実行可能  
- 指標: 成功率、遅延、トークン、コスト、品質ゲート  
- 製品 `BENCHMARK.md` とスクリプトが真実源  

## monorepo で実行

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
# 他 suite は monorepo の package.json / ドキュメントを確認
```

## ドキュメント上の現在メトリクス

**25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。  
正確なベンチ点数は monorepo で自分で走らせた結果を優先してください。

## セキュリティ・スイート

Red Team · AgentDojo · Tenant isolation など。

## 関連

- [セキュリティ](/ja/guide/security)  
- [本番準備](/ja/architecture/production-readiness)  
- [Changelog](/ja/guide/changelog)  
