# 实战手册

端到端配方。每篇：**目标 → 命令 → 成功信号 → 失败模式**。

| 配方 | 说明 |
|------|------|
| [安全审计仓库](/zh/guide/cookbook/security-audit) | 流式多代理安全向分析 |
| [英文：安全重构模块](/guide/cookbook/refactor-module) | plan → run → review |
| [英文：CI full-auto](/guide/cookbook/ci-full-auto) | 非交互修复 lint |

约定：在 monorepo 根目录、`pnpm install` 之后、已 export 一把 Key。

```bash
npx tsx packages/core/src/cliEntry.ts <command>
# 构建后: commander <command>
```

新手请先看 [快速开始](/zh/guide/getting-started)。
