import pygame


class Boss:
    def __init__(self, damage, xpos, ypos, cooldown, timer):
        self.health = 1000
        self.damage = damage
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.timer = timer
        self.image = pygame.image.load('images/New Piskel (5) (1).png')

class Acid:
    def __init__(self):
        self.image = pygame.image.load()