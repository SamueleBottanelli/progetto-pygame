import pygame,sys
from pygame import *

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
class punteggio:
    def __init__(self, screen, size, pos):
        self.size=size
        self.pos=pos
        self.screen=screen
        self.puntiA=0
        self.image=pygame.Surface(size)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])

    def draw(self):
        size=self.size
        font=pygame.font.Font(None,25)
        testo=f'PUNTEGGIO: {self.puntiA}'
        im=pygame.image.load("punteggio.png")
        im=pygame.transform.scale(im,(size[0]+15,size[1]))
        text=font.render(testo,1,BLACK)
        
        

        self.screen.blit(im, (self.rect.x,self.rect.y))
        self.screen.blit(text, (self.rect.x+8,self.rect.y+12))
