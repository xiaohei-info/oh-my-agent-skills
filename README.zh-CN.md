# oh-my-agent-skills

语言版本：[English](README.md) | [简体中文](README.zh-CN.md)

一个面向公开复用的 **agent 方法论与 Hermes 兼容 skill 套件仓库**。

这个仓库不是新的执行引擎，也不是某台机器上本地 `~/.hermes/skills` 的原样导出。它是一个经过整理、分组、脱敏和文档化的 **可复用 agent operating methods 公共包**。

## 这个仓库解决什么问题

很多 agent 系统并不是缺模型、缺工具，而是缺这些东西：
- 明确的完成标准
- 有纪律的 debug 方法
- 多 agent 协作时清晰的 controller / child contract
- 把重复工作沉淀成 skill / template / reference 的机制
- 面向人类的 cron / alert 输出设计
- 原始笔记与编译知识分层维护的方法

这个仓库就是把这些方法打包出来，便于直接复用或迁移。

## 这个仓库最有辨识度的地方

- **Skill 是操作资产，不是 prompt 碎片**
- **执行质量来自纪律，而不只是模型能力**
- **多 agent 系统需要总控，不只是更多 agent**
- **自动化输出要为人读，而不是为模型自嗨**
- **知识库应该是编译出来的，而不是越堆越大**
- **公开打包本身就是价值放大器**

## 核心 bundle

- `engineering-execution/`
  - completion verification
  - root-cause debugging

- `multi-agent-control/`
  - subagent-first
  - subagent collaboration workflow

- `skill-engineering/`
  - skill authoring / packaging / optimization

- `chatops-and-ops/`
  - 面向聊天场景的 cron / alert 设计
  - 降噪运维监控

- `research-and-reading/`
  - URL 阅读路由
  - 横纵分析法

- `knowledge-compilation/`
  - Inbox -> Wiki 编译
  - wiki lint / triage

## 怎么用

### 方式 A：作为 Hermes skill bundle 使用
复制某个 skill 的完整目录，而不是只复制 `SKILL.md`。

典型规则：
- 一整个 skill 文件夹一起复制
- 保留 `references/`、`templates/`、`scripts/`、`assets/`

### 方式 B：迁移到别的 agent runtime
即使 skill 里写的是 Hermes 工具名，很多方法本身仍然可迁移：
- `delegate_task` -> 你的子代理机制
- `read_file/search_files/patch/write_file` -> 你的代码/文件工具
- `clarify` -> 你的用户确认层
- `todo` -> 你的任务状态层

### 方式 C：当方法论文库阅读
你也可以先把它当成 agent workflow 参考库来读，而不急着安装。

## 推荐阅读顺序

1. `README.md`
2. `docs/adoption-guide.md`
3. `docs/bundles.md`
4. `docs/portability-notes.md`
5. 再进入具体 `skills/<bundle>/<skill>/SKILL.md`

## 相关文档

- `AGENTS.md` — 给 agent / 协作者看的仓库规则
- `docs/adoption-guide.md` — 采用方式与路径
- `docs/bundles.md` — bundle 说明
- `docs/portability-notes.md` — Hermes 原生部分与可迁移边界
- `docs/source-map.md` — 公共仓库到原始 skill 家族的映射

## 许可证

MIT
