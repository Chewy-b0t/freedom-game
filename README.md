<div align="center">

![Freedom Fighters vs War Mongers](assets/icons/icon.svg)

# 🎮 Freedom Fighters vs War Mongers

[![Version](https://img.shields.io/badge/version-v0.1.9-blue?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/license-Open-green?style=for-the-badge)](#)
[![Size](https://img.shields.io/badge/single--file-100%25-orange?style=for-the-badge)](#)
[![PWA](https://img.shields.io/badge/PWA-Installable-purple?style=for-the-badge)](#)
[![Platform](https://img.shields.io/badge/platform-Browser%20%7C%20Mobile-lightblue?style=for-the-badge)](#)

### A 2D top-down browser shooter — zero dependencies, one file, infinite chaos.

**[Play Now](#-quick-start)** · **[Report Bug](https://github.com/Chewy-b0t/freedom-game/issues)** · **[Request Feature](https://github.com/Chewy-b0t/freedom-game/issues)**

</div>

---

## 📖 About

**Freedom Fighters vs War Mongers** is a wave-based survival shooter that runs entirely in your browser. No installs, no frameworks, no build step — just a single `index.html` file that delivers a complete gaming experience.

Fight through endless waves of enemies, face devastating bosses, unlock powerful weapons, build your talent tree, and climb the leaderboards. Every run is different. Every boss is a test of skill. Every upgrade feels earned.

---

## Most Important

- Cross-compatibility is a top priority
- Gameplay must stay fast and smooth no matter what

---

## ✨ Features

<details>
<summary><b>⚔️ Combat & Progression</b></summary>

- 🌊 **Wave Survival Loop** — Escalating enemy pressure with unique biomes
- 👹 **Boss Fights** — Epic encounters every 5 waves with attack-specific telegraphs
- 🧬 **Enemy Families** — Fraud, Corruption, Taxes, Abuse, Censorship, and more
- 🛒 **Shops & Economy** — Earn sats, buy power-ups, unlock weapons
- 🌳 **Talent Tree** — Deep branching progression across Offense, Defense, and Utility
- 🏆 **Achievements** — Unlockable milestones with persistent tracking
- 📅 **Daily Challenge** — Unique daily runs for bonus rewards
- 🎨 **Skins & Meta Progression** — Persistent XP, levels, and cosmetic unlocks

</details>

<details>
<summary><b>📱 Mobile & Touch Support</b></summary>

- 🕹️ **Dual-Stick Controls** — Left stick movement, right stick aim & shoot
- 🎯 **Mobile Aim Assist** — Smart targeting assistance for touch play
- 📲 **Installable PWA** — Add to home screen for full-screen standalone experience
- 📐 **Responsive UI** — Compact menus optimized for smaller screens
- 🔘 **On-Screen Buttons** — WAKE, SHOP, PAUSE during gameplay

</details>

<details>
<summary><b>♿ Accessibility</b></summary>

- 🔆 **Brightness Control** — Adjustable display brightness
- 🔍 **UI Scaling** — Customize interface size for comfort
- 🎞️ **Reduced Motion** — Minimize animations for sensitive users
- 🎨 **Colorblind Mode** — Accessible color palette options
- 💡 **Keybind Hints** — Toggle control reference overlays
- 📊 **Boss Attack Overlays** — Text labels + shape-based telegraphs for all boss attacks

</details>

<details>
<summary><b>🎮 Controller Support</b></summary>

- 🎮 **Xbox/Standard Gamepad** — Full native controller support
  - Left stick: Move
  - Right stick: Aim
  - Triggers: Shoot
  - X: Convert enemies
  - Y: Open shop
  - LB/RB: Switch weapons
  - Start: Pause

</details>

---

## 🚀 Quick Start

### Prerequisites

- **Python 3** (for the dev server)
- Any modern web browser (Chrome, Firefox, Safari, Edge)

### Run Locally

```bash
# Clone the repository
git clone https://github.com/Chewy-b0t/freedom-game.git
cd freedom-game

# Start the dev server
python3 dev.py
```

Then open the URL printed by `dev.py` (usually `http://localhost:8080`)

### Mobile Testing

The dev server prints a LAN URL. Open it on any device on your network:

```
http://<your-lan-ip>:8080
```

> 💡 **Tip:** On Android, add the game to your home screen for a fullscreen PWA experience!

---

## 🎯 Controls

### Desktop

| Key | Action |
|-----|--------|
| `WASD` / `Arrows` | Move |
| **Mouse Click/Hold** | Aim & Shoot |
| `Q` | Convert nearby enemies |
| `E` | Open shop (near station) |
| `1-4` | Switch weapons |
| `ESC` | Pause |
| `P` | Settings |
| `J` | Daily challenge (start screen) |

### Touch

| Gesture | Action |
|---------|--------|
| **Left side drag** | Movement stick |
| **Right side drag/tap** | Aim & shoot |
| **On-screen buttons** | WAKE / SHOP / PAUSE |

### Controller

| Control | Action |
|---------|--------|
| **Left stick / D-pad** | Move |
| **Right stick** | Aim + shoot |
| **Triggers** | Also shoot |
| `A` | Confirm / start / open nearby shop |
| `B` | Back |
| `X` | Convert / settings |
| `Y` | Daily challenge / alt shop |
| `LB / RB` | Switch weapons |
| `Start` | Pause |

> Controller notes: the start screen includes a dedicated controller menu for remapping, vibration toggle, rumble strength, and test rumble. On Android/Chrome, touch overlays hide while controller input is active and come back when touch is used again.

---

## 🏗️ Architecture

```
freedom-game/
├── index.html              # 🎮 The entire game — no build step needed
├── dev.py                  # 🔧 Dev server with live reload & LAN support
├── assets/
│   └── icons/              # 📱 PWA & icon assets
│       ├── icon.svg        # 🎨 Source vector icon
│       ├── icon-192.png    # 🖼️ PWA icon (192x192)
│       ├── icon-512.png    # 🖼️ PWA icon (512x512)
│       ├── manifest.webmanifest  # 📱 PWA manifest for installable shell
│       └── sw.js           # ⚙️ Service worker for offline/PWA support
```

**Design Principles:**
- ✅ **Single file** — The entire game lives in `index.html`
- ✅ **Zero dependencies** — No npm, no bundler, no framework
- ✅ **Live reload** — Save `index.html` and connected browsers refresh automatically
- ✅ **Modern browsers** — Works on desktop and mobile without polyfills

---

## 🧪 Testing Guide

### Manual Test Flow

1. **Start the server:**
   ```bash
   python3 dev.py
   ```

2. **Desktop Basics:**
   - [ ] Start a run, move, shoot, pause
   - [ ] Open settings, toggle brightness/UI scale
   - [ ] Test keybind hints and touch controls
   - [ ] Open keybinds and talents from settings

3. **Touch/Mobile:**
   - [ ] Open LAN URL on Android (Chrome recommended)
   - [ ] Test left-stick movement + right-side aim/shoot
   - [ ] Verify WAKE / SHOP / PAUSE buttons
   - [ ] Navigate settings, talents, shop with taps only
   - [ ] Add to home screen → confirm fullscreen launch

4. **Boss Accessibility:**
   - [ ] Reach/spawn a boss
   - [ ] Verify attack label panel updates
   - [ ] Verify cycle progress bar moves
   - [ ] Verify ring/line/vertical/seeker/blink telegraphs

5. **Persistence:**
   - [ ] Change settings → reload page → verify they persist
   - [ ] Verify high score persists across sessions

---

## 🛠️ Development

### Live Reload

The dev server (`dev.py`) injects a live-reload script. Saving `index.html` automatically refreshes all connected browsers — no manual refresh needed.

### Syntax Checking

Extract the `<script>` block from `index.html` to a temp `.js` file, then run:

```bash
node --check temp.js
```

### Dev Server Features

- 🔁 Automatic live reload on file save
- 🌐 Smart LAN IP selection (prefers local network over VPN adapters)
- 📱 Mobile-friendly testing URL
- 🔄 Port reclamation (grabs `8080` from stale processes)

---

## 📸 Screenshots

> _Add gameplay screenshots here!_

<div align="center">
  <img src="https://via.placeholder.com/400x225/121725/f7931a?text=Gameplay+Screenshot+1" width="400" alt="Screenshot 1">
  <img src="https://via.placeholder.com/400x225/121725/4dd0e1?text=Gameplay+Screenshot+2" width="400" alt="Screenshot 2">
</div>

---

## 🗺️ Roadmap

### Completed (v0.1.9) ✅

- [x] Settings: brightness, UI scale, keybind hints, touch controls
- [x] Touch gameplay with dual-stick controls + aim assist
- [x] Mobile-responsive menu layout
- [x] Boss accessibility overlays (attack names, cycle bar, telegraphs)
- [x] PWA install shell, manifest, icons, service worker
- [x] Performance: cached grid rendering, spatial grids for collisions
- [x] Achievement verification & persistence
- [x] Boss-wave readability tuning for touch
- [x] Arctic/Jungle hazard config fixes
- [x] Dev server LAN URL correction

### Coming Soon 🔮

- [ ] Landscape space optimization (better use of wide screens)
- [ ] Achievement gallery & progression surfacing
- [ ] Deeper late-wave performance pass (if profiling shows need)
- [ ] Richer PWA polish (offline messaging, update prompts)

---

## 🤝 Contributing

Contributions are welcome! Whether it's:

- 🐛 Bug reports
- 💡 Feature suggestions
- 🎨 Art/assets
- 🔧 Code improvements

Feel free to [open an issue](https://github.com/Chewy-b0t/freedom-game/issues) or [submit a PR](https://github.com/Chewy-b0t/freedom-game/pulls).

---

<div align="center">

**Built with nothing but HTML, CSS, and JavaScript. No excuses.**

Made with ❤️ by [Chewy-b0t](https://github.com/Chewy-b0t)

⭐ **Star this repo if you enjoyed the game!** ⭐

</div>
