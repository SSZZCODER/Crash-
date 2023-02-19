from email.mime import image
from sys import _xoptions

import math
import pygame

import pygame
class Fire():
    def __init__(self, damage, life, cooldown, angle, xPos, yPos):
         self.damage = damage
         self.speed = 5
         self.life = life
         self.cooldown = cooldown
         self.image = pygame.image.load('images/New Piskel (35) (1).png')
         self.angle = angle
         self.xPos = xPos
         self.yPos = yPos
    def render(self,screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos))) 

    def update(self, screen):
        self.xPos +=  math.cos(self.angle) *self.speed
        self.yPos +=  math.sin(self.angle) *self.speed  
        self.render(screen)
