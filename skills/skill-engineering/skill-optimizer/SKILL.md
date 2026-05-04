---
name: skill-optimizer
description: >
  Hermes skill optimizer inspired by Karpathy's autoresearch. Evaluates SKILL.md files
  using an 8-dimension rubric (structure + effectiveness), runs hill-climbing with git
  version control, validates improvements through test prompts. Use when user mentions
  "优化skill", "skill评分", "自动优化", "auto optimize", "skill质量检查", "帮我改改skill",
  "skill怎么样", "提升skill质量", "skill review", "skill打分", "达尔文", "darwin".
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [meta, skill, optimization, evaluation, autoresearch]
    source: adapted from alchaincyf/darwin-skill
---

# Skill Optimizer

> 借鉴 Karpathy autoresearch 的自主实验循环，对 Hermes skills 进行持续优化。
> 核心理念：**评估 → 改进 → 实测验证 → 人类确认 → 保留或回滚**

---

## 设计哲学

autoresearch 的精髓：
1. **单一可编辑资产** — 每次只改一个 SKILL.md
2. **双重评估** — 结构评分（静态分析）+ 效果验证（跑测试看输出）
3. **棘轮机制** — 只保留改进，自动回滚退步
4. **独立评分** — 评分用子代理，避免「自己改自己评」的偏差
5. **人在回路** — 每个 skill 优化完后暂停，用户确认再继续

与纯结构审查的区别：不只看 SKILL.md 写得规不规范，更看改完后**实际跑出来的效果是否更好**。

---

## 评估 Rubric（8维度，总分100）

### 结构维度（60分）— 静态分析

| # | 维度 | 权重 | 评分标准 |
|---|------|------|---------|
| 1 | **Frontmatter质量** | 8 | name 规范（小写-连字符）、description 包含做什么+何时用+触发词、≤1024字符 |
| 2 | **工作流清晰度** | 15 | 步骤明确可执行、有序号、每步有明确输入/输出 |
| 3 | **边界条件覆盖** | 10 | 处理异常情况、有 fallback 路径、错误恢复 |
| 4 | **检查点设计** | 7 | 关键决策前有用户确认、防止自主失控 |
| 5 | **指令具体性** | 15 | 不模糊、有具体参数/格式/示例、可直接执行 |
| 6 | **资源整合度** | 5 | references/scripts/assets 引用正确、路径可达 |

### 效果维度（40分）— 需要实测

| # | 维度 | 权重 | 评分标准 |
|---|------|------|---------|
| 7 | **整体架构** | 15 | 结构层次清晰、不冗余不遗漏、与 Hermes skill 约定一致 |
| 8 | **实测表现** | 25 | 用测试 prompt 跑一遍，输出质量是否符合 skill 宣称的能力 |

### 评分规则

- 维度 1-7：每个维度打 1-10 分，乘以权重得到该维度得分
- 维度 8（实测表现）：跑 2-3 个测试 prompt，按输出质量打 1-10 分
- **总分 = Σ(维度分 × 权重) / 10**，满分 100
- 改进后总分必须 **严格高于** 改进前才保留

### 评分锚点（统一刻度）

| 分数段 | 含义 | 判断标准 |
|--------|------|----------|
| **1-3** | 严重缺失 | 该维度核心要素不存在或严重错误，导致 skill 不可用 |
| **4-6** | 基本满足但有短板 | 核心要素存在，但至少 1 个关键点缺失或模糊 |
| **7-9** | 良好 | 核心要素完整，关键点清晰，仅有轻微改进空间 |
| **10** | 完美 | 无改进空间，可作为该维度的标杆示例 |

**示例锚点（D2 工作流清晰度）：**
- 1-3 分：无步骤编号、步骤顺序混乱、无输入/输出说明
- 4-6 分：有步骤编号但部分步骤模糊（如"处理数据"）、输入/输出不全
- 7-9 分：步骤有序号、每步有明确输入/输出、可直接执行
- 10 分：上述全部 + 有示例演示完整流程

