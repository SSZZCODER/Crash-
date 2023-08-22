from turtle import Screen, speed
import pygame
import random
from gamelogic import GameLogic
from pygame.math import Vector2
from player import Player
import math
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
        elif self.moving == True:
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

class Boss2:
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
        self.fireballtimer = 100
        self.skull = pygame.image.load('images/skull.png')
        self.skull = pygame.transform.scale(self.skull,(70, 80))
        self.image = pygame.image.load('images/magmaboss (1).png')
        self.image = pygame.transform.scale(self.image,(175, 200))
        self.aura_image = pygame.image.load("images/fireaura.png")
        self.aura_image = pygame.transform.scale(self.aura_image, (300, 290))
        self.aura_rect = self.aura_image.get_bounding_rect()
        self.fireballs = []
    def fire_curse(self, screen):
        if self.aura_rect.colliderect(pygame.Rect(GameLogic.playerPos, [50, 55])):
            Player.health -= .25 
            GameLogic.playSoundBoss("curse")
            screen.blit(self.skull, (GameLogic.playerPos[0], GameLogic.playerPos[1]-50))
    def fireball(self, screen):
        if self.fireballtimer <= 0:
            self.fireballs.append(Fireball(0,0,self.xPos, self.yPos, GameLogic.playerPos))
            self.fireballtimer = 100
        elif self.fireballtimer > 0:
            self.fireballtimer -= 1
        if len(self.fireballs) > 0:
            for fireball in self.fireballs:
                fireball.update(screen)
                if fireball.destroyed == True:
                    self.fireballs.remove(fireball)
        print(len(self.fireballs))
    def attack(self):
        return [0, 0]
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
        screen.blit(self.aura_image, self.aura_image.get_rect(center = (self.xPos, self.yPos)))
        self.aura_rect.center = (self.xPos, self.yPos)        
    def update(self, screen):
        self.move()            
        self.render(screen)
        self.fireball(screen)
        self.fire_curse(screen)
class Fireball:
    def __init__(self, angle, direction, xPos, yPos, playerpos):
        self.imagethrow = pygame.image.load("images/fireball.png")
        self.imagethrow = pygame.transform.scale(self.imagethrow, (60,30))
        self.throw_dmg = 25
        self.throw_rect = self.imagethrow.get_bounding_rect()
        self.angle = angle
        self.damage = 5
        self.speed = 7
        self.direction = direction
        self.xPos = xPos 
        self.yPos = yPos
        self.throwing = True
        self.destroyed = False
        self.playerpos = playerpos
        self.direction = Vector2(self.playerpos) - Vector2([self.xPos, self.yPos])
        self.direction = self.direction.normalize()
        self.rel_x = 0
        self.true_ypos = yPos
    def render(self, screen):
        if self.throwing == True:
            screen.blit(self.imagethrow, [self.xPos, self.yPos])
            self.throw_rect.x = self.xPos
            self.throw_rect.y = self.yPos 
    def move(self):
        if self.throwing == True:
            self.xPos += self.direction[0] * self.speed
            self.true_ypos += self.direction[1] * self.speed
            self.yPos = self.true_ypos+(50*math.sin((self.rel_x)*math.pi+10))
        if self.xPos > 750 or self.xPos < 0:
            self.destroyed = True
        if self.yPos > 750 or self.yPos < 0:
            self.destroyed = True
        self.rel_x += 0.1
    def attack(self):
        if self.throwing == True:
            if pygame.Rect(GameLogic.playerPos,[50,55]).colliderect(self.throw_rect):
                print("hit player")
                Player.health -= self.throw_dmg
                self.destroyed = True
    def update(self, screen):
        self.move()
        self.render(screen)
        self.attack()
                
