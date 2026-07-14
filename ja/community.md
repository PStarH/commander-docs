# Community

**Community.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Channel | Status | Link |
|---------|--------|------|
| **GitHub** | Live | [github.com/PStarH/Commander](https://github.com/PStarH/Commander) — issues, PRs, stars |
| **Discussions** | Use GitHub Issues | Feature ideas and Q&A via [Issues](https://github.com/PStarH/Commander/issues) |
| **Docs** | Live | This site + PRs on [commander-docs](https://github.com/PStarH/commander-docs) |
| **Discord / Twitter** | Planned | Not live yet — follow the repo for announcements |


## 主な内容

### Get involved

運用では **Get involved** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Contributing

運用では **Contributing** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Roadmap

運用では **Roadmap** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Trust signals

運用では **Trust signals** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Contribute docs

運用では **Contribute docs** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Showcase

運用では **Showcase** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Stay updated

運用では **Stay updated** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

### Docs for AI assistants

運用では **Docs for AI assistants** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/community)を参照してください。

## 例（コードは英語のまま）

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
# Prefer project scripts when available:
pnpm test:all   # or: cd packages/core && npx tsx --test tests/*.test.ts
```

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
