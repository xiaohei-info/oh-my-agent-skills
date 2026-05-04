# Alert Template

Use this template for monitoring, threshold, health-check, error, or state-change cron jobs.

## Routine Mode

```text
🟢 常规更新｜<topic>
<一句话说明：本轮无重大变化 / 一切正常 / 暂无动作>

📍 当前状态: <current status>
📊 核心指标: <1-3 key metrics>
🎯 结论: <one action/status label>

🔥 当前需要关注:
- <triggered / near-triggered / changed item>
- <optional second item>

✅ 建议动作:
- <action 1>
- <optional action 2>

⚠️ 风险/阻塞:
- <single biggest risk or blocker>

👀 下次观察:
- <watchpoint 1>
- <watchpoint 2>
```

## Expanded Mode

```text
🔴 重要变化｜<topic>
⚠️ <1-2 句话直接说明发生了什么>

📍 当前状态: <current status>
📊 核心指标: <1-4 key metrics>
🎯 结论: <one action/status label>

🔥 变化原因:
- <what changed>
- <why it matters>
- <what prior assumption/state no longer holds>

✅ 建议动作:
- <action 1>
- <action 2>
- <optional action 3>

❌ 不建议:
- <thing to avoid>
- <optional second>

⚠️ 风险/阻塞:
- <risk 1>
- <optional risk 2>

👀 下次观察:
- <watchpoint 1>
- <watchpoint 2>
- <watchpoint 3>
```

## Notes
- First line must signal priority.
- Only show changed or relevant items.
- Do not dump every internal check.
- Keep routine mode short enough for fast mobile reading.
