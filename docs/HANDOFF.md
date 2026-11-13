# Handoff
Status (2026-11-13): Anichess-style UI (top bar, spell card, spell icon grid with mana diamonds, cosmetics panel + picker, toolbar, record view). 21 skins in skins/<id>/ (12 pieces .webp, board.webp, bg.webp, thumb.webp). Spell icons in skins/spells/ (cropped from spell card screenshots). Every spell has a cast intro + its own FX/piece animation.
Next: check spell rules (Juke capture? which spells end the turn?); add new skins via tools/skins_src.py (ORDER = piece code per sorted file).
Rules: one HTML file, no build step for the page.
