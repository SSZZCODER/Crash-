import pygame
import random
from gamelogic import GameLogic
class objectspawner:
    def __init__(self, itemcount):
            self.itemcount = itemcount
            if len(GameLogic.objects[GameLogic.current_chunk]) == 0:
                self.spawnigloo()
            
    def spawnigloo(self):
            for i in range(self.itemcount):
                xpos = random.randint(50, 650)
                ypos = random.randint(50, 650)
                while xpos> 320 and xpos <400: 
                    xpos =random.randint(50, 650)
                while ypos> 320 and ypos<410:
                    ypos = random.randint(50, 650)
                GameLogic.objects[GameLogic.current_chunk].append(igloo(xpos, ypos))
class igloo:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.image_raw= pygame.image.load("images/igloo.png")
        self.image_raw = pygame.transform.scale(self.image_raw, (96 , 96 ))
        self.image = pygame.transform.rotate(self.image_raw, random.randint(0,360))
        self.rectangle = pygame.Rect(self.xpos, self.ypos, 85,50)
        self.rectangle.center= self.image.get_rect(center = (self.xpos, self.ypos)).center
    def update(self, screen):
        self.render(screen)
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xpos, self.ypos)))