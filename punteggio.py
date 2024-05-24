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
        self.image.fill(BLACK)
        font=pygame.font.Font(None,20)
        testo=f'       PUNTEGGIO: {self.puntiA}'
        text=font.render(testo,1,WHITE)
        term=pygame.image.load("blocco nero.jpeg")
        term=pygame.transform.scale(term,self.size)
        self.image.blit(term,(0,0))
        self.image.blit(text,(0,5))
        

        self.screen.blit(self.image, self.rect)
