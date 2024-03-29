import pygame 
from player import Player

class bar:
    x = 600
    y = 0
    def __init__(self, x, y, width, height, color = (0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)

class staminabar(bar):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (255, 242, 0)

    def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((1-Player.dash_cooldown/600)*self.rect.width), self.rect.height))

class healthbar(bar):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (250, 28, 0)
    


    def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((Player.health/250)*self.rect.width), self.rect.height))
         
class spell(bar):
     def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (255, 171, 0)

     def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((Player.dmgcounter/300)*self.rect.width), self.rect.height))
class slowed(bar):
     def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (220,220,220)

     def render(self, screen):
         super().render(screen)
         pygame.draw.rect(screen, self.color, pygame.Rect(self.rect.x, self.rect.y, int((Player.freezecooldown/60)*self.rect.width), self.rect.height))