class Boss3:
        def __init__(self, damage, xPos, yPos):
            self.health = 2500
            self.damage = damage
            self.xPos = xPos
            self.yPos = yPos
            self.movetimer = 0
            self.moving = True
            self.newcenter = Vector2(random.randint(0,750),random.randint(0,750))
            self.velocity = Vector2(0)
            self.speed = 3
            self.imageright = pygame.image.load('images/sharkboss.png')
            self.imageright = pygame.transform.scale(self.imageright,(175, 200))
            self.imageleft = pygame.transform.flip(self.imageright, True, False)
            self.imageleft = pygame.transform.scale(self.imageleft,(175, 200))
            self.topimage = pygame.image.load('images/topdownviewsharkboss.png')
            self.topimage = pygame.transform.scale(self.topimage,(175, 200))
            self.toprightimage = pygame.transform.rotate(self.topimage, -45)
            self.toprightimage = pygame.transform.scale(self.toprightimage,(200, 225))
            self.topleftimage = pygame.transform.rotate(self.topimage, 45)
            self.topleftimage = pygame.transform.scale(self.topleftimage,(200,225))           
            self.bottomimage = pygame.transform.flip(self.topimage,False, True)
            self.bottomimage = pygame.transform.scale(self.bottomimage,(175, 200))
            self.bottomrightimage = pygame.transform.rotate(self.topimage, -135)
            self.bottomrightimage = pygame.transform.scale(self.bottomrightimage, (200,225))
            self.bottomleftimage = pygame.transform.rotate(self.topimage, 135)
            self.bottomleftimage = pygame.transform.scale(self.bottomleftimage, (200,225))
            self.image = self.imageright
            self.lungespeed = 5
            self.lunging = False
            self.trackplayertime = 150
            self.lungevelocity = Vector2(0)
            self.lungedistance = -1
            self.startlungepos = Vector2(0)
            self.teethtimer = 100
            self.tooths = []
        def move(self):
            if self.xPos > self.newcenter.x and self.yPos == self.newcenter.y:
                self.image = self.imageleft
            if self.xPos < self.newcenter.x and self.yPos == self.newcenter.y:
                self.image = self.imageright
            if self.xPos > self.newcenter.x and self.yPos < self.newcenter.y:
                self.image = self.bottomleftimage
            if self.xPos < self.newcenter.x and self.yPos > self.newcenter.y:
                self.image = self.toprightimage
            if self.xPos > self.newcenter.x and self.yPos > self.newcenter.y:
                self.image = self.topleftimage
            if self.xPos < self.newcenter.x and self.yPos < self.newcenter.y:
                self.image = self.bottomrightimage
            if self.xPos == self.newcenter.x and self.yPos > self.newcenter.y:
                self.image = self.topimage
            if self.xPos == self.newcenter.x and self.yPos < self.newcenter.y:
                self.image = self.bottomimage
            if self.xPos > self.newcenter.x:
                self.xPos -= 1
            if self.yPos > self.newcenter.y:
                self.yPos -= 1
            if self.xPos < self.newcenter.x:
                self.xPos += 1
            if self.yPos < self.newcenter.y:
                self.yPos += 1
        
            if self.xPos == self.newcenter.x and self.yPos == self.newcenter.y:
                self.newcenter = Vector2(random.randint(0,750),random.randint(0,750))
                self.moving = False
                self.lunging = True
        def lunge(self):
            if self.trackplayertime > 0:
                self.lungevelocity =  GameLogic.playerPos - Vector2(self.xPos, self.yPos)
                self.lungevelocity = self.lungevelocity.normalize()
                self.lungevelocity = self.lungevelocity * self.lungespeed
                self.lungedistance = Vector2(self.xPos, self.yPos).distance_to(GameLogic.playerPos)
                self.startlungepos = Vector2(self.xPos, self.yPos)
                x_dist = GameLogic.playerPos[0]-self.xPos
                y_dist = GameLogic.playerPos[1]-self.yPos
                angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
                self.bleed_dmg = random.choice([4, 5])
                self.bleed_duration = random.choice([120, 240])
                lunge_image = pygame.image.load("images/lungeshark.png")
                lunge_image = pygame.transform.scale(lunge_image,(175, 200))
                image_rot = pygame.transform.rotate(lunge_image, angle-180)
                self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
                self.image = image_rot
                '''
                if self.lungevelocity[0] > 0 and self.lungevelocity[1] == 0:
                    self.image = self.imageright
                if self.lungevelocity[0] < 0 and self.lungevelocity[1] == 0:
                    self.image = self.imageleft
                if self.lungevelocity[0] == 0 and self.lungevelocity[1] >0:
                    self.image = self.bottomimage
                if self.lungevelocity[0] == 0 and self.lungevelocity[1] <0:
                    self.image = self.topimage
                if self.lungevelocity[0] > 0 and self.lungevelocity[1] < 0:
                    self.image = self.toprightimage             
                if self.lungevelocity[0] < 0 and self.lungevelocity[1] < 0:
                    self.image = self.topleftimage      
                if self.lungevelocity[0] < 0 and self.lungevelocity[1] > 0:
                    self.image = self.bottomleftimage      
                if self.lungevelocity[0] > 0 and self.lungevelocity[1] > 0:
                    self.image = self.bottomrightimage      
                '''
                self.trackplayertime -= 1
            if self.trackplayertime <= 0 and self.startlungepos.distance_to(Vector2(self.xPos, self.yPos))<self.lungedistance:
                self.xPos += self.lungevelocity[0]
                self.yPos += self.lungevelocity[1]
                distance = Vector2(self.xPos, self.yPos).distance_to(GameLogic.playerPos)
            if self.trackplayertime <= 0 and self.startlungepos.distance_to(Vector2(self.xPos, self.yPos))>self.lungedistance:
                self.xPos = int(self.xPos)
                self.yPos = int(self.yPos)
                self.trackplayertime = 150
                self.lunging = False
                self.moving = True
         
        def takeDamage(self, damage):
            self.health -= damage
            GameLogic.playSoundBoss("bossdmg")
            if self.health <= 0:
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
        def teeth(self, screen):
            if self.teethtimer <= 0:
                self.tooths.append(Tooth(0,0,self.xPos, self.yPos, GameLogic.playerPos))
                self.teethtimer = 100
            elif self.teethtimer > 0:
                self.teethtimer -= 1
            if len(self.tooths) > 0:
                for tooth in self.tooths:
                    tooth.update(screen)
                    if tooth.destroyed == True:
                        self.tooths.remove(tooth)
        def attack(self):
            return [4, 3, 60]
        def render(self, screen):
            screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(245, 10, 300, 50))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(245, 10, int((self.health/2500)*300), 50))
        def update(self, screen):
            if self.moving == True:
                self.move()
                print("moving to " + str(self.newcenter.x) + " , " + str(self.newcenter.y))
                print("currently at " + str(self.xPos) + " , " + str(self.yPos))
            if self.lunging == True:
                self.lunge()
                print("lunging")   
            self.render(screen)
            self.teeth(screen)
            self.attack()
