# Campaign build context

Operational notes for Customer.io Journeys in this repo’s workspace. API base: `https://eu.fly.customer.io`.

## Workspace

| Field | Value |
|--------|--------|
| Environment (workspace) ID | `218062` |
| Journeys UI (root) | https://eu.fly.customer.io/workspaces/218062 |

`build` numbers **2–9** are the product checklist used in this doc. **Customer.io campaign ids** are shown in the table (they are assigned by the API and are not equal to build numbers).

## Campaigns build 2–9 (journeys)

| Build | Customer.io campaign id | Name | Type | Entry | Workflow (summary) | State |
|-------|---------------------------|------|------|-------|---------------------|-------|
| 2 | [8](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/8) | Welcome — First day | behavioral | Segment **29** (S1 — Just Signed Up Today) | filter gate → **email** (template **11**, Xplain identity) → exit | draft |
| 3 | [11](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/11) | Day 2 check-in | behavioral | Segment **27** (S2 — Day 2 New User) | filter gate → email (template **16**) → exit | draft |
| 4 | [10](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/10) | Streak recovery | behavioral | Segment **53** (S26 — Streak Just Broke) | filter gate → email (template **15**) → exit | draft |
| 5 | [9](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/9) | Daily limit nurture | behavioral | Segment **71** (S54 — Hit Daily Limit Today) | filter gate → email (template **14**) → exit | draft |
| 6 | [12](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/12) | One week inactive | behavioral | Segment **35** (S13 — 1 Week Gone) | filter gate → email (template **13**) → exit | draft |
| 7 | [7](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/7) | Daily Limit Reset | transactional | Event **`daily_limit_reset`** | attribute update: `daily_limit_hit` → `false` → exit (no email) | draft |
| 8 | [14](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/14) | Challenge invite nudge | behavioral | Segment **115** (S96 — Pending Challenge Invite) | filter gate → email (template **17**) → exit | draft |
| 9 | [13](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/13) | Squad re-engage | behavioral | Segment **99** (S85 — Squad Going Quiet) | filter gate → email (template **12**) → exit | draft |

**Email sender:** templates use verified identity **Xplain** (`from_identity_id` **1**, `notifications@getxplain.ai`). All new journey emails are **`sending_state: draft`** until you review and start each campaign.

**App contract (build 7):** Track `daily_limit_reset` per person when their daily allowance should reset (e.g. local midnight or first open of a new day).

## Other journey (not in build 2–9 table)

| Customer.io id | Name | Notes |
|-----------------|------|--------|
| [6](https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/6) | Streak Save Machine | Pre-existing; push-focused (segment **43**). |

## Adding or editing email content

1. Add or reorder **`email_action`** nodes via campaign `update_type: add_actions` and a full **`edges`** list (see Customer.io skill `fly-api/campaigns.md`).
2. Set copy on the action’s template: `PUT /v1/environments/218062/templates/{template_id}` with `subject`, `body`, `preheader_text`, `from_identity_id`, etc.

## Links when discussing resources

Use the Journeys UI URLs above with `218062` — do not use `mailto:` for people; use `/journeys/people/...` as in Customer.io copilot guidance.
