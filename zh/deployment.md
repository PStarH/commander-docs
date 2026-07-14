# 部署

本页说明 Commander 中 **部署** 的用途、操作方式与生产注意点。命令路径与产品 monorepo 保持一致。

## 快速入口

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:     http://localhost:4000
# Web GUI: http://localhost:3000   (Docker / Nginx)
# Dev GUI: http://localhost:5173   (pnpm gui, no Docker)
```


## 说明

### Local (Docker Compose)

（对应英文文档章节 **Local (Docker Compose)** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Production (VM / VPS)

（对应英文文档章节 **Production (VM / VPS)** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Observability Stack

（对应英文文档章节 **Observability Stack** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Configuration Reference

（对应英文文档章节 **Configuration Reference** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）


## 指标口径

25 提供商 · 5 规范拓扑 · 18 内置工具 · 6700+ 测试。

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [命令](/zh/guide/commands)  
