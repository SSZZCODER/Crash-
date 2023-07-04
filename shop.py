from email.mime import image
from sys import _xoptions
import pygame

class Shop:
    def __init__(self, xPos, yPos):
        self.xPos = xPos    
        self.yPos = yPos
        self.image = pygame.image.load("images/shop.png")
        self.image = pygame.transform.scale(self.image, (98 *7.75,73 * 7.75))
        self.rifle = pygame.image.load("images/rifle.png")
        self.rifle = pygame.transform.scale(self.rifle, (90*2,18*2))
        self.bomb = pygame.image.load("images/bomb.png")
        self.bomb = pygame.transform.scale(self.bomb, (12*12,12*12))
        self.sword = pygame.image.load("images/sword.png")
        self.sword = pygame.transform.scale(self.sword, (17*2 ,64*2))
     
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))
        screen.blit(self.rifle, (88, 305))
        screen.blit(self.bomb, (340, 255))
        screen.blit(self.sword, (613,255))
    def update(self, screen):
        self.render(screen)

