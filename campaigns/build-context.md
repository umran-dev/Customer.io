# Campaign build context

Operational notes for Customer.io Journeys in this repo’s workspace. API base: `https://eu.fly.customer.io`.

## Workspace

| Field | Value |
|--------|--------|
| Environment (workspace) ID | `218062` |
| Journeys UI (root) | https://eu.fly.customer.io/workspaces/218062 |

## Daily Limit Reset (campaign id `7`)

| Field | Value |
|--------|--------|
| UI | https://eu.fly.customer.io/workspaces/218062/journeys/campaigns/7 |
| Type | Event-triggered (`transactional`) |
| Entry event | `daily_limit_reset` |
| Workflow | `attribute_update_action` → sets `daily_limit_hit` to `false` → `exit_action` |
| State | Draft until started in UI or via API |

**App contract:** Track `daily_limit_reset` per person when their daily allowance should reset (e.g. local midnight or first session of a new day). No email step is configured.

**Related segments (examples):**

- `71` — S54 - Hit Daily Limit Today (uses `daily_limit_hit` / `daily_limit_hit` attribute-change style rules)
- `74` — S55 - Hit Limit Yesterday

## Adding email to a flow

1. Add an `email_action` to the campaign (`update_type: add_actions`, full edge list per `fly-api/campaigns.md` in Customer.io skills).
2. Set content on the action’s template: `PUT /v1/environments/218062/templates/{template_id}` with `subject`, `body`, `from_identity_id`, etc. New message actions ship with an empty template until updated.

## Links when discussing resources

Use the Journeys UI URLs above with `218062` — do not use `mailto:` for people; use `/journeys/people/...` as in Customer.io copilot guidance.
