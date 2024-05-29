import pygame

class boss:
    def __init__(self,pos,size,screen) -> None:
        self.rect=pygame.rect(pos[0],pos[1],size[0],size[1])
        self.screen=screen
    def draw(self):
        im=pygame.image.load()