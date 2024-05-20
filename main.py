import pygame, sys
from pygame.locals import *
from sbarra import sbarra
from palla import palla
from mattoncini import mattoncino
from punteggio import punteggio
dimensionifinestra=(600,400)
white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode(dimensionifinestra,0,32)
pygame.display.set_caption("pygame")
clock=pygame.time.Clock()
fps=60



pos=(300,375)
size=(150,25)
paddle=sbarra(screen,pos,size,white)
paddle.draw()

mattoncini=[]
pos1=(300,200)
size1=(25,25)
velocity=[8,8]
ball=palla(screen,pos1,size1,white,paddle,mattoncini)
ball.draw()

sizepunteggio=(50,20)
pospunteggio=(550,0)
puteggio=punteggio(screen,sizepunteggio,pospunteggio)


for i in range(3):
    bpos=[0,i*50]
    for j in range(6):
        brick=mattoncino(bpos,(100,50),screen,white,ball)
        brick.draw()
        mattoncini.append(brick)
        bpos[0]+=100
    bpos[1]+=50


while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    ball.muovi(velocity)

    key=pygame.key.get_pressed()
    if key[K_LEFT]:
        paddle.moveleft(8)
    if key[K_RIGHT]:
        paddle.moveright(8)
    
    

    
    screen.fill(black)
    paddle.draw()
    ball.draw()
    punteggio.draw()
    for b in mattoncini:
        if b.colpito()==False:
            mattoncini.remove(b)
        else:
            b.draw()
            punteggio.puntiA+=1
            

    


    pygame.display.flip()
    clock.tick(fps)

