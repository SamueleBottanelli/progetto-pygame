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
        self.size=size
    def draw(self):
        #self.image.fill(WHITE)
        #font=pygame.font.Font(None,20)
        #text=font.render("     RESTART",1,BLACK)
        
        im=pygame.image.load("restart.png")
        im=pygame.transform.scale(im,self.size)
        self.image.blit(im,(0,0))
        #self.image.blit(im,self.rect)


        self.screen.blit(im,self.rect)
    
    def tocca(self):
        n=pygame.mouse.get_pos()
        if self.rect.colliderect(n[0],n[1],1,1):
            coso=pygame.mouse.get_pressed()
            if coso[0]==True:
                return True
            else:
                return False
        else:
            return False

