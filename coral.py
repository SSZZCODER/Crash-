import pygame
import random
from gamelogic import GameLogic
class objectspawner:
    def __init__(self, itemcount):
            self.itemcount = itemcount
            if len(GameLogic.objects[GameLogic.current_chunk]) == 0:
                self.spawncoral()
            
    def spawncoral(self):
            for i in range(self.itemcount):
                xpos = random.randint(50, 650)
                ypos = random.randint(50, 650)
                GameLogic.objects[GameLogic.current_chunk].append(coral(xpos, ypos))
class coral:     
    def __init__(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos
        self.image= pygame.image.load('images/coral.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rectangle = pygame.Rect(self.xpos, self.ypos, 85,50)
        self.rectangle.center= self.image.get_rect(center = (self.xpos, self.ypos)).center
    def update(self, screen):
        self.render(screen)
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xpos, self.ypos)))