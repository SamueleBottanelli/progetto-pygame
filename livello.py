import pygame

class livello:
    def __init__(self,pos,size,screen) -> None:
        self.screen=screen
        self.image=pygame.Surface(size)
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.size=size
        self.lvl=1
    def draw(self):
        size=self.size
        im=pygame.image.load("punteggio.png")
        im=pygame.transform.scale(im,(size[0]+15,size[1]))
        font=pygame.font.Font(None,25)
        testo=f'LIVELLO: {self.lvl}'
        text=font.render(testo,1,(0,0,0))
        self.screen.blit(im, (self.rect.x,self.rect.y))
        self.screen.blit(text, (self.rect.x+8,self.rect.y+12))
    
    def aggiorna(self):
        self.lvl+=1
    def resetta(self):
        self.lvl=1
    