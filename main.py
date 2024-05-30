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
from powerup import powerup

pygame.init()
def rimettipowerup(screen,mattoncini):
    powerup1list={}
    powerup2list={}
    n=randint(10,20)
    for i in range(n):
        r=randint(0,len(mattoncini)-1)
        if mattoncini[r] not in powerup1list:
            powerup1list[i]=mattoncini[r]
        else:
            i-=1
    powerup1list2=[]
    for i in range(n):
        velocity1=randint(3,8)
        powerup1=powerup(screen,(powerup1list[i].rect.x,powerup1list[i].rect.y),(10,5),1,velocity1,False)
        powerup1list2.append(powerup1)
    for i in range(n):
        k=randint(0,len(mattoncini)-1)
        if mattoncini[k] not in powerup2list:
            powerup2list[i]=mattoncini[k]
        
        else:
            i-=1
    powerup2list2=[]
    conta=[]
    for i in range(n):
        velocity2=randint(3,8)
        powerup2=powerup(screen,(powerup2list[i].rect.x,powerup2list[i].rect.y),(15,15),3,velocity2,False)
        powerup2list2.append(powerup2)
        conta.append(0)

    pallapowerup=[]
    velocitylista=[]

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
powerup1list={}
powerup2list={}
n=randint(5,7)
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
for i in range(n):
    r=randint(0,len(mattoncini)-1)
    if mattoncini[r] not in powerup1list:
        powerup1list[i]=mattoncini[r]

    else:
        i-=1
for i in range(n):
    k=randint(0,len(mattoncini)-1)
    if mattoncini[k] not in powerup2list:
        powerup2list[i]=mattoncini[k]
    
    else:
        i-=1
    
powerup1list2=[]
for i in range(n):
    velocity1=randint(3,8)
    powerup1=powerup(screen,(powerup1list[i].rect.x,powerup1list[i].rect.y),(10,5),1,velocity1,False)
    powerup1list2.append(powerup1)
condgameover=True
condricomincia=False
pallapowerup=[]
velocitylista=[]
powerup2list2=[]
conta=[]
for i in range(n):
    velocity2=randint(3,8)
    powerup2=powerup(screen,(powerup2list[i].rect.x,powerup2list[i].rect.y),(15,15),3,velocity2,False)
    powerup2list2.append(powerup2)
    conta.append(0)



for i in range(n*5):
    velocityx1=randint(4,8)
    velocityx2=randint(-8,-4)
    velocityy1=randint(4,8)
    velocityy2=randint(-8,-4)
    u=randint(0,1)
    if u==0:
        velocityx=velocityx1
    else:
        velocityx=velocityx2
    p=randint(0,1)
    if p==0:
        velocityy=velocityy1
    elif p==1:
        velocityy=velocityy2
    h=[velocityx,velocityy]
    velocitylista.append(h)
        
    condscompari=True 
