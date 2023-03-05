from email.mime import image
from sys import _xoptions
import pygame

import pygame
from enemy import enemy

from gamelogic import GameLogic
class Fire():
    def __init__(self, angle,life, direction, xPos, yPos):
         self.angle = angle
         self.damage = 3
         self.speed = 3
         self.life = life
         self.image = pygame.image.load('images/New Piskel (35) (1).png')
         self.image = pygame.transform.scale(self.image,(35, 20))
         self.image = pygame.transform.rotate(self.image, self.angle)
         self.direction = direction
         self.xPos = xPos
         self.yPos = yPos

    def hit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.image.get_rect(center=(self.xPos, self.yPos))).colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos))):
                enemy.takeDamage(self.damage)
                print("Hit")
                GameLogic.spellList.remove(self)
    
    def render(self,screen):    
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos))) 

    def update(self, screen):
        self.xPos +=  self.direction[0]*self.speed
        self.yPos +=  self.direction[1]*self.speed  
        self.render(screen)
        Fire.hit(self)
        if self.life >0:
            self.life -= 1
        else:
            GameLogic.spellList.remove(self)

        