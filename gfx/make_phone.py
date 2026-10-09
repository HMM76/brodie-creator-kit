# Clean iMessage demo screen inside the getbrodie.com phone frame, rendered at 2x.
from PIL import Image, ImageDraw, ImageFont, ImageOps
G='/Users/imashkoksal/Downloads/brodie-carousel-engine-main/docs/outreach/brodie_creators/gfx/'
S=2
def sf(size, w=400):
    f=ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', int(size*S))
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
frame=Image.open(G+'phone-front-empty.png').convert('RGBA'); frame=frame.resize((frame.width*S, frame.height*S), Image.LANCZOS)
sx,sy,sw,sh=14*S,9*S,620*S,1312*S
scr=Image.new('RGBA',(sw,sh),(255,255,255,255)); d=ImageDraw.Draw(scr)
GREY=(233,233,235); BLUE=(27,140,255); INK=(0,0,0); MUTE=(142,142,147)
# status bar
d.text((44*S,22*S),"9:41",font=sf(22,600),fill=INK)
bx=sw-100*S; by=28*S
for i,hh in enumerate([5,8,11,14]): d.rounded_rectangle([bx+i*7*S,by+(14-hh)*S,bx+i*7*S+4*S,by+14*S],radius=1*S,fill=INK)
d.rounded_rectangle([sw-56*S,by,sw-22*S,by+15*S],radius=4*S,outline=INK,width=2*S); d.rounded_rectangle([sw-53*S,by+3*S,sw-27*S,by+12*S],radius=2*S,fill=INK)
# dynamic island
d.rounded_rectangle([sw//2-62*S,16*S,sw//2+62*S,52*S],radius=18*S,fill=(0,0,0))
# header
hy=70*S
d.rounded_rectangle([20*S,hy+10*S,78*S,hy+44*S],radius=17*S,fill=(240,240,242))
d.polygon([(38*S,hy+27*S),(46*S,hy+19*S),(46*S,hy+35*S)],fill=BLUE); d.text((52*S,hy+19*S),"12",font=sf(13,600),fill=INK)
av=Image.open(G+'brodie_avatar.png').convert('RGBA').resize((56*S,56*S),Image.LANCZOS); scr.alpha_composite(av,(sw//2-28*S,hy+2*S))
t="brodie"; f=sf(12,500); tw=d.textlength(t,font=f); d.text((sw//2-tw//2-6*S,hy+62*S),t,font=f,fill=INK); d.text((sw//2+tw//2-2*S,hy+63*S),"›",font=sf(12,400),fill=MUTE)
d.rounded_rectangle([sw-62*S,hy+12*S,sw-24*S,hy+40*S],radius=5*S,outline=INK,width=2*S); d.polygon([(sw-24*S,hy+20*S),(sw-14*S,hy+15*S),(sw-14*S,hy+37*S),(sw-24*S,hy+32*S)],fill=INK)
d.line([(0,hy+88*S),(sw,hy+88*S)],fill=(225,225,228),width=1*S)
# composer (bottom)
cy=sh-78*S
d.ellipse([18*S,cy+4*S,54*S,cy+40*S],fill=(240,240,242)); d.line([(36*S,cy+13*S),(36*S,cy+31*S)],fill=MUTE,width=2*S); d.line([(27*S,cy+22*S),(45*S,cy+22*S)],fill=MUTE,width=2*S)
d.rounded_rectangle([66*S,cy+2*S,sw-20*S,cy+42*S],radius=20*S,outline=(210,210,214),width=2*S)
d.text((84*S,cy+11*S),"iMessage",font=sf(15,400),fill=MUTE)
for i,hh in enumerate([6,12,18,12,6]): d.line([(sw-52*S+i*5*S,cy+22*S-hh*S//2),(sw-52*S+i*5*S,cy+22*S+hh*S//2)],fill=MUTE,width=2*S)
d.rounded_rectangle([sw//2-70*S,sh-14*S,sw//2+70*S,sh-9*S],radius=3*S,fill=INK)
# thread, laid out bottom-up above the composer
def bubble_img(path, right, y_bottom, w=380):
    im=Image.open(path).convert('RGB'); ratio=im.height/im.width; W=w*S; H=int(W*ratio)
    im=im.resize((W,H),Image.LANCZOS); m=Image.new('L',(W,H),0); ImageDraw.Draw(m).rounded_rectangle([0,0,W-1,H-1],radius=22*S,fill=255)
    x=sw-20*S-W if right else 20*S; y=y_bottom-H
    scr.paste(im,(x,y),m); return x,y,W,H
def bubble_txt(text, right, y_bottom, maxw=400):
    f=sf(17,400); words=text.split(); lines=[]; cur=""
    for wd in words:
        t=(cur+" "+wd).strip()
        if d.textlength(t,font=f)>maxw*S-32*S: lines.append(cur); cur=wd
        else: cur=t
    lines.append(cur); lh=22*S; H=len(lines)*lh+22*S; W=int(max(d.textlength(l,font=f) for l in lines))+32*S
    x=sw-20*S-W if right else 20*S; y=y_bottom-H
    d.rounded_rectangle([x,y,x+W,y+H],radius=20*S,fill=BLUE if right else GREY)
    # tail
    if right: d.polygon([(x+W-2*S,y+H-14*S),(x+W+8*S,y+H),(x+W-16*S,y+H-2*S)],fill=BLUE)
    else: d.polygon([(x+2*S,y+H-14*S),(x-8*S,y+H),(x+16*S,y+H-2*S)],fill=GREY)
    for i,l in enumerate(lines): d.text((x+16*S,y+11*S+i*lh),l,font=f,fill=(255,255,255) if right else INK)
    return x,y,W,H
yb=cy-14*S
d.text((sw-20*S-d.textlength("Delivered",font=sf(11,600)),yb-14*S),"Delivered",font=sf(11,600),fill=MUTE); yb-=20*S
x,y,W,H=bubble_txt("running it back",True,yb); yb=y-10*S
x,y,W,H=bubble_txt("just like last week, your right side lags. even your grip, then punch your right fist up first",False,yb); yb=y-8*S
x,y,W,H=bubble_img(G+'bench-analysis.jpg',False,yb); yb=y-14*S
x,y,W,H=bubble_img(G+'bench-raw.jpg',True,yb)
# play button + duration on the sent video
cx,cy2=x+W//2,y+H//2; d.ellipse([cx-26*S,cy2-26*S,cx+26*S,cy2+26*S],fill=(0,0,0,140)); d.polygon([(cx-8*S,cy2-13*S),(cx+14*S,cy2),(cx-8*S,cy2+13*S)],fill=(255,255,255))
d.rounded_rectangle([x+W-58*S,y+H-30*S,x+W-10*S,y+H-10*S],radius=6*S,fill=(0,0,0,150)); d.text((x+W-50*S,y+H-27*S),"0:14",font=sf(11,600),fill=(255,255,255))
# screen corner mask + composite into frame
mask=Image.new('L',(sw,sh),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,sw-1,sh-1],radius=92*S,fill=255)
out=frame.copy(); out.paste(scr,(sx,sy),mask)
out.save(G+'phone_v2.png'); print('phone_v2', out.size)
