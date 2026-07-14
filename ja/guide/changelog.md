# Changelog

- **SQLite persistence**: `SqliteWarRoomStore` with WAL mode, 9 indexes, transaction-safe writes. Enable via `WARROOM_STORAGE=sqlite`; `createWarRoomStore()` factory provides transparent switching - **Event sourcing engine**: Write-Ahead Log with SHA-256 hash chain tamper protection, snapshot-based recovery, deterministic event replay (IF-05)

本ページは Commander における **Changelog** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