### 关于「实测表现」维度

这是与纯结构评分最大的区别。评分方式：

1. 为每个 skill 设计 2-3 个**典型用户 prompt**（不是边缘 case，是最常见的使用场景）
2. 用子代理执行：一个带 skill 跑，一个不带 skill 跑（baseline）
3. 对比输出质量，从以下角度打分：
   - 输出是否完成了用户意图？
   - 相比不带 skill 的 baseline，质量提升明显吗？
   - 有没有 skill 引入的负面影响（过度冗余、跑偏、格式奇怪）？

如果无法跑子代理（时间/资源限制），可以退化为「干跑验证」：读完 skill 后模拟一个典型 prompt 的执行思路，判断流程是否合理。但要在 results.tsv 中标注 `dry_run`。

---

## 自主优化循环

### Phase 0: 初始化

```
1. 确认优化范围：
   - 全部 skills → 扫描 ~/.hermes/skills/*/SKILL.md
   - 指定 skills → 用户指定列表
   - **异常：skill 不存在 → 提示用户并跳过，不中断流程**

2. 初始化 git（如 skills 目录不是 repo）：
   - git init + baseline commit
   - 创建优化分支：auto-optimize/YYYYMMDD-HHMM
   - **异常：git 命令失败 → 提示用户检查权限，终止流程**

3. 初始化 results.tsv（如不存在）
4. 读取现有 results.tsv 了解历史优化记录
```

### Phase 0.5: 测试 Prompt 设计

在评估之前，为每个 skill 设计测试 prompt。这步很关键——没有测试 prompt，「实测表现」维度就打不了分。

```
for each skill:
  1. 读取 SKILL.md，理解它做什么
     - **异常：SKILL.md 不存在或无法读取 → 跳过该 skill，记录到 results.tsv**
  
  2. 检查是否已有 test-prompts.json：
     - 如果存在 → 展示给用户确认是否沿用
     - 如果不存在 → 设计 2-3 个测试 prompt
  
  3. 设计测试 prompt 时覆盖：
     - 最典型的使用场景（happy path）
     - 一个稍复杂或有歧义的场景
  
  4. 保存到 skill目录/test-prompts.json：
     [
       {"id": 1, "prompt": "用户会说的话", "expected": "期望输出的简短描述"},
       {"id": 2, "prompt": "...", "expected": "..."}
     ]
  
  5. **异常：test-prompts.json 写入失败 → 提示用户检查目录权限，该 skill 只做 dry_run 评估**
```

展示所有测试 prompt 给用户，**确认后再进入评估**。测试 prompt 的质量决定了优化方向是否正确。

### Phase 1: 基线评估（Baseline）

```
for each skill in 优化范围:

  # 结构评分（主 agent 可以做）
  1. 读取 SKILL.md 全文
     - **异常：读取失败 → 标记为 "unreadable"，跳过该 skill**
  2. 按维度 1-7 逐项打分（附简短理由）

  # 效果评分（用子代理做，独立于主 agent）
  3. 对每个测试 prompt，spawn 子代理：
     - with_skill: 带着 SKILL.md 执行测试 prompt
     - baseline: 不带 skill 执行同一 prompt
     - **异常：子代理超时（>60s）→ 该 prompt 标记 timeout，维度 8 用 dry_run**
     - **异常：子代理报错 → 记录错误，维度 8 用 dry_run**
  4. 对比两组输出，打维度 8 的分

  # 汇总
  5. 计算加权总分
  6. 记录到 results.tsv
```

**如果子代理不可用**（超时、环境限制），维度 8 用干跑验证打分，标注 `dry_run`。

基线评估完成后，展示评分卡：

