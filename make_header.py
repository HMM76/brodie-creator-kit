# Email header in the getbrodie.com system: #0a0a0b, white Archivo 800 caps, one acid line, muted Plus Jakarta meta.
from PIL import Image, ImageDraw, ImageFont
F='/Users/imashkoksal/Downloads/brodie-carousel-engine-main/assets/fonts/'
def archivo(size, w=800, wd=100):
    f=ImageFont.truetype(F+'Archivo.ttf', size); f.set_variation_by_axes([w, wd]); return f
def jakarta(size, w=800):
    f=ImageFont.truetype(F+'PlusJakartaSans.ttf', size); f.set_variation_by_axes([w]); return f
W,H=1200,700; BG=(10,10,11); INK=(255,255,255); MUTED=(142,145,152); ACID=(217,255,61); LINE=(35,36,40)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); pad=56
# wordmark + pill
d.text((pad,pad-2),"BRODIE",font=jakarta(34,800),fill=INK)
tag="BUILT BY PENN STUDENTS"; tf=jakarta(17,700); tw=d.textlength(tag,font=tf)
px=W-pad-tw-36; d.rounded_rectangle([px,pad-6,px+tw+36,pad+34],radius=40,outline=(60,62,68),width=2); d.text((px+18,pad+4),tag,font=tf,fill=MUTED)
# headline, tight tracking by drawing per line
big=archivo(128,800,100)
lines=[("YOUR FIRST",INK),("PAID CONTENT",ACID),("GIG.",INK)]
y=185
for t,c in lines:
    d.text((pad-6,y),t,font=big,fill=c); y+=122
# bottom meta
d.line([(pad,H-82),(W-pad,H-82)],fill=LINE,width=2)
mf=jakarta(19,600)
d.text((pad,H-60),"ufc fighters · 100k+ creators · no experience needed",font=mf,fill=MUTED)
u="getbrodie.com"; uw=d.textlength(u,font=mf); d.text((W-pad-uw,H-60),u,font=mf,fill=ACID)
im.save('hero_banner.jpg',quality=92); print('hero_banner.jpg',im.size)
