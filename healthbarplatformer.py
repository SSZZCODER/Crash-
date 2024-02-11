import pygame
from player_platformer import Player_Platformer

class bar:
    x = 600
    y = 0
    def __init__(self, x, y, width, height, color = (0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)
class healthbar(bar):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (250, 28, 0)

    def render(self, screen, player):
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((player.health/250)*self.rect.width), self.rect.height))