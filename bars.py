import pygame 
from player import Player
class bar:
    def __init__(self, x, y, width, height, color = (0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)

class staminabar(bar):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (0, 255, 255)
        
    def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((1-Player.dash_cooldown/600)*self.rect.width), self.rect.height))

