# oh-my-agent-skills

语言版本：[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/xiaohei-info/oh-my-agent-skills?display_name=tag)](https://github.com/xiaohei-info/oh-my-agent-skills/releases)
[![License](https://img.shields.io/github/license/xiaohei-info/oh-my-agent-skills)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/xiaohei-info/oh-my-agent-skills)](https://github.com/xiaohei-info/oh-my-agent-skills/commits/main)

**一组可安装、可按需组合的 Agent Skill 与工作流方法，用来修复 AI 系统里的常见失败模式。**

如果你想让 Agent 更可靠，但又不想重做整套系统，这个仓库就是给你的：你可以只拿 **一个 skill**、**一个 bundle**，或者整套引入。

它特别适合这些场景：想把“没验证就报完成”的执行习惯改掉，想把多 Agent 协作做干净，想让 cron / alert 真的适合发到聊天里，想把方法沉淀成可复用 skill，或者想把原始笔记慢慢编译成可维护的知识层。

![oh-my-agent-skills social preview](assets/social-preview.png)

## 这个仓库能帮你修什么问题

如果你的 Agent / 工作流有这些问题，可以从这里开始：

- 任务还没验证就说“做完了”
- debug 变成到处试、没有根因闭环
- 多 Agent 协作容易跑偏、重叠、失控
- cron / alert 发到聊天里，信息虽然对，但没人愿意看
- research 质量不稳定，读网页和选工具全靠临场发挥
- 笔记越积越多，但始终没有沉淀成耐用的知识层

## 从小处开始：一个 skill、一个 bundle，或整套采用

你**不需要**把整个仓库一次性装进去。

- **一个 skill**：先解决一个尖锐问题
  - 例子：`verification-before-completion`
- **一个 bundle**：先补一类工作流能力
  - 例子：`engineering-execution/`
- **整套采用**：把它当成一组更完整的 Hermes-compatible skill library

这个仓库就是按模块化思路组织的，方便你按需取用，而不是强耦合整包上车。

## 按需求选择的推荐起点

### 如果你的 Agent 经常过早报完成
先看：
- `engineering-execution/verification-before-completion`
- `engineering-execution/systematic-debugging`

### 如果多 Agent 协作经常变乱
先看：
- `multi-agent-control/subagent-first`
- `multi-agent-control/subagent-collaboration-workflow`

### 如果 cron / 监控消息发出来不好读
先看：
- `chatops-and-ops/user-friendly-cron-messages`
- `chatops-and-ops/ops-sentry`

### 如果你想把方法沉淀成可复用 skill
先看：
- `skill-engineering/writing-skills`
- `skill-engineering/external-hermes-skills-lifecycle`
- `skill-engineering/skill-optimizer`

### 如果你要加强 research 或知识工作流
先看：
- `research-and-reading/web-reading-router`
- `research-and-reading/hv-analysis`
- `knowledge-compilation/*`

## Hermes 快速安装方式

### 1. 先 clone 仓库

```bash
git clone https://github.com/xiaohei-info/oh-my-agent-skills.git
cd oh-my-agent-skills
```

### 2. 先装一个 skill

例子：只安装 `verification-before-completion`。

```bash
mkdir -p ~/.hermes/skills/software-development
cp -R skills/engineering-execution/verification-before-completion \
  ~/.hermes/skills/software-development/
```

### 3. 或者先装一个完整 bundle（当目标分类一致时）

例子：安装整个 `engineering-execution` bundle。

```bash
mkdir -p ~/.hermes/skills/software-development
cp -R skills/engineering-execution/verification-before-completion \
  ~/.hermes/skills/software-development/
cp -R skills/engineering-execution/systematic-debugging \
  ~/.hermes/skills/software-development/
```

### 4. 混合分类的 bundle 请对照 source map

公开仓库里的 bundle 结构是为了更好浏览；Hermes 里的安装路径仍然要按 skill 原始分类落位。

像这些 bundle，请先看 [`docs/source-map.md`](docs/source-map.md)：
- `multi-agent-control/`
- `skill-engineering/`
- `knowledge-compilation/`

### 5. 一定保留 support files

复制时不要只拿 `SKILL.md`。

要把整个 skill 目录一起带走，包括可能存在的：
- `references/`
- `templates/`
- `scripts/`
- `assets/`

## 装完之后怎么用

装完 skill 之后，最好在任务里显式点名调用。

例如：
- “Use `verification-before-completion` before telling me this bug is fixed.”
- “Use `subagent-first` to plan and delegate this feature.”
- “Use `user-friendly-cron-messages` to rewrite this monitoring output for Telegram.”
- “Use `web-reading-router` to choose the lightest reliable way to read this URL set.”

## 不用 Hermes 也能拿来迁移

这些 skill 的语法很多是 Hermes-native，但底层方法通常可以迁移。

常见映射方式：
- `delegate_task` -> 你的子代理 / worker 抽象
- `read_file/search_files/patch/write_file` -> 你的代码与文件工具
- `clarify` -> 你的用户确认层
- `todo` -> 你的任务状态层

如果你要迁移到别的 runtime，先看 [`docs/portability-notes.md`](docs/portability-notes.md)。

## 仓库结构

```text
skills/
  engineering-execution/
  multi-agent-control/
  skill-engineering/
  chatops-and-ops/
  research-and-reading/
  knowledge-compilation/

docs/
  adoption-guide.md
  bundles.md
  portability-notes.md
  social-preview.md
  source-map.md

assets/
  social-preview.png
```

## Bundle 总览

- **engineering-execution** — 验证与 debug 纪律
- **multi-agent-control** — controller 侧的 delegation 方法
- **skill-engineering** — 可复用 skill 的编写、打包、迭代
- **chatops-and-ops** — 面向聊天场景的人类可读自动化输出
- **research-and-reading** — 阅读路由与深度分析工作流
- **knowledge-compilation** — Inbox -> Wiki 的知识编译与维护

更详细的 bundle 说明见 [`docs/bundles.md`](docs/bundles.md)。

## 适合谁用

如果你符合下面任意一种，这个仓库大概率会有用：
- 在搭建 AI agent runtime
- 在维护一组可复用 skill library
- 想把多 Agent 协作从“能跑”提升到“可控”
- 想把 prompt / method 资产整理成可公开复用的形态
- 在做 chat-native 的 cron / alert 系统
- 在维护 Obsidian 风格的编译型知识库

## 这套仓库的核心价值观

这里面最重要的几条是：
- **先验证，再报完成**
- **先找根因，再修问题**
- **多 Agent 协作需要总控，不是只堆更多 Agent**
- **自动化输出应该面向人读，而不是内部 dump**
- **知识库要能编译维护，而不是只不断堆原始材料**
- **方法要能沉淀成可复用 skill，而不是一次性 prompt**

## 推荐阅读路径

1. 先选你要修的问题。
2. 先装一个 skill 或一个 bundle。
3. 再看 [`docs/adoption-guide.md`](docs/adoption-guide.md) 了解更完整的采用路径。
4. 如果你不在 Hermes 上，再看 [`docs/portability-notes.md`](docs/portability-notes.md)。
5. 真正用到生产前，读一遍对应 skill 的 `SKILL.md` 和 support files。

## 相关文档

- [`AGENTS.md`](AGENTS.md) — 给 agent / 协作者看的仓库规则
- [`docs/adoption-guide.md`](docs/adoption-guide.md) — 模块化采用路径与安装指引
- [`docs/bundles.md`](docs/bundles.md) — 按 bundle 拆解的问题 / skill 指南
- [`docs/portability-notes.md`](docs/portability-notes.md) — Hermes 原生部分与可迁移边界
- [`docs/social-preview.md`](docs/social-preview.md) — social preview 说明
- [`docs/source-map.md`](docs/source-map.md) — 公开 bundle 与原始 Hermes 分类映射
- [`SECURITY.md`](SECURITY.md) — 安全问题反馈方式
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — 社区参与规则

## 贡献

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 许可证

MIT
