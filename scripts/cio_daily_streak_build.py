#!/usr/bin/env python3
"""Build Customer.io campaign 18 workflow payloads (encoding helpers)."""
import json
import urllib.parse
import base64

def enc(conditions):
    raw = json.dumps(conditions)
    return base64.b64encode(urllib.parse.quote(raw, safe='').encode()).decode()

def attr(field, op, value):
    return {"type": "attribute", "field": field, "operator": op, "value": value}

LESSONS_GT = enc([attr("lessons_completed_today", "gt", "0")])
LESSONS_EQ0 = enc([attr("lessons_completed_today", "eq", "0")])
ONBOARDED = enc([attr("onboarded", "eq", "true")])
STREAK_EQ0 = enc([attr("current_streak_days", "eq", "0")])
STREAK_GT0 = enc([attr("current_streak_days", "gt", "0")])

MILESTONE_DAYS = [3, 4, 6, 10, 14, 24, 30]
MILESTONE_CONDITIONS = [enc([attr("current_streak_days", "eq", str(d))]) for d in MILESTONE_DAYS]

if __name__ == "__main__":
    print("STREAK_AT_RISK", enc([attr("current_streak_days", "gt", "0"), attr("lessons_completed_today", "eq", "0")]))
    for d, c in zip(MILESTONE_DAYS, MILESTONE_CONDITIONS):
        print(d, c)
