from re import S
from turtle import Screen
import pygame

class Inventory:
    def __init__(self):
        self.rect = pygame.Rect(324, 671.5, 110,72.5)
        self.rectcolor = (135,135,135)

        self.size = []
    

    def Draw(self, screen):

        pygame.draw.rect(screen, (0,0,0), (160,286.5, 430,90))
        pygame.draw.rect(screen, (135, 135, 135), (165,290, 420, 82))
  
        
       
