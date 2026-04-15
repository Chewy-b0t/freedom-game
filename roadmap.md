# Freedom Fighters vs War Mongers Roadmap

## Status

`v0.1.9` is complete.

Completed for `v0.1.9`:
- Settings: brightness, UI scale, keybind hint toggle, touch controls
- Touch/mobile support for gameplay with dual-stick controls and mobile aim assist
- Mobile-oriented menu polish and more responsive start screen layout
- Boss accessibility overlays: readable attack name, cycle progress bar, shape/pattern telegraphs
- PWA install shell, manifest, icons, and service worker
- Performance work: cached grid rendering, reduced update-loop allocations, spatial grids for crowded collision paths
- Achievement verification/persistence fix
- Boss-wave readability tuning for touch play
- Manual Android validation including an installed-PWA first-boss clear
- Arctic/Jungle hazard config completed so post-wave-20 biome hazards no longer hard-stop gameplay
- Dev server LAN URL selection corrected so Android test instructions prefer the actual local-network IP over VPN adapters

## v0.1.9 Checklist

- [x] Brightness setting
- [x] UI scale setting
- [x] Keybind hint toggle
- [x] Touch controls toggle
- [x] Colorblind-friendly boss indicator improvements
- [x] Pattern-based boss telegraphs
- [x] Core mobile gameplay touch controls
- [x] Touch-friendly settings, talents, and keybind menu navigation
- [x] Installable Android/PWA shell
- [x] Final balance/readability pass
- [x] Achievement verification and persistence
- [x] Late-wave performance pass
- [x] Mobile boss-fight validation

## Next After v0.1.9

Priority order:

1. Use extra landscape side space intentionally without stretching the playfield.
2. Add an achievement gallery and clearer progression surfacing.
3. Push the next deeper performance pass only if late-wave profiling shows it is still needed.
4. Consider richer PWA polish like offline messaging and update prompts.

## Local Test Commands

Serve locally:

```bash
cd /home/y/workspace/freedom-game
python3 dev.py
```

Open the local URL printed by `dev.py`, usually:

```text
http://localhost:8080
```

Open from Android on the same network using the printed LAN URL, usually:

```text
http://<your-lan-ip>:8080
```

The LAN URL should now prefer your real home-network/private IP instead of a VPN tunnel address when both are present.

Stop the server with `Ctrl+C`.