```
┌──────────────────────────┬───────┬──────────────┬──────────────┐
│ Skill                    │ Score │ 结构短板      │ 效果短板      │
├──────────────────────────┼───────┼──────────────┼──────────────┤
│ github-pr-workflow       │ 78    │ 边界条件      │ 测试prompt2  │
│ systematic-debugging     │ 72    │ 指令具体性    │ baseline持平 │
├──────────────────────────┼───────┼──────────────┼──────────────┤
│ 平均                     │ 75    │              │              │
└──────────────────────────┴───────┴──────────────┴──────────────┘
```

**暂停等用户确认，再进入优化循环。**

### Phase 2: 优化循环

用户确认后，按基线分数从低到高排序，先优化最弱的。

```
for each skill:
  round = 0
  while round < MAX_ROUNDS (默认3):
    round += 1

    # Step 1: 诊断
    找出得分最低的维度（结构或效果都算）

    # Step 2: 提出改进方案
    针对最低维度，生成 1 个具体改进方案：
      - 改什么（具体段落/行）
      - 为什么改（对应 rubric 哪条）
      - 预期提升多少分

    # Step 3: 执行改进
    编辑 SKILL.md（用 Hermes patch/write_file）
    git add + commit（message: "optimize {skill}: {改进摘要}"）

    # Step 4: 重新评估
    - 结构维度：主 agent 重新打分
    - 效果维度：spawn 独立子代理重跑测试 prompt（关键！不能自己评自己）

    # Step 5: 决策
    if 新总分 > 旧总分:
      status = "keep"，更新旧总分
    else:
      status = "revert"
      git revert HEAD（创建新 commit 回滚，不用 reset --hard）
      - **异常：git revert 失败 → 提示用户手动介入，暂停优化流程**
      记录失败尝试到 results.tsv
      break  # 该 skill 到瓶颈，跳到下一个

    # Step 6: 日志
    results.tsv 追加行

  # === 每个 skill 优化完后的人类检查点 ===
  展示该 skill 的改动摘要：
    - git diff（改前 vs 改后）
    - 分数变化（哪些维度提升/下降）
    - 测试 prompt 输出对比（如果跑过的话）
  等用户确认 OK 再继续下一个 skill。
  如果用户说"不好"，回滚到该 skill 的优化前版本。
```

### Phase 2.5: 探索性重写（可选）

当 hill-climbing 连续 2 个 skill 都在 round 1 就 break（涨不动）时，提议一次「探索性重写」：

```
1. 选一个瓶颈 skill
2. git stash 保存当前最优版本
3. 从头重写 SKILL.md（不是微调，是重新组织结构和表达方式）
4. 重新评估
5. if 重写版 > stash版: 采用重写版
   else: git stash pop 恢复
```

这解决了 hill-climbing 的局部最优问题——有时候需要「先拆后建」才能突破瓶颈。
**必须征得用户同意后才执行。**

### Phase 3: 汇总报告

```
## 优化报告

### 总览
- 优化 skills 数：N
- 总实验次数：M
- 保留改进：X（Y%）
- 回滚次数：Z
- 实测验证：A 次完整测试 / B 次干跑

### 分数变化
┌──────────────────────────┬────────┬────────┬────────┐
│ Skill                    │ Before │ After  │ Δ      │
├──────────────────────────┼────────┼────────┼────────┤
│ github-pr-workflow       │ 78     │ 87     │ +9     │
│ systematic-debugging     │ 72     │ 83     │ +11    │
├──────────────────────────┼────────┼────────┼────────┤
│ 平均                     │ 75     │ 85     │ +10    │
└──────────────────────────┴────────┴────────┴────────┘

### 主要改进
1. [skill-A] 补充了边界条件处理，测试输出质量提升明显
2. [skill-B] 重组了 workflow 结构，baseline 对比优势增大
```

---

## test-prompts.json 格式

```json
[
  {"id": 1, "prompt": "用户会说的话", "expected": "期望输出的简短描述", "category": "happy_path"},
  {"id": 2, "prompt": "...", "expected": "...", "category": "edge_case"}
]
```

