import pygame, sys
from pygame.locals import*

pygame.init()

class powerup:
    def __init__(self,screen,pos,size,tipo,velocity,cond):
        self.screen=screen
        self.pos=pos
        self.size=size
        self.tipo=tipo
        self.velocity=velocity
        self.image=pygame.Surface(size)
        self.cond=cond
        if self.tipo==1:
            self.texture=pygame.image.load('./43-Breakout-Tiles.png')
        if self.tipo==2:
            self.texture=pygame.image.load('./44-Breakout-Tiles.png')
        if self.tipo==3:
            self.texture=pygame.image.load("./47-Breakout-Tiles.png")
        self.texture=pygame.transform.scale(self.texture,self.size)
        self.rect=Rect(pos[0],pos[1],size[0],size[1])
        self.image.blit(self.texture,(0,0))

    def draw(self):
        
        self.screen.blit(self.image,self.rect)

    def move(self):
        self.rect.y+=self.velocity