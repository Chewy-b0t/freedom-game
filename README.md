# Freedom Fighters vs War Mongers

2D top-down browser shooter built as a single `index.html` file. No framework, no build step, no package install.

Current state: `v0.1.9` is complete.

What is already in:
- Wave survival loop with shops, sats, power-ups, allies, combos, bosses, biomes, achievements, daily challenge, meta progression, skins, remappable keybinds, and talent trees
- Mobile/touch support with dual-stick controls, mobile aim assist, and gameplay touch buttons
- Accessibility settings including brightness, UI scale, reduced motion, colorblind mode, keybind hint toggle, and boss attack overlays with text + shape telegraphs

`v0.1.9` closeout notes:
- Mobile/PWA flow was validated on Android, including install and a first-boss clear
- Achievement persistence is now restored correctly from save data
- Late-wave collision work now uses lightweight spatial grids for enemies and enemy bullets
- Boss-wave minion pressure was reduced on early boss waves for better readability on touch devices
- Arctic/Jungle biome hazards now have complete runtime config, fixing the late-cycle freeze seen when Arctic hazards first trigger
- `dev.py` now prints a real LAN test URL instead of preferring VPN tunnel interfaces on machines with Proton or similar adapters

## Quick Start

Run the local dev server:

```bash
cd /home/y/workspace/freedom-game
python3 dev.py
```

Then open the local URL printed by `dev.py`, usually:

```text
http://localhost:8080
```

If you want to test from an Android device on the same network, use the LAN URL printed by `dev.py`. The dev server now prefers `8080`, reclaims it from your old dev process when possible, and otherwise falls forward automatically.

## Controls

Desktop:
- `WASD` or arrows: move
- Mouse click / hold: aim and shoot
- `Q`: convert nearby enemies
- `E`: open shop near a station
- `1-4`: switch weapons
- `ESC`: pause
- `P`: settings
- `J`: daily challenge from the start screen

Touch:
- Left side drag: movement stick
- Right side drag/tap: aim and shoot
- On-screen `WAKE`, `SHOP`, `PAUSE` buttons during gameplay
- Menus use direct tap targets

## Features

Combat and progression:
- Multiple enemy families including late-game variants like Fraud, Corruption, Taxes, Abuse, and Censorship
- Boss fights every 5 waves, including late bosses and attack-specific overlays
- Shops, sats, temporary boosts, weapon unlocks, persistent unlocks, and daily challenge mode
- Talent tree with offense, defense, and utility branches
- Persistent player XP, levels, skins, lifetime stats, and high score

Accessibility and UX:
- Brightness and UI scaling
- Reduced motion and colorblind mode
- Optional keybind hints
- Boss attack name panel, cycle bar, and pattern-based telegraphs
- Compact mobile-friendly start/menu layout
- Installable PWA shell for Android home-screen launch

Technical constraints:
- Single-file HTML game
- Zero runtime dependencies
- Works in modern desktop and mobile browsers

## Local Testing

Recommended manual test flow:

1. Start the server:
```bash
cd /home/y/workspace/freedom-game
python3 dev.py
```

2. Open the local URL printed by `dev.py`, usually:
```text
http://localhost:8080
```

3. Verify desktop basics:
- Start a run
- Move, shoot, pause, open settings
- Toggle brightness, UI scale, keybind hints, and touch controls
- Open keybinds and talents from settings

4. Verify touch/mobile behavior:
- Open the LAN URL on your Android phone in Chrome
- Confirm the compact start screen layout fits cleanly
- Start a run and test left-stick movement, right-side aim/shoot, and `WAKE` / `SHOP` / `PAUSE`
- Open settings, keybinds, talents, and shop with taps only
- Add it to the home screen and confirm standalone/fullscreen launch behavior

5. Verify accessibility overlays:
- Reach or spawn a boss
- Confirm the boss attack label panel updates
- Confirm the cycle progress bar moves
- Confirm ring/line/vertical/seeker/blink telegraphs appear distinctly

6. Verify persistence:
- Change settings
- Reload the page
- Confirm settings and high score persist

## Dev Notes

- `dev.py` injects a small live-reload script, so saving `index.html` refreshes connected browsers automatically.
- Syntax check for the embedded script can be done by extracting the `<script>` block to a temp `.js` file and running `node --check` on that file.
- The game currently lives entirely in `index.html`; there is no separate asset pipeline.
