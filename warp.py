from re import X
from tkinter import Y
import pygame
import player
from player import Player


class Warp:

    def __init__(self, xpos, ypos, width, height, color):   
        self.rect = pygame.Rect(xpos, ypos, width,height)
        self.color = color
    def Touched(self):  
        if self.rect.collidepoint(Player.playercenter):
            return True
        else:
            return False
    def Render(self,screen):
        pygame.draw.rect(screen,self.color ,self.rect)
    def Update(self, screen):
        self.Touched()
        self.Render(screen) 