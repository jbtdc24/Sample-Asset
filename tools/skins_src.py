import glob, os
C = "D:/ANICHESS EDIT/Cosmetics/"
def g(p): return sorted(glob.glob(C + p))
SETS = {
 "astral":   dict(name="Astral", pcs=g("SETS/Astral/Pieces/Astral_*.png"), board=C+"SETS/Astral/Board and BG/Astral Board.jpg", bg=C+"SETS/Astral/Board and BG/Astral BG.png"),
 "circus":   dict(name="Circus Tent", pcs=g("SETS/CIRCUS TENT/pieces/*.png"), board=C+"SETS/CIRCUS TENT/CIRCUS TENT BOARD.png", bg=C+"SETS/CIRCUS TENT/CIRCUS TENT.png"),
 "candy":    dict(name="Candy Nightmare", pcs=g("SETS/Candy Nightmare/pieces/*.png"), board=C+"SETS/Candy Nightmare/Candy Nightmare Board.png", bg=C+"BG/Candy Nightmare Board.png"),
 "space":    dict(name="Deep Space", pcs=g("SETS/DEEP SPACE/pieces/*.png"), board=C+"SETS/DEEP SPACE/Deepspace Board.png", bg=C+"SETS/DEEP SPACE/Deep Space.png"),
 "doodle":   dict(name="Doodle Sketch", pcs=g("SETS/DOODLE SKETCH/pieces/*.png"), board=C+"SETS/DOODLE SKETCH/Doodle Sketch Board.png", bg=C+"SETS/DOODLE SKETCH/Doodle Sketch Bg.png"),
 "egypt":    dict(name="Egyptian Tomb", pcs=g("SETS/EGYPTIAN TOMB/Pieces/*.png"), board=C+"SETS/EGYPTIAN TOMB/EGYPTIAN TOMB.png", bg=C+"SETS/EGYPTIAN TOMB/EGYPTIAN TOMB BG.png"),
 "ember":    dict(name="Emberfall Forge", pcs=g("SETS/Emberfall Forge/Pieces_*.png"), board=C+"SETS/Emberfall Forge/Emberfall Forge Board.png", bg=C+"SETS/Emberfall Forge/Emberfall Forge BG.png"),
 "garden":   dict(name="Living Garden", pcs=g("SETS/Living Garden/Living-Garden_*.png"), board=C+"SETS/Living Garden/Living Garden Board.png", bg=C+"SETS/Living Garden/Living Garden Bg.png"),
 "tavern":   dict(name="Medieval Tavern", pcs=g("SETS/MEDIEVAL TAVERN/pieces/*.png"), board=C+"SETS/MEDIEVAL TAVERN/MEDIEVAL TAVERN.png", bg=C+"SETS/MEDIEVAL TAVERN/MEDIEVAL TAVERN BG.png"),
 "pirate":   dict(name="Pirate Cove", pcs=g("SETS/PIRATE COVE/pieces/*.png"), board=C+"SETS/PIRATE COVE/PIRATE COVE BOARD.png", bg=C+"SETS/PIRATE COVE/PIRATE COVE BG.png"),
 "sakura":   dict(name="Sakura Garden", pcs=g("SETS/SAKURA GARDEN/SakuraGarden_*.png"), board=C+"SETS/SAKURA GARDEN/Set/SakuraGardenBoard.jpg", bg=C+"SETS/SAKURA GARDEN/Set/SakuraGardenBG.jpg"),
 "scrap":    dict(name="Scrapyard", pcs=g("SETS/Scrapyard/Srapyard_*.png"), board=C+"SETS/Scrapyard/Scrapyard.png", bg=None),
 "steam":    dict(name="Steampunk", pcs=g("SETS/Steam punk/Steampunk_[BKQRp]*_*.png"), board=C+"SETS/Steam punk/Steampunk_Chessboard.jpg", bg=C+"SETS/Steam punk/Steampunk_Background.png"),
 "toybox":   dict(name="Toy Box", pcs=g("SETS/Toy Box/pieces/*.png"), board=C+"BOARDS/Toy Box.png", bg=C+"BG/Toy Box 1.png"),
 "ghost":    dict(name="Ghost Parade", pcs=g("GHOST PARADE/Pieces_*.png"), board=C+"GHOST PARADE/GHOST PARADE Board.jpg", bg=C+"GHOST PARADE/GHOST PARADE BG.png"),
 "pumpkin":  dict(name="Jack-O'-Lantern", pcs=g("JACK-O'-LANTERN KINGDOM/Pieces_*.png"), board=C+"JACK-O'-LANTERN KINGDOM/JACK-O'-LANTERN KINGDOM Board.jpg", bg=C+"JACK-O'-LANTERN KINGDOM/JACK-O'-LANTERN KINGDOM BG.png"),
 "franken":  dict(name="Frankenstein", pcs=g("Frankenstein/Frankenstein_*.png"), board=C+"Frankenstein/Frankenstein Board.jpg", bg=C+"Frankenstein/Frankenstein BG.png"),
 "mummy":    dict(name="The Mummy", pcs=g("THE MUMMY/themummy_*.png"), board=C+"THE MUMMY/THE MUMMY Board.jpg", bg=C+"THE MUMMY/THE MUMMY BG.png"),
 "vampire":  dict(name="Vampire Castle", pcs=g("VAMPIRE*/VAMPIRE-CASTLE_*.png"), board=glob.glob(C+"VAMPIRE*/*Board.jpg")[0], bg=glob.glob(C+"VAMPIRE*/*BG.png")[0]),
 "witch":    dict(name="Witch's Potion Lab", pcs=g("WITCH*/WITCH*_0000s_*.png"), board=glob.glob(C+"WITCH*/*Board.jpg")[0], bg=glob.glob(C+"WITCH*/*BG.png")[0]),
}
SETS["candy"]["board"]=C+"BOARDS/Candy Nightmare.png"; SETS["candy"]["bg"]=C+"SETS/Candy Nightmare/Candy Nightmare Board.png"
B,W="b","w"
ORDER={
 "astral":"bq wk bk wp bp wr br wn bn wb bb wq",
 "circus":"wk bk wq bq wn bn wb bb wr br wp bp",
 "candy":"bp wp br wr bb wb bn wn bq wq bk wk",
 "space":"bb wb bn wn br wr bp wp bk wk bq wq",
 "doodle":"br wr bp wp bb wb bn wn bk wk bq wq",
 "egypt":"bb wb bn wn br wr bp wp bk wk bq wq",
 "ember":"bb wb bq wq bk wk bn wn br wr wp bp",
 "garden":"wp bp wr br wn bn wb bb bk wk bq wq",
 "tavern":"wb bb wn bn wr br wp bp wk bk wq bq",
 "pirate":"bb wb bn wn br wr bp wp bk wk bq wq",
 "sakura":"br bb wb bk wk bn wn bp wp bq wq wr",
 "scrap":"wp bp wr br wb bb wn bn wq bq wk bk",
 "steam":"bb wb bk wk bn wn bq wq br wr bp wp",
 "toybox":"wb bb wn bn wr br wp bp wk bk wq bq",
 "ghost":"br wr bp wp bb wb bn wn bk wk bq wq",
 "pumpkin":"wr br wb bb wp bp wn bn wk bk wq bq",
 "franken":"br wr bp wp bb wb bn wn bk wk bq wq",
 "mummy":"wr br wp bp wb bb wn bn wk bk wq bq",
 "vampire":"br wr bp wp bb wb bn wn bk wk bq wq",
 "witch":"br wr bp wp bb wb bn wn bk wk bq wq",
}
