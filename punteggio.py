import pygame,sys
from pygame import *

BLACK=(0,0,0)
WHITE=(255,255,255)
class punteggio:
    def__init__(self, screen, size, pos):
        self.size=size
        self.pos=pos
        self.text=text
        self.puntiA=0
        self.image=pygame.Surface(size)
        self.rect=pygame.rect(pos[0],pos[1],size[0],size[1])

    def draw(self):
        self.image.fill(BLACK)
        font=pygame.font.Font(None,81)
        text=font.render(str(self.puntiA),1,WHITE)
        self.image.blit(text,(250,0))
        

        self.sreen.blit(self.image, self.rect)
