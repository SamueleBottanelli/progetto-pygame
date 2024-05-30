import pygame, sys
from pygame.locals import *

red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

class mattoncino:
    def __init__(self,pos,size,screen,color,ball,cond=True) -> None:
        self.image=pygame.Surface(size)
        self.color=color
        self.rect=Rect(pos[0],pos[1],size[0],size[1])
        self.screen=screen
        self.color1=green
        self.color2=blue
        self.ball=ball
        self.size=size
        self.cond=cond
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    def colpito(self):
        if self.rect.colliderect(self.ball.rect):
            return False
    def draw(self):
        if self.color==red:
            texture=pygame.image.load("blocco rosso.jpeg")
        elif self.color==green:
            texture=pygame.image.load("blocco verde.jpeg")
        else:
            texture=pygame.image.load("blocco blu.jpeg")
        texture=pygame.transform.scale(texture,self.size)
        self.image.blit(texture,(0,0))
        self.screen.blit(self.image,self.rect)
    def cambiacolore(self):
        if self.color==(255,0,0):
            self.color=self.color1
        elif self.color==(0,255,0):
            self.color=self.color2
