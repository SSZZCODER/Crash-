import pygame
import random
from gamelogic import GameLogic
from pygame.math import Vector2

class Boss:
    def __init__(self, damage, xPos, yPos):
        self.health = 1000
        self.damage = damage
        self.xPos = xPos
        self.yPos = yPos
        self.cooldown = 0
        self.curse_cooldown = 0
        self.timer = {"curse": 240}
        self.image = pygame.image.load('images/New Piskel (5) (1).png')
        self.image = pygame.transform.scale(self.image,(175, 200))
        self.movetimer = 0
        self.moving = False
        self.newcenter = Vector2(0)
        self.velocity = Vector2(0)
        self.speed = 3


    def acid(self):
        pass
    def move(self):
        pass
    def summon(self):
        pass
    def curse(self):
        self.cooldown = self.timer["curse"]
        GameLogic.playerspeedmulti = .5
    def updatecurse(self):
        if self.curse_cooldown != 0:
            self.curse_cooldown -= 1
        else:
            GameLogic.playerspeedmulti = 1
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
    def move(self):
        if self.moving == False and self.movetimer == 0:
            self.newcenter.x = random.randint(0,750)
            self.newcenter.y = random.randint(0,750)
            self.velocity =  self.newcenter - Vector2(self.xPos, self.yPos)
            self.velocity.normalize()
            self.velocity = self.velocity * self.speed
            self.moving == True
    
        elif self.moving == False and self.movetimer > 0:
            self.movetimer -=1
        if self.moving == True:
            if self.xPos != self.newcenter.x:
                self.xPos += self.velocity.x
            if self.yPos != self.newcenter.y:
                self.yPos += self.velocity.y
            if self.xPos == self.newcenter.x and self.yPos == self.newcenter.y:
                self.moving = False
                self.movetimer = 30
            
    def update(self, screen):
        self.move()
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
class Rocks:
        def __init__(self, angle, direction, xPos, yPos):
            self.image = pygame.image.load("images/New Piskel (6) (1).png")
            self.image2 = pygame.image.load("images/New Piskel (7) (1).png")
            self.angle = angle
            self.damage = 5
            self.speed = 2
            self.direction = direction
            self.xPos = xPos 
            self.yPos = yPos