class Tooth:
    def __init__(self, angle, direction, xPos, yPos, playerpos):
        self.image = pygame.image.load("images/sharktooth.png")
        self.image = pygame.transform.scale(self.image, (60,30))
        self.throw_dmg = 25
        self.throw_rect = self.image.get_bounding_rect()
        self.angle = angle
        self.damage = 5
        self.speed = 10
        self.direction = direction
        self.xPos = xPos 
        self.yPos = yPos
        self.throwing = True
        self.destroyed = False
        self.playerpos = playerpos
        self.direction = Vector2(self.playerpos) - Vector2([self.xPos, self.yPos])
        self.direction = self.direction.normalize()
        self.rel_x = 0
        self.true_ypos = yPos
    def render(self, screen):
        if self.throwing == True:
            screen.blit(self.image, [self.xPos, self.yPos])
            self.throw_rect.x = self.xPos
            self.throw_rect.y = self.yPos 
    def move(self):
        if self.throwing == True:
            self.xPos += self.direction[0] * self.speed
            self.true_ypos += self.direction[1] * self.speed
            self.yPos = self.true_ypos+(50*math.sin((self.rel_x)*math.pi+10))
        if self.xPos > 750 or self.xPos < 0:
            self.destroyed = True
        if self.yPos > 750 or self.yPos < 0:
            self.destroyed = True
        self.rel_x += 0.1
    def attack(self):
        if self.throwing == True:
            if pygame.Rect(GameLogic.playerPos,[50,55]).colliderect(self.throw_rect):
                print("hit player")
                Player.health -= self.throw_dmg
                self.destroyed = True
    def update(self, screen):
        self.move()
        self.render(screen)
        self.attack()
                