import pygame, sys
from pygame.locals import *

class mattoncino:
    def __init__(self,pos,size,screen,color,ball) -> None:
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.rect=Rect(pos[0],pos[1],size[0],size[1])
        self.screen=screen
        self.ball=ball
    def colpito(self):
        if self.rect.colliderect(self.ball.rect):
            return False
    def draw(self):
        self.screen.blit(self.image,self.rect)
        