import random

HEIGHT=500
WIDTH=500

cactuspostures=['cactus1','cactus2','cactus3','cactus4','cactus5']

trexpostures=['run1','run2']

trexspeed=1

gamestatus=0

trexpos=150

cactuspos=550

trexswitch=0

score=0

trex=Actor('run1',anchor=('left','bottom'))
trex.pos=(trexpos,HEIGHT/2)

floor=Actor('floor-1')
floor.pos=(WIDTH/2,HEIGHT/2)

cactus=Actor('cactus1',anchor=('left','bottom'))
cactus.pos=(cactuspos,HEIGHT/2)

cloud=Actor('1x-cloud')
cloud.pos=(WIDTH/2,50)

gameover=Actor('1x-restart')
gameover.pos=(WIDTH/2,HEIGHT/2)

def draw():
    screen.fill("white")

    trex.draw()
    floor.draw()
    cactus.draw()
    cloud.draw()

    screen.draw.text(str(score),(450,25),color='black',fontname='pixelmix_bold',fontsize=12)

    if gamestatus==1:
        gameover.draw()
        screen.draw.text('GAME OVER',center=(WIDTH/2,190),color='white',fontname='pixelmix_bold',
        ocolor='black',owidth=2,fontsize=20)

def update():
    global trexpos, trexpostures, trexswitch, score, gamestatus
    if gamestatus==0:
        FPI=7
        trex.image=trexpostures[trexswitch//FPI]
        trexswitch+=1
        if trexswitch //FPI >= len(trexpostures):
            trexswitch=0

        #cactus movement HERE \/
        cactus.x-=4
        if cactus.x<=-35:
            cactus.x=cactuspos
            cactus.image=random.choice(cactuspostures)

        #cloud movement here\/
        cloud.x-=4
        if cloud.x<=-10:
            cloud.x=450
        score+=2
        if trex.colliderect(cactus):
            gamestatus=1



def on_mouse_down(pos,button):
    global gamestatus, score
    if button == mouse.LEFT and gameover.collidepoint(pos):
        gamestatus=0
        score=0
        cactus.x=WIDTH+50