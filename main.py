import pygame, sys
from pygame.locals import *
from sbarra import sbarra
from palla import palla
from mattoncini import mattoncino
from punteggio import punteggio
from restart import restart



pygame.init()
dimensionifinestra=(600,490)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen=pygame.display.set_mode(dimensionifinestra,0,32)
pygame.display.set_caption("pygame")
clock=pygame.time.Clock()
fps=60



pos=(300,425)
size=(150,25)
paddle=sbarra(screen,pos,size,white)
paddle.draw()

mattoncini=[]
pos1=(300,200)                          
size1=(25,25)
velocity=[8,8]
ball=palla(screen,pos1,size1,white,paddle,mattoncini)
ball.draw()

sizepunteggio=(100,40)
pospunteggio=(499,0)
punti=punteggio(screen,sizepunteggio,pospunteggio)


sizericomincia=(100,35)
posricomincia=(250,dimensionifinestra[1]-35)
ricomincia=restart(screen,posricomincia,sizericomincia)





for i in range(1,4):
    bpos=[0,i*50]
    for j in range(6):
        brick=mattoncino(bpos,(100,50),screen,red,ball)
        brick.draw()
        mattoncini.append(brick)
        bpos[0]+=100
    bpos[1]+=50

condgameover=True
condricomincia=False
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if ball.rect.y==450:
        condgameover=False
    if condgameover==True:
        ball.muovi(velocity)

        key=pygame.key.get_pressed()
        if key[K_LEFT]:
            paddle.moveleft(8)
        if key[K_RIGHT]:
            paddle.moveright(8)
        
        

        
        screen.fill(black)
        paddle.draw()
        ball.draw()
    
    
    
        for b in mattoncini:
            if b.colpito()==False:
                if b.color==blue:
                    mattoncini.remove(b)
                    punti.puntiA+=1 
                else:
                    b.cambiacolore()
                    punti.puntiA+=1
            else:
                #b.draw()
                b.draw()

        punti.draw()
        ricomincia.draw()

        

    if condgameover==False:
        ball.rect.y=300
    
    condricomincia=ricomincia.tocca()
    if condricomincia:
        condgameover=True
        screen.fill(black)
        mattoncini.clear()
        for i in range(1,4):
            bpos=[0,i*50]
            for j in range(6):
                brick=mattoncino(bpos,(100,50),screen,red,ball)
                brick.draw()
                mattoncini.append(brick)
                bpos[0]+=100
            bpos[1]+=50
        ball.rect.x=600
        ball.rect.y=200
        velocity=[8,8]
        ball.draw()
        paddle.rect.y=425
        paddle.rect.x=300
        paddle.draw()
        punti.puntiA=0
        


    
                

        
            
            

    


    pygame.display.flip()
    clock.tick(fps)

