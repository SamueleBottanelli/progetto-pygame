import pygame, sys
from pygame.locals import *

class palla:
    def __init__(self,screen, pos, size, color,paddle,mattoncini=None) -> None:
        self.screen=screen
        self.image=pygame.Surface(size)
        pygame.draw.circle(self.image,color,[size[0]/2,size[1]/2],size[0]/2)
        self.rect=self.image.get_rect()
        self.mattoncini=mattoncini
        if mattoncini==None:
            self.mattoncini=[]
        self.paddle=paddle
        self.rect.x=600
        self.rect.y=400
    def muovi(self,velocity):
        self.rect.x+=velocity[0]
        self.rect.y+=velocity[1]

        if self.rect.x<=0:
            self.rect.x=0
            velocity[0]=velocity[0]*-1
        if self.rect.x>=600:
            self.rect.x=600
            velocity[0]=velocity[0]*-1

        if self.rect.y<=0:
            self.rect.y=0
            velocity[1]=velocity[1]*-1
        if self.rect.y>=400:
            self.rect.y=400
            velocity[1]=velocity[1]*-1
        if self.rect.colliderect(self.paddle.rect):
            velocity[1]=velocity[1]*-1
        for mattoncino in self.mattoncini:
            if self.rect.colliderect(mattoncino):
                velocity[1]=-velocity[1]
               
    
    def draw(self):
        self.screen.blit(self.image,self.rect)
