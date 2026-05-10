# GetXplain.AI — Campaign Build Context

## Workspace

- **Platform:** Customer.io EU (`eu.fly.customer.io`)
- **Environment ID:** `218062`
- **Account ID:** `152066`
- **App:** GetXplain.AI — AI learning app for kids (Egypt/MENA)
- **Current goal:** 5,000 user-generated lessons in public library (currently ~30)
- **Goal split:** 60% keep users active / 40% drive lesson generation

## Hard Rules (non-negotiable)

- Max **5 push/day**, **3 email/day** per user
- **Working hours only:** 9am–9pm Cairo (Africa/Cairo, GMT+2)
- **Exit immediately** when user takes desired action
- **80% kid / 20% parent** — all push targets the kid
- Copy: kid-first, game-like, personalized with real data, short (title <50 chars, body <100)
- Deep-link to the exact screen
- No conversion/sales/subscription language

## API Patterns (proven working)

### Create campaign
```
POST /v1/environments/218062/campaigns
body: {"campaign": {"name": "...", "type": "behavioral", "description": "..."}}
```
Response gives `workflow_action_ids`: [FILTER_ID, EXIT_ID] and initial edge.

### Set segment trigger
```
PUT /v1/environments/218062/campaigns/{id}
body: {"campaign": {"update_type": "recipients", "type": "behavioral", "anchors": "<base64>"}}
```
Anchors encoding: `base64(urlEncode(JSON))` where JSON = `[{"negate":false,"segments":[SEGMENT_ID],"type":"segments_negatable"}]`

### Set event trigger
```
PUT /v1/environments/218062/campaigns/{id}
body: {"campaign": {"update_type": "recipients", "type": "transactional", "event": "event_name"}}
```
Response gives `workflow_action_ids`: [EXIT_ID] only (no filter gate).

### Add actions
```
PUT /v1/environments/218062/campaigns/{id}
body: {"campaign": {"update_type": "add_actions", "edges": [...]}, "actions": [...]}
```
Placeholder IDs: `-N` = first action in array, `-1` = last. Edges replace entirely.

### Set push content
```
PUT /v1/environments/218062/templates/{template_id}
body: {"template": {"subject": "title", "body_json": "{\"title\":\"...\",\"body\":\"...\",\"link\":\"...\"}"}}
```
**body_json must be a STRING**, not an object.

### Set email content
```
PUT /v1/environments/218062/templates/{template_id}
body: {"template": {"subject": "...", "body": "<html>...</html>", "from_identity_id": ID}}
```

### Enable message limits
```
PUT /v1/environments/218062/campaigns/{id}
body: {"campaign": {"update_type": "global_settings", "use_message_limits": true}}
```

### Condition encoding (for branches)
`base64(urlEncode(JSON.stringify([{type, field, operator, value}])))`
Python: `base64.b64encode(urllib.parse.quote(json_str).encode()).decode()`

### Action types
- `push_action`, `email_action` — message (auto-creates template)
- `delay_seconds_action` — fixed wait (`delay` in seconds; 3600=1h, 7200=2h, 86400=1d)
- `delay_time_window_action` — wait for time window (`start_time`, `end_time`, `days`, `zone`)
- `conditional_branch_action` — T/F (`conditions`: single base64 string, 2 edges)
- `multi_split_branch_action` — multi-path (`multi_conditions`: array of base64, N+1 edges)
- `conditional_wait_action` — wait until condition or timeout (`multi_conditions`, `delay`, `exit_type`)
- `attribute_update_action` — set customer attribute
- `exit_action` — exit node (create new ones for branch exits)

### Edge types
- `{"from": "A", "to": "B", "type": "continue"}` — linear
- `{"from": "A", "to": "B", "type": "branch", "index": 0}` — branch path

### Graph rules
- All branches must reconverge at same downstream action (or dedicated exit_action)
- Every non-exit action needs exactly 1 outgoing edge
- Edges list replaces entirely on every update

## Segment IDs Needed

