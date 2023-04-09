import pygame
import random
from gamelogic import GameLogic
class objectspawner:
    def __init__(self, itemcount):
            self.itemcount = itemcount
            if len(GameLogic.objects[GameLogic.current_chunk]) == 0:
                self.spawnbush()
    def spawnbush(self):
            for i in range(self.itemcount):
                xpos = random.randint(50, 650)
                ypos = random.randint(50, 650)
                GameLogic.objects[GameLogic.current_chunk].append(bush(xpos, ypos))
class bush:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.image= pygame.image.load("images/bush.png")
        self.image = pygame.transform.scale(self.image, (200, 225))
    def update(self, screen):
        self.render(screen)
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xpos, self.ypos)))