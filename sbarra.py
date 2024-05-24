import pygame, sys
from pygame.locals import *

class sbarra:
    def __init__(self, screen, pos, size, color) -> None:
        self.screen=screen
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.size=size
    def moveleft(self,pixels):
        if self.rect.x-pixels<=0:
            self.rect.x=0
        else:
            self.rect.x-=pixels
    def moveright(self,pixels):
        if self.rect.right+pixels>=1100:
            self.rect.x=1100-self.rect.size[0]
        else:
            self.rect.x+=pixels
    def draw(self):
        term=pygame.image.load("blocco nero.jpeg")
        term=pygame.transform.scale(term,self.size)
        self.image.blit(term,(0,0))
        self.screen.blit(self.image,self.rect)