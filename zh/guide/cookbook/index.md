# 实战手册（Cookbook）

端到端配方。每页结构：**目标 → 命令 → 期望信号 → 失败模式**。

| 配方                                                 | 时间     | 练习内容                      |
| ---------------------------------------------------- | -------- | ----------------------------- |
| [仓库安全审计](/zh/guide/cookbook/security-audit)    | ~10 分钟 | DISPATCH 式分析、流式、质量门 |
| [安全地重构模块](/zh/guide/cookbook/refactor-module) | ~15 分钟 | Plan → run → review           |
| [CI 全自动修 lint](/zh/guide/cookbook/ci-full-auto)  | ~15 分钟 | 非交互模式、exit code         |

## 约定

所有配方默认你在 Commander monorepo 根目录完成 `pnpm install`，并已 export 一把 API Key。

```bash
# 源码检出
npx tsx packages/core/src/cliEntry.ts <command>

# 构建 @commander/core 之后
commander <command>
```

新手请先看 [快速开始](/zh/guide/getting-started)。

## 相关

- [为什么选 Commander](/zh/guide/why-commander)
- [拓扑决策树](/zh/guide/usage/topology-decision-tree)
- [Web 控制台](/zh/guide/web-console)
