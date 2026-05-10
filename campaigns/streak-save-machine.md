# Streak Save Machine Campaign

**Campaign ID:** 6
**Status:** Draft
**Type:** Behavioral (Segment-triggered)

## Trigger

**Segment:** S25 — Streak About to Break (ID: 43)
- Fires when `streak_at_risk = true` (user was active yesterday but not today)
- Auto-exits when user leaves the segment (saves their streak)

## Workflow

```
Entry Gate → Time Window (5pm–9pm Cairo) → Branch: Personal Best?
  ├─ YES → Push #1A (Personal Best Alert)
  └─ NO  → Push #1B (Standard Streak Save)
Both converge → 2-Hour Delay → Push #2 (Last Chance) → Exit
```

### Action Map

| ID | Type | Name |
|----|------|------|
| 10 | Entry Gate | filter_match_delay_action |
| 12 | Time Window | Wait until 5pm-9pm Cairo (Africa/Cairo, all days) |
| 13 | T/F Branch | about_to_hit_personal_best = true |
| 14 | Push | #1A — Personal Best Alert (template 7) |
| 15 | Push | #1B — Standard Streak Save (template 8) |
| 16 | Delay | 2 hours (7200s) |
| 17 | Push | #2 — Last Chance (template 9) |
| 11 | Exit | exit_action |

## Push Copy

### Push #1A — Personal Best Alert (about_to_hit_personal_best = true)
- **Title:** ONE more day, {{customer.kid_name}}! 🏆
- **Body:** Your {{customer.current_streak_days}}-day streak becomes your LONGEST EVER! Don't stop now — one lesson keeps it alive 🔥
- **Deep Link:** getxplain://lessons/generate

### Push #1B — Standard Streak Save
- **Title:** Your streak is fading, {{customer.kid_name}} 🔥
- **Body:** {{customer.current_streak_days}} days strong — don't let it end! One quick lesson keeps your streak alive ✨
- **Deep Link:** getxplain://lessons/generate

### Push #2 — Last Chance (2 hours after Push #1)
- **Title:** Last chance, {{customer.kid_name}}! ⏰
- **Body:** Your {{customer.current_streak_days}}-day streak ends at midnight. Just one quick lesson — you've got this! 💪
- **Deep Link:** getxplain://lessons/generate

## Rules Compliance

| Rule | Status |
|------|--------|
| Max 5 push/day | ✅ Campaign sends max 2 push per run. Message limits enabled. |
| Working hours 9am-9pm Cairo | ✅ Time window enforces 5pm-9pm Cairo (Africa/Cairo) |
| Exit on goal hit | ✅ `exit_on_trigger_or_filter_not_matched: true` — exits when streak saved |
| Kid-first messaging | ✅ Uses {{customer.kid_name}}, game-like tone |
| Personalized data | ✅ Uses streak count, personal best status |
| Deep links | ✅ Links to lesson generator |

## Required Attributes (Basel must fire from app)

- `streak_at_risk` (bool) — active yesterday, not today
- `about_to_hit_personal_best` (bool) — current streak = longest - 1
- `current_streak_days` (int) — current streak count
- `kid_name` (string) — kid's display name
