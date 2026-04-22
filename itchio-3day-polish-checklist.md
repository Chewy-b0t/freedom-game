# itch.io 3-Day Polish Checklist

## Goal
Ship a stable, tournament-ready browser build in 3 days with repeatable QA.

## Day 1 — Core Stability + Wave 50 Validation

- [ ] Run full gameplay pass to wave 50 (desktop keyboard/mouse)
- [ ] Validate boss rotation on waves 35/40/45/50
- [ ] Validate boss kill progression + achievements still unlock
- [ ] Check for hard blockers:
  - [ ] Softlocks in pause/shop/settings/start menu
  - [ ] Broken input remaps
  - [ ] Save/load corruption after reload
  - [ ] Massive FPS drops during heavy particle scenes
- [ ] Smoke test Daily Challenge seed load

Acceptance:
- No game-breaking bug in 2 consecutive runs to 35+
- Bosses rotate correctly after wave 30

## Day 2 — UX/Balance Polish + Mobile/Controller

- [ ] Mobile pass (Android Chrome):
  - [ ] Touch movement + shooting + buttons
  - [ ] Settings navigation via touch only
  - [ ] PWA add-to-home + relaunch
- [ ] Controller pass:
  - [ ] Start screen navigation
  - [ ] In-run controls + pause + shop
  - [ ] Weapon switching and convert action
- [ ] Balance pass for tournament feel:
  - [ ] Wave 20-35 difficulty ramp sanity
  - [ ] Boss TTK sanity with default + common upgrades
  - [ ] Sats economy not starved or flooded

Acceptance:
- Input works across desktop/touch/controller with no blockers
- Difficulty curve feels fair through at least wave 30

## Day 3 — Release Candidate + Submission Package

- [ ] Final regression pass:
  - [ ] New game, mid-run reload, fresh browser session
  - [ ] Achievement persistence
  - [ ] Meta hub tabs and stats
  - [ ] Daily challenge start + finish
- [ ] Performance sanity:
  - [ ] No runaway memory/perf collapse after long session
- [ ] Itch.io package prep:
  - [ ] Verify title/description/screenshots
  - [ ] Confirm controls + known issues section
  - [ ] Upload build and do one full run from hosted page

Acceptance:
- Release candidate tagged and playable from itch.io page
- No known critical/high-severity bugs

---

## Bug Triage Severity

- **Critical**: crash, freeze, unplayable, broken progression, stuck UI
- **High**: major mechanic broken, severe input issues, save corruption
- **Medium**: visual bugs, occasional overlap issues, minor balance pain
- **Low**: cosmetic polish only

Fix priority: Critical > High > Medium > Low

---

## Quick Test Matrix (must-pass)

1. Start run -> wave 5 boss kill -> continue
2. Reach wave 30 -> kill The System -> continue to wave 35 boss
3. Reach wave 50 in at least one dev run
4. Reload browser mid-progression and verify state recovery
5. Mobile touch session (10+ mins)
6. Controller session (10+ mins)
7. Daily challenge run start/finish

---

## Notes

- Keep changes scoped. Avoid large refactors before deadline.
- Prefer deterministic, targeted fixes with quick validation.
- Log every bug with: reproduction steps, expected, actual, fix commit.
