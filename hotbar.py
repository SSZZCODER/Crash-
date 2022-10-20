from cmath import rect
from turtle import position
import pygame

class  Hotbar:

    def __init__(self):
        self.rect = pygame.Rect(324, 671.5, 110,72.5)
        self.rectcolor = (135,135,135)
    
    def Rectangle(self, screen):   
        pygame.draw.rect(screen, (0,0,0), (320, 668.5, 118.75,79.5))
        pygame.draw.rect(screen,self.rectcolor, self.rect)
    def Hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rectcolor = (89, 89, 89)
        else:
            self.rectcolor = (135,135,135)
            
            


    def Render(self,screen):
        self.Hover()
        self.Rectangle(screen)