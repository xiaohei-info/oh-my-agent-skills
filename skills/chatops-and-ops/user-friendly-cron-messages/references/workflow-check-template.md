# Workflow Check Template

Use this template for readiness checks, execution gates, pre-action validation, deployment readiness, account readiness, pre-trade checks, or any cron whose job is to tell the user whether to proceed, wait, or stop.

## Routine Check

```text
🟢 常规检查｜<topic>
<一句话结论：当前无重大变化 / 条件基本稳定 / 继续按原计划>

📍 当前状态:
- <ready / waiting / partially ready / blocked>

📊 关键条件:
- <condition 1>
- <condition 2>
- <condition 3>

🎯 当前结论:
- <go / wait / pause / blocked>

✅ 建议动作:
- <next step 1>
- <optional next step 2>

⚠️ 主要阻塞/风险:
- <single blocker or risk>

👀 下次重点检查:
- <watchpoint 1>
- <watchpoint 2>
```

## Expanded Check

```text
🟡 需要关注｜<topic>
<1-2 句话说明：本轮为什么更值得看，哪个条件变了>

📍 当前状态:
- <ready / waiting / partially ready / blocked>

📊 关键条件:
- <condition 1>
- <condition 2>
- <condition 3>
- <optional condition 4>

🔥 变化点:
- <what changed>
- <why it matters>
- <which prior assumption is weaker / invalid>

🎯 当前结论:
- <go / wait / pause / blocked>

✅ 建议动作:
- <action 1>
- <action 2>
- <optional action 3>

❌ 不建议动作:
- <avoid 1>
- <optional avoid 2>

⚠️ 风险/阻塞:
- <risk 1>
- <optional risk 2>

👀 下次重点检查:
- <watchpoint 1>
- <watchpoint 2>
- <watchpoint 3>
```

## Urgent Blocked Mode

```text
🔴 关键阻塞｜<topic>
⚠️ <一句话说明：当前不能继续推进的原因>

📍 当前状态:
- blocked

🔥 阻塞原因:
- <blocker 1>
- <blocker 2>

🎯 当前结论:
- 暂停推进 / 等待确认 / 先补条件

✅ 建议优先动作:
- <action 1>
- <action 2>

📝 若需用户回复，可直接回:
- <minimal reply format>
```

## Notes
- Workflow checks should end in a clear state: go / wait / pause / blocked.
- The user should not need to infer readiness from raw facts.
- Surface missing prerequisites early.
- If user input is needed, request the smallest useful confirmation.
- Avoid long background when the decisive blocker is already known.
