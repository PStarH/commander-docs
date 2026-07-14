# 实战：安全审计一个仓库

**目标：** 用流式多代理做安全向审计，并得到可读结论。  
**时间：** 约 10 分钟 · **风险：** 以读为主（建议先 `read-only` / `plan`）

## 1. 准备

```bash
cd /path/to/Commander
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=read-only   # 可选
```

## 2. 先 plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**期望：** 分类（常为 ANALYSIS）、复杂度、拓扑（常为 DISPATCH / REVIEW）。

## 3. 带 stream 执行

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**期望：** 审议横幅、代理/工具活动、质量门、综合 findings。

## 4. 成功清单

- [ ] plan 打印拓扑且未崩溃  
- [ ] stream 有代理/工具输出  
- [ ] 最终摘要有具体发现或明确「范围内无发现」  
- [ ] 无无事件挂死（>2 分钟零输出）  

## 失败模式

| 问题 | 动作 |
|------|------|
| 无提供商 | `doctor`；检查当前 shell 环境变量 |
| 审计过浅 | 指向真实代码路径；提示写更具体 |
| SAFETY 告警 | 若命中类密钥模式，视为信号 |

英文完整版：[Security audit cookbook](/guide/cookbook/security-audit)。
