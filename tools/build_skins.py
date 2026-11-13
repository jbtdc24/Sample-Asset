import sys,os,json,numpy as np
from PIL import Image
from skins_src import SETS,ORDER
OUT=sys.argv[1];meta={}
def lum(a):return a[...,:3].mean(-1)
for k,s in SETS.items():
    d=f"{OUT}/{k}";os.makedirs(d,exist_ok=True)
    codes=ORDER[k].split();assert sorted(codes)==sorted(c+t for c in "wb" for t in "kqrbnp"),k
    for f,code in zip(s["pcs"],codes):
        im=Image.open(f).convert("RGBA");im=im.crop(im.getbbox());sz=max(im.size)
        sq=Image.new("RGBA",(sz,sz));sq.paste(im,((sz-im.width)//2,sz-im.height));sq=sq.resize((180,180),Image.LANCZOS)
        sq.save(f"{d}/{code}.webp",quality=88)
    b=Image.open(s["board"]).convert("RGB");N=b.width;a=np.asarray(b.resize((512,512))).astype(float);L=lum(a)
    best=None
    for m in np.arange(0.0,0.14,0.001):
        o=m*512;q=(512-2*o)/8;e=0
        for i in range(1,8):
            l=o+i*q
            for r in range(8):
                y=int(o+r*q+q/2)
                e+=abs(L[y-3:y+3,int(l-4):int(l-1)].mean()-L[y-3:y+3,int(l+1):int(l+4)].mean())
                e+=abs(L[int(l-4):int(l-1),y-3:y+3].mean()-L[int(l+1):int(l+4),y-3:y+3].mean())
        if best is None or e>best[0]:best=(e,m)
    m=best[1];o=m*512;q=(512-2*o)/8;v=np.zeros((8,8))
    for r in range(8):
        for c in range(8):
            y0,x0=int(o+r*q+q*.25),int(o+c*q+q*.25);v[r,c]=L[y0:int(y0+q*.5),x0:int(x0+q*.5)].mean()
    par=(np.add.outer(np.arange(8),np.arange(8))%2==0);best=(v[par].mean()-v[~par].mean(),m)
    sc,m=best;o=int(m*N);b=b.crop((o,o,N-o,N-o))
    if sc<0:b=b.transpose(Image.FLIP_LEFT_RIGHT)  # top-left (a8) must be light
    b.resize((1024,1024),Image.LANCZOS).save(f"{d}/board.webp",quality=82)
    b.resize((96,96),Image.LANCZOS).save(f"{d}/thumb.webp",quality=80)
    if s["bg"]:
        g=Image.open(s["bg"]).convert("RGB");g.thumbnail((1920,1920));g.save(f"{d}/bg.webp",quality=72)
    meta[k]=dict(name=s["name"],bg=bool(s["bg"]))
    print(k,"inset %.3f"%m,"flip" if sc<0 else "",round(abs(sc)))
json.dump(meta,open(f"{OUT}/skins.json","w"),indent=1)