| Segment | ID | Used By Campaign |
|---------|-----|-----------------|
| S25 Streak About to Break | 43 | ~~#1 Done~~ |
| S55 Hit Limit Yesterday | 74 | #2 Daily Limit Reset |
| S63 Their Lesson Got Used | 90 | #3 Lesson Got Famous |
| S64 Famous Creator | 82 | #3 Lesson Got Famous |
| S91 Friend Overtook Me | 120 | #4 Friend Overtook You |
| S11 3-Day Gap | 33 | #5 Inactivity Ladder |
| S13 1 Week Gone | 35 | #5 Inactivity Ladder |
| S14 2 Weeks Gone | 34 | #5 Inactivity Ladder |
| S15 3 Weeks Gone | 31 | #5 Inactivity Ladder |
| S146 Power User Going Quiet | 167 | #6 Power User Going Quiet |
| S43 Has Abandoned Lesson | 72 | #7 Abandoned Lesson |
| S44 Abandoned Recently | 68 | #7 Abandoned Lesson |
| S96 Pending Challenge Invite | 115 | #8 Pending Challenge |
| S49 Never Generated | 70 | #9 First Lesson |
| S50 Tried Once | 76 | #9 First Lesson |
| S27 Approaching Personal Best | 42 | branch condition |
| S114 Boys 6-8 | 126 | demographic branches |
| S115 Boys 9-11 | 134 | demographic branches |
| S116 Boys 12-14 | 135 | demographic branches |
| S117 Boys 15-17 | 137 | demographic branches |
| S118 Girls 6-8 | 127 | demographic branches |
| S119 Girls 9-11 | 129 | demographic branches |
| S120 Girls 12-14 | 138 | demographic branches |
| S121 Girls 15-17 | 130 | demographic branches |

## Campaign Specs (2–9)

---

### #2 Daily Limit Reset
**Goal:** 40% generation — drive the 5K lesson target
**Trigger:** Segment S55 (Hit Limit Yesterday, ID: 74)
**Flow:**
```
Entry → Time Window (9am-10am Cairo) → Push "Your 5 lessons unlocked!"
  → Delay 7h → T/F Branch (generated today?)
    → NO: Push "4 lessons still waiting"
    → YES: Exit
  → Exit
```
**Key attributes:** `kid_name`, `lessons_generated_today`, `their_lessons_completed_by_others`, `daily_limit_hit`
**Exit:** First lesson generated OR leaves S55
**Copy direction:** Excitement about fresh daily quota, mention impact if their lessons were used by others

---

### #3 Your Lesson Got Famous
**Goal:** 40% generation — emotional engine for 5K
**Trigger:** Event `lesson_used_by_other` (transactional/event-triggered)
**Flow:**
```
Entry on event → Push "Someone learned from your lesson!"
  → Delay 24h → T/F Branch (generated new lesson?)
    → NO: Push "Your lessons help others — create another?"
    → YES: Exit
  → T/F Branch (their_lessons_completed_by_others >= 20)
    → YES: Attribute Update (power_creator = true) → Email "Tarek thanks you"
    → NO: Exit
```
**Key attributes:** `kid_name`, `last_generated_topic`, `their_lessons_completed_by_others`, `lessons_generated_count`
**Exit:** New lesson generated
**Copy direction:** Celebrate impact, show how many kids learned from them, drive more creation

---

### #4 Friend Overtook You
**Goal:** 60% retention — competitive trigger
**Trigger:** Segment S91 (Friend Overtook Me, ID: 120)
**Flow:**
```
Entry → Time Window (3:30pm-9pm Cairo) → Push "{friend} just passed your XP!"
  → Exit
```
**Key attributes:** `kid_name`, `friend_overtook_xp`, `total_xp`, `kid_gender`, `age_bucket`
**Exit:** Any XP-earning activity OR leaves S91
**Copy direction:** Competitive tone, vary by demographic:
- Boys 9-11: "Are you going to let them win?!"
- Girls 9-11: "You two are neck and neck!"
- Teens: "Reclaim your spot"
**Note:** Single push, minimal — the trigger itself is the hook

---

