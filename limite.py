import pygame
class limite:
    def __init__(self,screen,pos,color) -> None:
        self.screen=screen
        self.rect=pygame.Rect(pos[0],pos[1],1100,6)
        size=(1100,6)
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.size=size
    def draw(self):
        term=pygame.image.load("blocco nero.jpeg")
        term=pygame.transform.scale(term,self.size)
        self.image.blit(term,(0,0))
        self.screen.blit(self.image,self.rect)