import pygame
from player import Player

class textbar:
    def __init__(self):
        self.font1 = pygame.font.Font('font/Elfboyclassic.ttf', 25)
        self.text1  =  self.font1.render("Welcome to the world ", True, (0,0,0) )
        self.text2 = self.font1.render("of Blocky!", True, (0,0,0))
        self.rect =  pygame.Rect(248, 507, 275, 80)
    def render(self, screen):
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(235, 500, 300, 95))
            pygame.draw.rect(screen, (101, 184, 145), self.rect)
 
            screen.blit(self.text1, (250, 508))
            screen.blit(self.text2, (250, 520))
    def update():
        pass