**字段说明：**
- `id`: 测试编号，用于追踪
- `prompt`: 用户实际会说的话（自然语言，不是指令式）
- `expected`: 期望输出的简短描述（不是完整输出，而是关键特征）
- `category`: 测试类型（`happy_path` / `edge_case` / `specific_problem`）

**示例（skill-optimizer 自身的 test-prompts.json）：**
```json
[
  {
    "id": 1,
    "prompt": "优化 github-pr-workflow 这个 skill",
    "expected": "应触发 Phase 0.5-2，输出包含 8 维评分、git diff、分数变化",
    "category": "happy_path"
  },
  {
    "id": 2,
    "prompt": "评估所有 skills 的质量",
    "expected": "应只执行 Phase 0.5-1，展示评分卡表格",
    "category": "edge_case"
  },
  {
    "id": 3,
    "prompt": "帮我改改 systematic-debugging，它效果不好",
    "expected": "应识别为优化请求，先诊断问题维度再针对性改进",
    "category": "specific_problem"
  }
]
```

文件位置：`~/.hermes/skills/{skill-name}/test-prompts.json`

---

## results.tsv 格式

```tsv
timestamp	commit	skill	old_score	new_score	status	dimension	note	eval_mode
2026-04-15T10:00	baseline	github-pr-workflow	-	78	baseline	-	初始评估	full_test
2026-04-15T10:05	a1b2c3d	github-pr-workflow	78	84	keep	边界条件	补充fallback	full_test
2026-04-15T10:10	b2c3d4e	github-pr-workflow	84	82	revert	指令具体性	过度细化	dry_run
```

新增 `eval_mode` 列：`full_test`（跑了子代理测试）或 `dry_run`（模拟推演）。
文件位置：`~/.hermes/skills/meta/skill-optimizer/results.tsv`

---

## 优化策略库

按优先级排序，每轮只做最高优先级的一个：

### P0: 效果问题（实测发现的）
- 测试输出偏离用户意图 → 检查 skill 是否有误导性指令
- 带 skill 比不带还差 → skill 可能过度约束，考虑精简
- 输出格式不符合预期 → 补充明确的输出模板

### P1: 结构性问题
- Frontmatter 缺少触发词 → 补充中英文触发词
- 缺少 Phase/Step 结构 → 重组为线性流程
- 缺少用户确认检查点 → 在关键决策处插入

### P2: 具体性问题
- 步骤模糊（"处理图片"）→ 改为具体操作和参数
- 缺少输入/输出规格 → 补充格式、路径、示例
- 缺少异常处理 → 补充 "如果 X 失败，则 Y"

### P3: 可读性问题
- 段落过长 → 拆分+用表格
- 重复描述 → 合并去重
- 缺少速查 → 添加 TL;DR 或决策树

### P4: 结构精简（文件大小控制）
- 详细示例移到引用段落 → 主流程保持简洁，用 "详见 X 章节" 引用
- 重复流程合并 → 不同章节的相似内容合并为单一参考段落
- Phase 编号优于抽象章节名 → "Phase 0-4" 比 "Introduction/Workflow/Conclusion" 更易执行
- 保留核心指令，细节外移 → SKILL.md 主文件 <22KB，细节可放 references/

### P5: Checkpoint 设计（D4 提升）
- ⚠️ 符号标记 → 视觉上突出决策点
- 显式触发条件 → "当 5+ subagents" 而非 "必要时询问用户"
- 三要素：触发条件 + 询问内容 + 用户选择影响

---

## 约束规则

1. **不改变 skill 的核心功能和用途** — 只优化"怎么写"和"怎么执行"，不改"做什么"
2. **不引入新依赖** — 不添加 skill 原本没有的 scripts 或 references 文件
3. **每轮只改一个维度** — 避免多个变更导致无法归因
4. **记录维度变化** — 每轮结束后明确标注哪个维度从 X 分→Y 分，便于分析瓶颈
4. **保持文件大小合理** — 优化后 SKILL.md 不应超过原始大小的 150%
5. **简洁为上** — 避免过度膨胀
6. **可回滚** — 所有改动在 git 分支上，用 git revert 而非 reset --hard
7. **评分独立性** — 效果维度必须用子代理或至少干跑验证，不能在同一上下文里「改完直接评」

