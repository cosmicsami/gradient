import pgzrun,random,time
WIDTH=800
HEIGHT=600
TITLE="connecting the satalittes"

satalittes=[]
lines=[]

nextsatalittes=0
numofsatallites=random.randint(5,10)

for number in range(numofsatallites):
    s=Actor("satallite")
    s.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
    satalittes.append(s)



def draw():
    screen.blit("space",(0,0))
    for i in range (numofsatallites):
        satalittes[i].draw()
        screen.draw.text(str(i+1), (satalittes[i].pos[0],satalittes[i].pos[1]+20))    

pgzrun.go()    
