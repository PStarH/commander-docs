# Custom Tools

本页说明 Commander 中 **Custom Tools** 的用途、操作方式与生产注意点。命令路径与产品 monorepo 保持一致。

## 快速入口

```bash
interface Tool {
  name: string;
  description: string;
  parameters?: Record<string, ParameterSchema>;

  execute(context: ToolContext, args: any): Promise<ToolResult>;
}
```


## 说明

### Tool Interface

（对应英文文档章节 **Tool Interface** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Example: Webhook Tool

（对应英文文档章节 **Example: Webhook Tool** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Registering a Tool

（对应英文文档章节 **Registering a Tool** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Tool Features

（对应英文文档章节 **Tool Features** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）


## 指标口径

25 提供商 · 5 规范拓扑 · 18 内置工具 · 6700+ 测试。

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [命令](/zh/guide/commands)  
