import random,pgzrun
WIDTH=300
HEIGHT=300
TITLE="gradient"
def draw():
    r=random.randint(0,255)
    g=0
    b=255
    w=WIDTH
    h=HEIGHT/3
    a=0
    c=100
    for i in range(18):
        rect=Rect((a,c),(w,h))
       # rect.center=150,150
        screen.draw.rect(rect,(r,g,b))
        w-=10
        h+=10
        g=g+10
        b=b-10
        a+=5
        c-=5








pgzrun.go()