#!/usr/bin/env python3
import json
import re
from pathlib import Path

NAME_RE = re.compile(r"^S\d+")
ALLOW = set(json.loads(Path(__file__).with_name("allowlist.json").read_text()))


def load_rows(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def main() -> None:
    import sys

    base = Path(__file__).parent
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        text = sys.stdin.read()
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    else:
        rows = load_rows(base / "segments.ndjson")
    by_id = {int(r["id"]): r for r in rows}

    def collect_attrs(seg_id: int, seen: set[int]) -> set[str]:
        if seg_id in seen:
            return set()
        seen.add(seg_id)
        r = by_id.get(seg_id)
        if not r:
            return set()
        attrs = set(r.get("attrs") or [])
        for nid in r.get("seg") or []:
            attrs |= collect_attrs(int(nid), seen)
        return attrs

    valid: list[str] = []
    invalid: list[tuple[str, str, str]] = []

    def sol(attr: str) -> str:
        fixes = {
            "kid_gender": "Use `gender` with the same eq/to+from pattern (values must match how you store `gender`).",
            "last_generated_world": "Use `last_question_generated_world` with the same operator/value pattern.",
            "follows_count": "Use `following_count` (SOT name) with the same pattern.",
            "lessons_completed_count": "Use `lessons_completed_today` / `lessons_completed_this_week` / `lessons_completed_this_month` or `xp` + milestones; there is no `lessons_completed_count` in SOT.",
            "total_xp": "Use `xp` with the same numeric thresholds.",
            "days_since_signup": "Use `_created_in_customerio_at` with `timestamp_gt` / `timestamp_lt` offsets (seconds) instead of a counter attribute.",
            "days_since_last_active": "Use `last_sign_in_at` with timestamp operators and negative offsets (e.g. inactive 4d: to `timestamp_lt` value `-345600` paired with inverse `from`).",
            "leaderboard_rank_global": "Use `current_leaderboard` / `previous_leaderboard` JSON or per-world `world_*_leaderboard_position`; if global rank is required, Basel: add `leaderboard_rank_global` (number).",
            "leaderboard_rank_school": "Basel: add `leaderboard_rank_school` (number) or encode rank inside `current_leaderboard` and filter on that.",
            "leaderboard_rank_country": "Basel: add `leaderboard_rank_country` (number) or derive from `current_leaderboard` + `country`.",
            "favorite_world": "Use `favourite_category` and/or `last_question_generated_world` / per-world XP fields depending on intent.",
            "worlds_visited_count": "Use `worlds_totals` or specific `world_*_started_lessons` / `world_*_completed_lessons` counts; Basel: add `worlds_visited_count` (number) if you need a single counter.",
            "squads_joined_count": "Basel: add `squads_joined_count` (number); SOT only has `squad` string.",
            "lessons_generated_count": "Basel: add `lessons_generated_count` (number) or proxy via `questions_asked_today`/`questions_asked_this_week` if aligned.",
        }
        if attr in fixes:
            return fixes[attr]
        if attr in ALLOW:
            return "OK"
        return f"Basel: add `{attr}` with the correct type and sync it from backend, or replace with the closest SOT attribute."

    for r in rows:
        name = r.get("name") or ""
        if not isinstance(name, str) or not NAME_RE.match(name):
            continue
        seg_id = int(r["id"])
        attrs = collect_attrs(seg_id, set())
        bad = sorted(a for a in attrs if a not in ALLOW)
        if not bad:
            valid.append(name)
            continue
        for a in bad:
            invalid.append((name, a, sol(a)))

    print("VALID", len(valid))
    print("INVALID_ROWS", len(invalid))
    Path(base / "audit_result.json").write_text(
        json.dumps({"valid": sorted(valid), "invalid": invalid}, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
