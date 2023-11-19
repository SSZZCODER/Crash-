from turtle import Screen, speed
import pygame
import random
from gamelogic import GameLogic
from pygame.math import Vector2
from player import Player
import math

class Boss6:
    def __init__(self, damage, xPos, yPos):
        self.health = 2500
        self.damage = damage
        self.xPos = xPos
        self.yPos = yPos
        self.movetimer = 0
        self.moving = False
        self.newcenter = Vector2(0)
        self.velocity = Vector2(0)
        self.speed = 3
        self.image = pygame.image.load("images/snowmanboss.png")
        self.cooldown =0
        self.curse_cooldown = 0
        self.aura_image = pygame.image.load("images/snowaura.png")
        self.aura_image = pygame.transform.scale(self.aura_image, (240, 290))
        self.aura_rect = self.aura_image.get_bounding_rect()
        self.aura_angle = 0
       
    def curse(self): 
        if self.aura_rect.colliderect(pygame.Rect(GameLogic.playerPos, [50, 55])):
            Player.speed = 0
            Player.health -= .5 
            self.aura_angle +=1
        else:
            Player.speed = 3

    

    def move(self):
        if self.moving == False and self.movetimer == 0:
            self.newcenter.x = random.randint(0,750)
            self.newcenter.y = random.randint(0,750)
            self.velocity =  self.newcenter - Vector2(self.xPos, self.yPos)
            self.velocity.normalize()
            self.moving = True
            self.movetimer = 30

        elif self.moving == False and self.movetimer > 0:
            self.movetimer -=1
        if self.moving == True:
            if self.xPos > self.newcenter.x:
                self.xPos -= 1
            if self.yPos > self.newcenter.y:
                self.yPos -= 1
            if self.xPos < self.newcenter.x:
                self.xPos += 1
            if self.yPos < self.newcenter.y:
                self.yPos += 1
            if self.xPos == self.newcenter.x and self.yPos == self.newcenter.y:
                self.moving = False
    
    def takeDamage(self, damage):
        self.health -= damage
        GameLogic.playSoundBoss("bossdmg")
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)

    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(245, 10, 300, 50))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(245, 10, int((self.health/2500)*300), 50))
        aura_rot = pygame.transform.rotate(self.aura_image, self.aura_angle)
        screen.blit(aura_rot, self.aura_image.get_rect(center = (self.xPos, self.yPos)))
        self.aura_rect.center = (self.xPos, self.yPos)      
    def update(self, screen):
        self.move()            
        self.render(screen) 
        self.curse()



class IciclePierce:
    pass         