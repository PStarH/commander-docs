# Extension Points

本页说明 Commander 中 **Extension Points** 的用途、操作方式与生产注意点。命令路径与产品 monorepo 保持一致。

## 快速入口

```bash
class MyProvider implements LLMProvider {
  async call(messages: Message[], options: CallOptions): Promise<LLMResponse> {
    // Your implementation
  }
}
runtime.registerProvider('my-provider', new MyProvider());
```


## 说明

### Plugin System (19 Hook Points)

（对应英文文档章节 **Plugin System (19 Hook Points)** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Extension Interfaces

（对应英文文档章节 **Extension Interfaces** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Meta-Learner

（对应英文文档章节 **Meta-Learner** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）


## 指标口径

25 提供商 · 5 规范拓扑 · 18 内置工具 · 6700+ 测试。

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [命令](/zh/guide/commands)  
