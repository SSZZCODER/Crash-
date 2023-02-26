from email.mime import image
from sys import _xoptions

import math
import pygame

import pygame
class Fire():
    def __init__(self, angle,damage, life, direction, xPos, yPos):
         self.angle = angle
         self.damage = damage
         self.speed = 5
         self.life = life
         self.image = pygame.image.load('images/New Piskel (35) (1).png')
         self.image = pygame.transform.scale(self.image,(35, 20))
         self.image = pygame.transform.rotate(self.image, self.angle)
         self.direction = direction
         self.xPos = xPos
         self.yPos = yPos
    def render(self,screen):
        
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos))) 
        
    def update(self, screen):
        self.xPos +=  self.direction[0]*self.speed
        self.yPos +=  self.direction[1]*self.speed  
        self.render(screen)
