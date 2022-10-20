from re import S
from turtle import Screen
import pygame

class Inventory:
    def __init__(self):
        self.size = []
    

    def Draw(self, screen):
        
        pygame.draw.rect(screen, (0,0,0), (160,286.5, 430,90))
        pygame.draw.rect(screen, (135, 135, 135), (165,290, 420, 82))
        
       
