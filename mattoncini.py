import pygame, sys
from pygame.locals import *

red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

class mattoncino:
    def __init__(self,pos,size,screen,color,ball) -> None:
        self.image=pygame.Surface(size)
        self.color=color
        self.rect=Rect(pos[0],pos[1],size[0],size[1])
        self.screen=screen
        self.color1=green
        self.color2=blue
        self.ball=ball
    def colpito(self):
        if self.rect.colliderect(self.ball.rect):
            return False
    def draw(self):
        self.image.fill(self.color)
        self.screen.blit(self.image,self.rect)
    def cambiacolore(self):
        if self.color==(255,0,0):
            self.color=self.color1
        elif self.color==(0,255,0):
            self.color=self.color2
