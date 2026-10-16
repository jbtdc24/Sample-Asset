# Halloween Map – prototype

Open `index.html` in a browser (or serve the folder: `python3 -m http.server`).

## Files
- `map/map_master_4k.png` – 3840×2160 PNG master, cropped to 16:9 from the original 6880×3840 artwork.
- `map/map_web_2560.jpg` – 2560×1440 preview used by the page.
- `index.html` – the prototype. Landmarks, path order, and the linear flow are in the JS config at the top of the script.
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
| UFO Wheat Field (locked until Beginner is cleared) | 74.19 | 26.88 |
| Hidden Tomb (proposed, not in the route) | 13.22 | 34.04 |

## Crop behaviour
The stage is sized to cover the screen as a 16:9 box, so the cropping matches the spec: 16:10 cuts about 5% per side, 4:3 cuts more on the sides, and 21:9 cuts the top and bottom.

## Flow (current)
Pumpkin Field → Graveyard → Pirate Ship → Science Lab → Boss Hall. Clearing all five unlocks Hard mode and the UFO. Change `FLOW` in `index.html` to try other orders.
