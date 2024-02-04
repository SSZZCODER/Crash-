import pygame
from player_platformer import Player_Platformer

class healthbar(bar):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (250, 28, 0)
    


    def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((Player_Platformer.health/250)*self.rect.width), self.rect.height))