#suono=pygame.mixer.Sound("boing-2-44164.mp3")
time=0
while(True):
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    if ball.rect.y==dimensionifinestra[1]-100:
        condscompari=False
        if pallapowerup!=[]:
            for i in range(len(pallapowerup)):
                if pallapowerup[i].rect.y==dimensionifinestra[1]-100:
                    condgameover=False
                else:
                    condgameover=True
                    break
        else:
            condgameover=False
    if condgameover==True:
        
        if time==(1/2):
            paddle.accorciasbarra()
        
        key=pygame.key.get_pressed()
        if key[K_LEFT]:
            paddle.moveleft(10)
        if key[K_RIGHT]:
            paddle.moveright(10)
        

        
        screen.blit(sfondo,(0,0))
        paddle.draw()
        
        limit1.draw()
        limit2.draw()
        for i in range(len(powerup1list2)):
            if powerup1list2[i].rect.colliderect(paddle.rect):
                for j in range(5):
                    palla2=palla(screen,(ball.rect.x,ball.rect.y),size1,white,paddle,mattoncini)
                    pallapowerup.append(palla2)
                    velocitylista.append(h)
        for i in range(len(powerup2list2)):
            if powerup2list2[i].rect.colliderect(paddle.rect):
                paddle.allungasbarra()
                time+=4

        if mattoncini==[]:
            pallapowerup.clear()
            condscompari=True
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
            elif lvl.lvl<5:
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
            rimettipowerup(screen,mattoncini)
            ball.rect.x=1100/2-5-3
            ball.rect.y=600/2-5+100
            #elif lvl.lvl==10:
        lvl.draw()

        l=[]
        for b in mattoncini:
            if pallapowerup!=[]:
                for i in pallapowerup:
                    #suono.play()
                    if i.rect.colliderect(b.rect): 
                        if b.color==blue:
                            if b not in l:
                                l.append(b)
                            punti.puntiA+=1 

                            for j in range(n):
                                if powerup1list[j]==b:
                                    powerup1list2[j].cond=True
                            for e in range(n):
                                if powerup2list[e]==b:
                                    powerup2list2[e].cond=True
                        else:
                            b.cambiacolore()
                            punti.puntiA+=1
            if b.colpito()==False:
                #suono.play()
                if b.color==blue:
                    mattoncini.remove(b)
                    punti.puntiA+=1 
                    for i in range(n):
                        if powerup1list[i]==b:
                            powerup1list2[i].cond=True
                    for i in range(n):
                        if powerup2list[i]==b:
                            powerup2list[i].cond=True
                
                else:
                    b.cambiacolore()
                    punti.puntiA+=1
            else:
                b.draw()
        for i in l:
            if i in l:
                i.cond=False
        for i in mattoncini:
            if i.cond==False:
                mattoncini.remove(i)
        if condscompari==True:
            ball.muovi(velocity)
            ball.draw()
        
        
        punti.draw()
       
            
        if pallapowerup!=[]:
            for i in range(len(pallapowerup)):
                
                pallapowerup[i].muovi(velocitylista[i])
            for i in pallapowerup:
                if i.rect.y>=dimensionifinestra[1]-100:
                    for j in range(len(pallapowerup)):
                        if pallapowerup[j]==i:
                            w=j
                    pallapowerup.remove(i)
                    
                    velocitylista.pop(w)
                else:
                    i.draw()
        for i in range(len(powerup1list2)):
            if powerup1list2[i].cond==True:
                powerup1list2[i].draw()
                powerup1list2[i].move()
        for i in range(len(powerup2list2)):
            if powerup2list2[i].cond==True:
                powerup2list2[i].draw()
                powerup2list2[i].move()
        

    if condgameover==False:
        ball.rect.y=300
        pallapowerup.clear()
        condscompari=True
        ricomincia.draw()
    
    condricomincia=ricomincia.tocca()
    if condricomincia:
        condgameover=True
        screen.blit(sfondo,(0,0))
        mattoncini.clear()
        pallapowerup.clear()
        powerup1list2.clear()
        powerup2list2.clear()
        condscompari=True
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
        time=0
        powerup1list={}
        powerup2list={}
        n=randint(5,7)
        for i in range(n):
            r=randint(0,len(mattoncini)-1)
            if mattoncini[r] not in powerup1list:
                powerup1list[i]=mattoncini[r]
            else:
                i-=1
        for i in range(n):
            k=randint(0,len(mattoncini)-1)
            if mattoncini[k] not in powerup2list:
                powerup2list[i]=mattoncini[k]
    
            else:
                i-=1
        powerup1list2=[]
        for i in range(n):
            velocity1=randint(3,8)
            powerup1=powerup(screen,(powerup1list[i].rect.x,powerup1list[i].rect.y),(10,5),1,velocity1,False)
            powerup1list2.append(powerup1)
        condgameover=True
        condricomincia=False
        pallapowerup=[]
        velocitylista=[]

        for i in range(n*5):
            velocityx1=randint(4,8)
            velocityx2=randint(-8,-4)
            velocityy1=randint(4,8)
            velocityy2=randint(-8,-4)
            u=randint(0,1)
            if u==0:
                velocityx=velocityx1
            else:
                velocityx=velocityx2
            p=randint(0,1)
            if p==0:
                velocityy=velocityy1
            elif p==1:
                velocityy=velocityy2
            h=[velocityx,velocityy]
            velocitylista.append(h)
            condscompari=True

            
            powerup2list2=[]
            conta=[]
            for i in range(n):
                velocity2=randint(3,8)
                powerup2=powerup(screen,(powerup2list[i].rect.x,powerup2list[i].rect.y),(15,15),3,velocity2,False)
                powerup2list2.append(powerup2)
                conta.append(0)
        


    
                

        
            
            
    if time>0:
        time-=(30/60)


    pygame.display.flip()
    clock.tick(fps)

