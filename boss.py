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
    def updatecurse(self):
        if self.curse_cooldown != 0:
            self.curse_cooldown -= 1
        else:
            GameLogic.playerspeedmulti = 1
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xpos, self.ypos)))
    def update(self, screen):
        self.render(screen)
class Acid:
    def __init__(self, angle, direction, xPos, yPos):
        self.image = pygame.image.load("images/New Piskel (6) (1).png")
        self.image2 = pygame.image.load("images/New Piskel (7) (1).png")
        self.angle = angle
        self.damage = 5
        self.speed = 2
        self.direction = direction
        self.xPos = xPos 
        self.yPos = yPos

