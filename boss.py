from turtle import Screen, speed
import pygame
import random
from gamelogic import GameLogic
from pygame.math import Vector2
from player import Player
class Boss:
    def __init__(self, damage, xPos, yPos):
        self.health = 2500
        self.damage = damage
        self.xPos = xPos
        self.yPos = yPos
        self.cooldown = 0
        self.curse_cooldown = 0
        self.timer = {}
        self.skull = pygame.image.load('images/skull.png')
        self.skull = pygame.transform.scale(self.skull,(70, 80))
        self.image = pygame.image.load('images/New Piskel (5) (1).png')
        self.image = pygame.transform.scale(self.image,(175, 200))
        self.aura_image = pygame.image.load("images/aura.png")
        self.aura_image = pygame.transform.scale(self.aura_image, (240, 290))
        self.aura_rect = self.aura_image.get_bounding_rect()
        self.movetimer = 0
        self.moving = False
        self.newcenter = Vector2(0)
        self.velocity = Vector2(0)
        self.speed = 3
        self.acids = []
        self.acidtimer = 100
    def acid(self, screen):
        if self.acidtimer <= 0:
            self.acids.append(Acid(0,0,self.xPos, self.yPos, GameLogic.playerPos))
            self.acidtimer = 100
        elif self.acidtimer > 0:
            self.acidtimer -= 1
        if len(self.acids) > 0:
            for acid in self.acids:
                acid.update(screen)
                if acid.destroyed == True:
                    self.acids.remove(acid)
    def move(self):
        pass
    def summon(self):
        pass
    def curse(self, screen):
        if self.aura_rect.colliderect(pygame.Rect(GameLogic.playerPos, [50, 55])):
            Player.speed = 1.5
            Player.health -= .25 
            screen.blit(self.skull, (GameLogic.playerPos[0], GameLogic.playerPos[1]-50))
            GameLogic.playSoundBoss("curse")
        else:
            Player.speed = 3
    def attack(self):
        return [0, 0]
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
        screen.blit(self.aura_image, self.aura_image.get_rect(center = (self.xPos, self.yPos)))
        self.aura_rect.center = (self.xPos, self.yPos)
      # pygame.draw.rect(screen, (0, 255, 0), self.aura_rect)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(245, 10, 300, 50))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(245, 10, int((self.health/2500)*300), 50))
    def move(self):
        if self.moving == False and self.movetimer == 0:
            self.newcenter.x = random.randint(0,750)
            self.newcenter.y = random.randint(0,750)
            self.velocity =  self.newcenter - Vector2(self.xPos, self.yPos)
            self.velocity.normalize()
            #self.velocity = self.velocity * self.speed
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

    def update(self, screen):
        self.move()

        self.render(screen)
        self.acid(screen)
        self.curse(screen)
class Acid:
    def __init__(self, angle, direction, xPos, yPos, playerpos):
        self.imagepuddle = pygame.image.load("images/acidpuddle.png")
        self.imagepuddle = pygame.transform.scale(self.imagepuddle, (75,75))
        self.imagethrow = pygame.image.load("images/acidtrail.png")
        self.imagethrow = pygame.transform.scale(self.imagethrow, (60,30))
        self.throw_dmg = 25
        self.puddle_dmg = .5
        self.puddle_rect = self.imagepuddle.get_bounding_rect()
        self.throw_rect = self.imagethrow.get_bounding_rect()
        self.angle = angle
        self.damage = 5
        self.speed = 7
        self.direction = direction
        self.xPos = xPos 
        self.yPos = yPos
        self.throwing = True
        self.lifetime = 500
        self.destroyed = False
        self.playerpos = playerpos
        self.direction = Vector2(self.playerpos) - Vector2([self.xPos, self.yPos])
        self.direction = self.direction.normalize()
    def render(self, screen):
        if self.throwing == True:
            screen.blit(self.imagethrow, [self.xPos, self.yPos])
            self.throw_rect.x = self.xPos
            self.throw_rect.y = self.yPos
            #pygame.draw.rect(screen,(255,0,0),self.throw_rect)
        else:
            screen.blit(self.imagepuddle, [self.xPos, self.yPos])
            self.puddle_rect.x = self.xPos
            self.puddle_rect.y = self.yPos
    def move(self):
        if self.throwing == True:
            """
            if self.xPos > self.playerpos[0]:
                self.xPos -= self.speed
            if self.xPos < self.playerpos[0]:
            if self.xPos > self.playerpos[0]-self.speed and self.xPos< self.playerpos[0]+self.speed:
                if self.yPos > self.playerpos[1] -  self.speed and self.yPos < self.playerpos[1]+self.speed:
                    self.throwing = False
             """
            self.xPos += self.direction[0] * self.speed
            self.yPos += self.direction[1] * self.speed
            if self.direction[0] < 0 and self.direction[1] < 0:
                if self.xPos < self.playerpos[0] and self.yPos < self.playerpos[1]:
                    self.throwing = False
            if self.direction[0] > 0 and self.direction[1] < 0:
                if self.xPos > self.playerpos[0] and self.yPos < self.playerpos[1]:
                    self.throwing = False
            if self.direction[0] > 0 and self.direction[1] > 0:
                if self.xPos > self.playerpos[0] and self.yPos > self.playerpos[1]:
                    self.throwing = False
            if self.direction[0] < 0 and self.direction[1] > 0:
                if self.xPos < self.playerpos[0] and self.yPos > self.playerpos[1]:
                    self.throwing = False
    def attack(self):
        if self.throwing == True:
            if pygame.Rect(GameLogic.playerPos,[50,55]).colliderect(self.throw_rect):
                print("hit player")
                Player.health -= self.throw_dmg
                Player.poison_dmg = 0.5
                Player.poison_cooldown = 240
                GameLogic.playSoundBoss("acid")
                self.destroyed = True
        else:
            if pygame.Rect(GameLogic.playerPos, [50, 50]).colliderect(self.puddle_rect):
                Player.health  -=  self.puddle_dmg     
            
    def update(self, screen):
        self.move()
        self.render(screen)
        self.attack()
        if self.lifetime > 0:
            self.lifetime -= 1
        elif self.lifetime <= 0:
            self.destroyed = True