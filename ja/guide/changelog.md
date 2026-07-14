# Changelog

Commander アーキテクチャの構成要素について日本語で説明します。monorepo 実装と整合しています。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 主な内容

### v0.2.1-pre (Unreleased)

運用では **v0.2.1-pre (Unreleased)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/changelog)を参照してください。

### v0.2.0 (2026-05-19)

運用では **v0.2.0 (2026-05-19)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/changelog)を参照してください。

### v0.1.0 (2026-05-17)

運用では **v0.1.0 (2026-05-17)** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/changelog)を参照してください。

## 運用

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
