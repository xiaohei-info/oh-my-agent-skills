# Cron UX Checklist

Use this checklist before finalizing any user-facing cron prompt or after refactoring an existing one.

## Priority & Triage
- [ ] Does the first line clearly signal priority or urgency?
- [ ] Can the user tell from the first 1-2 lines whether this message matters now?
- [ ] Is the priority label meaningful in Telegram list / notification view?

## Routine Message Quality
- [ ] Is the default routine version short enough for fast mobile reading?
- [ ] Does the routine version avoid dumping all unchanged checks?
- [ ] Does it surface only what changed, triggered, became due, or is near-actionable?
- [ ] Is there one clear top-level takeaway or action state?

## Expanded Message Quality
- [ ] Is there an explicit expanded mode for important changes?
- [ ] Are the triggers for expansion clearly defined in the prompt?
- [ ] Does the expanded mode explain what changed and why it matters, without becoming a full essay?

## User Actionability
- [ ] Does the message tell the user what to do next, if anything?
- [ ] Are recommended actions capped and non-redundant?
- [ ] If user input is needed, is the requested reply format minimal and easy?
- [ ] If no action is needed, does the message say so explicitly?

## Noise Control
- [ ] Have repetitive caveats and boilerplate been minimized?
- [ ] Are long raw data dumps, logs, or tables omitted unless truly necessary?
- [ ] Are low-value untouched checks compressed into one sentence or omitted?
- [ ] Is historical recap included only when it changes interpretation?

## Readability
- [ ] Is the message structured for skimming, not deep reading?
- [ ] Are section counts kept small?
- [ ] Are bullets, short labels, and compact lines used instead of wall-of-text paragraphs?
- [ ] Does the wording fit Telegram/mobile rather than internal report style?

## Trustworthiness
- [ ] Are missing or conflicting data explicitly labeled instead of guessed?
- [ ] Does the message preserve the minimum context needed for the user to trust the conclusion?
- [ ] Is risk/blocker content present but capped to the most important items?
- [ ] Is the conclusion consistent with the facts shown?

## Reusability
- [ ] Is the message structure generic enough to reuse for similar cron types?
- [ ] Did you choose the right template: alert / digest / reminder / workflow-check?
- [ ] If the cron prompt is domain-specific, is the UX layer still general and user-friendly?

## Final Standard
A good user-facing cron message should feel like:
- easy to scan
- low-noise in normal conditions
- clearly escalated when something important changes
- explicit about next action or no-action
- trustworthy without over-explaining
