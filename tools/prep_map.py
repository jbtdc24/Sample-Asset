from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
src = Image.open("/mnt/user-data/uploads/Halloween_map.png").convert("RGB")
W, H = src.size  # 6880x3840
# crop to exact 16:9 (trim width, keep full height)
cw = round(H * 16 / 9)  # 6827
x0 = (W - cw) // 2
crop = src.crop((x0, 0, x0 + cw, H))
master = crop.resize((3840, 2160), Image.LANCZOS)
master.save("map_master_4k.png", optimize=True)
# landmark positions as fractions of the 16:9 frame (display coords *3.44 -> source px)
S = 3.44
pts = {
 "Pumpkin Field": (400, 650),
 "Graveyard": (760, 690),
 "Sunken Pirate Ship": (1420, 790),
 "Science Laboratory": (1130, 400),
 "Boss Hall": (560, 120),
 "Hidden Tomb (proposed)": (270, 380),
 "UFO Wheat Field": (1480, 300),
 "Entrance (path)": (760, 1100),
}
out = {}
for k, (dx, dy) in pts.items():
    sx, sy = dx * S - x0, dy * S
    out[k] = (round((sx / cw) * 100, 2), round((sy / H) * 100, 2))
print(out)
ov = master.copy()
d = ImageDraw.Draw(ov)
f = ImageFont.load_default(size=56)
for k, (px, py) in out.items():
    X, Y = px / 100 * 3840, py / 100 * 2160
    d.ellipse([X-22, Y-22, X+22, Y+22], fill=(255,80,0), outline=(255,255,255), width=5)
    d.text((X+30, Y-20), k, fill=(255,255,255), font=f, stroke_width=4, stroke_fill=(0,0,0))
ov.resize((1920,1080)).save("overlay_check.png")