### #5 Inactivity Ladder
**Goal:** 60% retention — graduated win-back
**Trigger:** 4 separate campaigns, one per gap tier
**Campaigns:**
| Gap | Segment | Channel | Tone |
|-----|---------|---------|------|
| 3 days | S11 (ID:33) | Push | Soft, use favorite_world |
| 7 days | S13 (ID:35) | Push + Email | Stats recap |
| 14 days | S14 (ID:34) | Email | "Here's what you built" |
| 21 days | S15 (ID:31) | Email to parent (Tarek personal) | Genuine concern |

**Flow per tier:**
```
Entry → Time Window (appropriate hour) → Message → Exit
```
**Key attributes:** `kid_name`, `parent_name`, `parent_email`, `favorite_world`, `lessons_completed_count`, `total_xp`, `days_since_last_active`
**Exit:** Any activity OR leaves segment
**Copy direction:** Escalating urgency, increasingly personal

---

### #6 Power User Going Quiet
**Goal:** 60% retention — VIP save
**Trigger:** Segment S146 (Power User Going Quiet, ID: 167)
**Flow:**
```
Entry → Delay 0 (immediate) → Push "The leaderboard misses you at #{rank}"
  → Delay 48h → T/F Branch (still in S146?)
    → YES: Email from Tarek to parent
    → NO: Exit
  → Exit
```
**Key attributes:** `kid_name`, `parent_name`, `leaderboard_rank_global`, `total_xp`, `lessons_generated_count`
**Exit:** Any activity
**Copy direction:** Push to kid (status/rank loss), Email to parent (personal from Tarek, genuine)

---

### #7 Abandoned Lesson Recovery
**Goal:** 60% retention
**Trigger:** Segment S44 (Abandoned Recently, ID: 68)
**Flow:**
```
Entry → Time Window (3:30pm-9pm Cairo) → Push "You left '{title}' at {%}"
  → Exit
```
**Key attributes:** `kid_name`, `abandoned_lesson_title`, `abandoned_lesson_progress`, `current_squad_name`, `squads_joined_count`
**Exit:** Lesson completed or new lesson started
**Copy direction:** Remind specific lesson + progress %, mention squad XP if in squad

---

### #8 Pending Challenge Response
**Goal:** 60% retention
**Trigger:** Segment S96 (Pending Challenge Invite, ID: 115)
**Flow:**
```
Entry → Push "Someone challenged you! 🥊"
  → Delay 6h → T/F Branch (still pending?)
    → YES: Push "Your challenger is waiting..."
    → NO: Exit
  → Delay 12h → T/F Branch (still pending?)
    → YES: Push "Challenge expires soon"
    → NO: Exit
  → Exit
```
**Key attributes:** `kid_name`, `challenge_pending_invite`, `last_challenge_result`
**Exit:** Challenge accepted/declined OR leaves S96
**Copy direction:** FOMO + urgency escalation

---

### #9 First Lesson Generated Celebration
**Goal:** 40% generation — hook new creators
**Trigger:** Event `lesson_generated` with filter `lessons_generated_count = 1` (first ever)
**Flow:**
```
Entry on event → Push "You created your first lesson! 🎉"
  → Delay 24h → T/F Branch (lessons_generated_count >= 2?)
    → NO: Push "Ready for lesson #2? Try {unused_method}"
    → YES: Exit
  → Delay 48h → T/F Branch (lessons_generated_count >= 3?)
    → NO: Push "Creators with 5+ lessons get special recognition"
    → YES: Exit
  → Exit
```
**Key attributes:** `kid_name`, `lessons_generated_count`, `last_generation_method`, `preferred_generation_method`
**Exit:** 3 lessons generated
**Copy direction:** Celebrate, nudge method variety, tease creator recognition milestone

---

## Already Built

- **#1 Streak Save Machine** — Campaign ID: 6, draft, segment S25 (ID:43)
  - Actions: 10(gate) → 12(time window) → 13(branch) → 14/15(push) → 16(delay) → 17(push) → 11(exit)
  - Templates: 7, 8, 9
