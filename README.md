# Neon Tide – Halloween map prototype

A playable prototype of the Halloween PVE map, so the flow can be seen and felt before the real art and battles exist.

**Run it:** open `index.html` in a browser, or serve the folder (`python3 -m http.server`), or deploy the repo to Vercel / GitHub Pages as a static site (no build step).

## What's in it
- **Curved 3D world.** The map sits on a curved, planet-like surface with a tilted perspective camera. The camera gets lower as you zoom in. Fog, stars, 3D fireflies, and drifting mist add depth.
- **Flow (four battles, one puzzle).** Battle 1 Pumpkin Field → Battle 2 Graveyard → Puzzle Sunken Pirate Ship → Battle 3 Science Laboratory → Boss Hall.
- **Estate / Mansion tabs.** The Mansion stays sealed until the shipwreck puzzle is solved.
- **Portrait pins and popover cards.** Each stop shows its opponent, reward, and first-try bonus, with a neon route that follows the painted roads.
- **Face-off → match intro → battle.** The battle is a turn-based stand-in for the real board battle. The puzzle is a timing mini-game.
- **Candy rewards.** Each stop gives candy, with +1 for clearing it on the first try. Candy is spent in the Treat Exchange (placeholder skins).
- **Hard mode + UFO.** Clearing Beginner unlocks Hard mode and drops a UFO into the wheat field.
- **Hidden tomb.** The ruined chapel on the west side is a clickable secret spot.
- **Sound.** All synthesized in the browser (ambient wind/drone, music box, battle loop, SFX). No audio files.

Demo shortcuts in the browser console: `HE.skip()` clears the current stop, `HE.reset()` wipes progress.

## Files
- `index.html` – the whole prototype. Stops, the flow, rewards, enemies, and road waypoints are config at the top of the script.
- `map/map_master_4k.png` – 3840×2160 master, cropped to 16:9 from the original 6880×3840 artwork.
- `map/map_web_2560.jpg` – 2560×1440 map used by the page.
- `map/map_data.js` – the same map embedded as data, used only when the page is opened straight from disk (browsers block local images in WebGL).
- `vendor/three.min.js` – three.js r128 (MIT licence), bundled so there's no CDN dependency.
- `tools/prep_map.py` – crop/export script and landmark-position calculation.

## Landmark positions (% of the 16:9 frame, origin top-left)
| Landmark | x | y |
|---|---|---|
| Entrance (path start) | 37.91 | 98.54 |
| Pumpkin Field | 19.77 | 58.23 |
| Graveyard | 37.91 | 61.81 |
| Sunken Pirate Ship | 71.17 | 70.77 |
| Science Laboratory | 56.56 | 35.83 |
| Boss Hall | 27.84 | 10.75 |
| UFO Wheat Field (after Beginner clear) | 74.19 | 26.88 |
| Hidden Tomb (secret spot) | 13.22 | 34.04 |
