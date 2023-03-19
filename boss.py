import pygame
from gamelogic import GameLogic
class Boss:
    def __init__(self, damage, xpos, ypos):
        self.health = 1000
        self.damage = damage
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = 0
        self.curse_cooldown = 0
        self.timer = {"curse": 240}
        self.image = pygame.image.load('images/New Piskel (5) (1).png')
        
    def curse(self):
        self.cooldown = self.timer["curse"]
        GameLogic.playerspeedmulti = .5
    def update(self):
        if self.curse_cooldown != 0:
            self.curse_cooldown -= 1
        else:
            GameLogic.playerspeedmulti = 1
class Acid:
    def __init__(self):
        self.image = pygame.image.load()