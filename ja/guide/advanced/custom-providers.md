# Custom Providers

Connect Commander to any LLM provider by implementing the `LLMProvider` interface. Commander supports automatic fallback between providers:

本ページは Commander における **Custom Providers** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
interface LLMProvider {
  readonly name: string;
  readonly model: string;

  call(
    messages: Message[],
    options: CallOptions
  ): Promise<LLMResponse>;
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
