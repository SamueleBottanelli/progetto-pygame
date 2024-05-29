import pygame, sys
from pygame.locals import *
from sbarra import sbarra
from palla import palla
from mattoncini import mattoncino
from punteggio import punteggio
from restart import restart
from random import randint
from limite import limite
from livello import livello
pygame.init()
dimensionifinestra=(1100,600)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen=pygame.display.set_mode(dimensionifinestra,0,32)
pygame.display.set_caption("pygame")
clock=pygame.time.Clock()
fps=60
sfondo=pygame.image.load("spazio1.jpg")
sfondo=pygame.transform.scale(sfondo,dimensionifinestra)
size=(80,5)
pos=(dimensionifinestra[0]/2-(size[0]/2),dimensionifinestra[1]-size[1]-100)

paddle=sbarra(screen,pos,size,white)
paddle.draw()

mattoncini=[]
pos1=(1100/2-5-3,600/2-5+100)                          
size1=(10,10)
velocity=[4,-4]
ball=palla(screen,pos1,size1,white,paddle,mattoncini)
ball.draw()

sizepunteggio=(150,40)
pospunteggio=(10,dimensionifinestra[1]-80)
punti=punteggio(screen,sizepunteggio,pospunteggio)
poslivello=(10,dimensionifinestra[1]-80+40)
sizelvl=(125,40)
lvl=livello(poslivello,sizelvl,screen)
lvl.draw()
sizericomincia=(200,70)
posricomincia=(1100/2-(sizericomincia[0]/2),dimensionifinestra[1]-80)
ricomincia=restart(screen,posricomincia,sizericomincia)


limit1=limite(screen,(0,25),white)
limit2=limite(screen,(0,510),white)
limit1.draw()
limit2.draw()

for i in range(2,10):
    bpos=[0,i*25]
    for j in range(22):
        coso=randint(0,2)
        coso2=randint(0,2)
        if coso2==0:
            if coso==0:
                brick=mattoncino(bpos,(50,25),screen,blue,ball)
            elif coso==1:
                brick=mattoncino(bpos,(50,25),screen,green,ball)
            else:
                brick=mattoncino(bpos,(50,25),screen,red,ball)
            brick.draw()
            mattoncini.append(brick)
        bpos[0]+=50
    bpos[1]+=25

condgameover=True
condricomincia=False
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if ball.rect.y==dimensionifinestra[1]-100:
        condgameover=False
    if condgameover==True:
        
        key=pygame.key.get_pressed()
        if key[K_LEFT]:
            paddle.moveleft(10)
        if key[K_RIGHT]:
            paddle.moveright(10)
        
        

        
        screen.blit(sfondo,(0,0))
        paddle.draw()
        
        limit1.draw()
        limit2.draw()
    
        if mattoncini==[]:
            lvl.aggiorna()
            ball.draw()
            if lvl.lvl>=5:
                for i in range(2,10):
                    bpos=[0,i*25]
                    for j in range(22):
                        coso=randint(0,2)
                        coso2=randint(0,2)
                        if coso2==0:
                            if coso==0:
                                brick=mattoncino(bpos,(50,25),screen,blue,ball)
                            elif coso==1:
                                brick=mattoncino(bpos,(50,25),screen,green,ball)
                            else:
                                brick=mattoncino(bpos,(50,25),screen,red,ball)
                            brick.draw()
                            mattoncini.append(brick)
                        bpos[0]+=50
                    bpos[1]+=25 
            else:
                for i in range(2,10):
                    bpos=[0,i*25]
                    for j in range(22):
                        coso=randint(0,2)
                        coso2=randint(0,4)
                        if coso2==0:
                            if coso==0:
                                brick=mattoncino(bpos,(50,25),screen,blue,ball)
                            elif coso==1:
                                brick=mattoncino(bpos,(50,25),screen,green,ball)
                            else:
                                brick=mattoncino(bpos,(50,25),screen,red,ball)
                            brick.draw()
                            mattoncini.append(brick)
                        bpos[0]+=50
                    bpos[1]+=25 

        lvl.draw()

        for b in mattoncini:
            if b.colpito()==False:
                if b.color==blue:
                    mattoncini.remove(b)
                    punti.puntiA+=1 
                else:
                    b.cambiacolore()
                    punti.puntiA+=1
            else:
                b.draw()
        ball.muovi(velocity)

        punti.draw()
        ball.draw()
   

        

    if condgameover==False:
        ball.rect.y=300
        ricomincia.draw()
    
    condricomincia=ricomincia.tocca()
    if condricomincia:
        condgameover=True
        screen.blit(sfondo,(0,0))
        mattoncini.clear()
        for i in range(2,10):
            bpos=[0,i*25]
            for j in range(22):
                coso=randint(0,2)
                coso2=randint(0,40)
                if coso2==0:
                    if coso==0:
                        brick=mattoncino(bpos,(50,25),screen,blue,ball)
                    elif coso==1:
                        brick=mattoncino(bpos,(50,25),screen,green,ball)
                    else:
                        brick=mattoncino(bpos,(50,25),screen,red,ball)
                    brick.draw()
                    mattoncini.append(brick)
                bpos[0]+=50
            bpos[1]+=25
        
        ball.rect.x=pos1[0]
        ball.rect.y=pos1[1]
        velocity=[4,-4]
        ball.draw()
        paddle.rect.y=pos[1]
        paddle.rect.x=pos[0]
        paddle.draw()
        punti.puntiA=0
        limit1.draw()
        limit2.draw()
   
        punti.draw()
        lvl.resetta()
        lvl.draw()
        


    
                

        
            
            

    


    pygame.display.flip()
    clock.tick(fps)

