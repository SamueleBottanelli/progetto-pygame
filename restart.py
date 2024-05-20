import pygame, sys
from pygame.locals import *
pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
class restart:
    def __init__(self,screen,pos,size):
        self.screen=screen
        self.pos=pos
        self.size=size
        self.image=pygame.Surface(size)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])

    def draw(self):
        self.image.fill(WHITE)
        font=pygame.font.Font(None,20)
        text=font.render("RESTART",1,BLACK)
        self.image.blit(text,(0,10))

        self.screen.blit(self.image,self.rect)
    
    def tocca(self):
        n=pygame.mouse.get_pos()
        if self.rect.colliderect(n[0],n[1],1,1):
            return True
        else:
            return False


