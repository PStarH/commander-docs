# Channel Adapters

Commander supports multiple communication channels through its adapter system, allowing agents to interact with users across different platforms. Channel adapters implement the `ChannelAdapter` interface:

本ページは Commander における **Channel Adapters** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
interface ChannelAdapter {
  readonly name: string;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: InboundMessage) => void): void;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