---

### 使用方式

### 全量优化（推荐首次使用）
```
用户："优化所有 skills"
→ Phase 0-3 完整流程
→ 建议：先基线评估，选择分数最低的 5-10 个重点优化
```

### 单个优化
```
用户："优化 github-pr-workflow 这个 skill"
→ 只对指定 skill 执行 Phase 0.5-2
```

### 仅评估不改
```
用户："评估所有 skills 的质量"
→ 只执行 Phase 0.5-1（设计测试 prompt + 基线评估），不进入优化循环
```

### 问题诊断入口
```
用户："帮我改改 systematic-debugging，它效果不好"
→ 识别为"问题反馈型"请求，执行诊断流程：
   1. 先做 Phase 1 基线评估，找出得分最低的维度
   2. 分析用户反馈（"效果不好"）与评分的对应关系
   3. 针对最低维度提出改进方案
   4. 进入 Phase 2 优化循环
   
用户："这个 skill 输出太啰嗦了"
→ 诊断流程：
   1. 检查 SKILL.md 是否有"输出简洁"相关的指令
   2. 如果没有 → 补充输出格式约束（D5 指令具体性）
   3. 如果有但无效 → 用 test-prompts 实测验证（D8）
```

### 查看历史
```
用户："看看 skill 优化历史"
→ 读取并展示 results.tsv
```

---

## Hermes-Specific Notes

### 子代理执行
- 使用 Hermes `delegate_task` 工具 spawn 独立子代理
- 或使用 OpenCode ACP（非 pure 模式，指定 agent）
- 子代理与主代理隔离上下文，确保评分独立性

### Git 操作
- 在 `~/.hermes/skills/` 目录下执行 git 操作
- 使用 Hermes `terminal` 工具运行 git 命令
- 分支命名：`auto-optimize/YYYYMMDD-HHMM`

### 文件操作
- 使用 Hermes `patch` 工具做精确修改（推荐）
- 或使用 `write_file` 工具重写整个 SKILL.md
- 使用 `read_file` 工具读取 SKILL.md 内容

### 人工检查点
- 在 gateway/Telegram 上，使用 `clarify` 工具等待用户确认
- 在 CLI 上，直接暂停等待用户输入

### 路径约定
- skills 目录：`~/.hermes/skills/`
- 每个 skill 目录：`~/.hermes/skills/{category}/{skill-name}/`
- test-prompts.json：`~/.hermes/skills/{category}/{skill-name}/test-prompts.json`
- results.tsv：`~/.hermes/skills/meta/skill-optimizer/results.tsv`

---

## 设计灵感

> "You write the goals and constraints in program.md; let an agent generate and test code deltas indefinitely; keep only what measurably improves the objective."
> — Karpathy, autoresearch

本 skill 的对应关系：
- **program.md** → 本文件（评估 rubric 和约束规则）
- **train.py** → 每个 SKILL.md
- **val_bpb** → 8 维加权总分（含实测表现）
- **git ratchet** → 只保留有改进的 commit
- **test set** → 每个 skill 的 test-prompts.json

区别：增加了人在回路（autoresearch 是全自主的，skill 优化需要人的判断力），以及双重评估机制（结构+效果），因为 skill 的「好坏」比 loss 数值更微妙。

---

## 来源

本 skill 方法论来源于 alchaincyf/darwin-skill 项目，经 Hermes 适配改造：
- 去掉了展示层（result-card、screenshot 等）
- 适配了 Hermes 目录结构和工具链
- 保留了核心方法论：8 维 rubric + test-prompts + keep/revert + 人工检查点

原项目地址：https://github.com/alchaincyf/darwin-skill