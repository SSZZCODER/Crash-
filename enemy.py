from turtle import Vec2D
import pygame
import random 
from gamelogic import GameLogic
import math
from pygame.math import Vector2
from items import Coin
class enemy():
    def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.damage_cooldown = 0
        self.move_cooldown = 0
        self.movearound = False
        self.movearounddirection = random.randint(-1,1)
        while self.movearounddirection == 0:
            self.movearounddirection = random.randint(-1,1)
        self.original_image = self.assignImage()
        self.image = self.original_image
        self.range = range
        self.max_health = health    
        self.h = self.image.get_rect(center=(self.xPos, self.yPos)).h
        self.w = self.image.get_rect(center=(self.xPos, self.yPos)).w
        self.rect1 = pygame.Rect(int(self.w/2) + self.xPos, self.yPos, 2, int(self.h))
        self.rect2 = pygame.Rect(self.xPos - int(self.w/2), self.yPos, 2, int(self.h) )
        self.rect3 = pygame.Rect( self.xPos, self.yPos + int(self.h/2), int(self.w), 2)
        self.rect4 = pygame.Rect( self.xPos, self.yPos - int(self.h/2), int(self.w), 2)
        self.changeangle = 90
    def assignImage(self):
        pass
    def render(self, screen):   
        screen.blit(self.image, (self.xPos, self.yPos))
        pygame.draw.rect(screen, (0,255,0), self.rect1)
        pygame.draw.rect(screen, (0,255,0), self.rect2)
        pygame.draw.rect(screen, (0,255,0), self.rect3)
        pygame.draw.rect(screen, (0,255,0), self.rect4)
        #pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos,self.yPos-20, int((self.health/100)*57), 10))

    def move(self): 
        self.h=self.image.get_rect(center=(self.xPos, self.yPos)).h
        self.w=self.image.get_rect(center=(self.xPos, self.yPos)).w
        
        self.rect1 = pygame.Rect(int(self.w/2) + self.xPos, self.yPos, 2, int(self.h))
        self.rect1.center = (int(self.w/2) + self.xPos, self.yPos)
        self.rect2 = pygame.Rect(self.xPos - int(self.w/2), self.yPos, 2, int(self.h) )
        self.rect2.center = (self.xPos - int(self.w/2), self.yPos)
        self.rect3 = pygame.Rect( self.xPos, self.yPos + int(self.h/2), int(self.w), 2)
        self.rect3.center = (self.xPos, self.yPos + int(self.h/2))
        self.rect4 = pygame.Rect( self.xPos, self.yPos - int(self.h/2), int(self.w), 2)
        self.rect4.center = (self.xPos, self.yPos - int(self.h/2))
        player_x, player_y = GameLogic.playerPos
        rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
        n = rel_x**2 + rel_y**2

        if n>0:
            n = math.sqrt(n)
            rel_x = rel_x/n
            rel_y = rel_y/n
        if n<=self.range and self.movearound == False:
            self.xPos += rel_x * self.speed
            self.yPos += rel_y * self.speed
            angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
            self.image = pygame.transform.rotate(self.original_image, angle-self.changeangle)
        if self.movearound == True:
            self.xPos += self.movearounddirection*self.speed
        
        hitbox = self.image.get_rect(center = (self.xPos, self.yPos))
        l = 0
        length = len(GameLogic.objects[GameLogic.current_chunk])
        for bush in GameLogic.objects[GameLogic.current_chunk]:
            if bush.rectangle.colliderect((hitbox)):
               self.xPos -=rel_x*self.speed
               self.yPos -=rel_y*self.speed
               self.movearound = True
               break
            else:
                l += 1
        if l >= length:
            self.movearound = False
            """
            self.movearounddirection = random.randint(-1,1)
            while self.movearounddirection == 0:
                self.movearounddirection = random.randint(-1,1)
                """
            
        

    def update(self, screen):
        self.move()
        self.render(screen)
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            

        print("taken damage")
    def attack(self):
        return [0, self.damage]

class zombie(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.poison_dmg = random.choice([4, 5])
            self.poison_duration = random.choice([120, 240])
            self.dropKey = False
            self.itemcount = 10

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/zombie.png'),(57, 40))
    
        def render(self, screen):
             screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 2 , 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
         
        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                GameLogic.playSound("zombiea")
                return [1, self.poison_dmg, self.poison_duration]
            else:
                GameLogic.playSound("zombiea")
                return [0, self.damage]
            
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.dropKey = True
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class magma(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.fire_dmg = random.choice([4, 5])
            self.burn_duration = random.choice([120, 240])
            self.dropKey = False
            self.itemcount = 10

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/New Piskel (34) (1).png'),(57, 40))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))

        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                
                return [2, self.fire_dmg, self.burn_duration]
            else:
                return [0, self.damage]
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.dropKey = True
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class fish(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.bubble_dmg = random.choice([4, 5])
            self.bubble_duration = random.choice([120, 240])
            self.bubbles = []
            self.bubble_speed = 5
            self.bubble_cooldown  = 30
            self.melee_range = 100
            self.itemcount = 10

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/fish.png'),(57, 40))

        def render(self, screen):
            screen.blit(self.image, (self.xPos, self.yPos)) 
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
            pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
            player_x, player_y = GameLogic.playerPos
            rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
            n = rel_x**2 + rel_y**2

            if n>0:
                n = math.sqrt(n)
                rel_x = rel_x/n
                rel_y = rel_y/n
            if n < self.range and n > self.melee_range:
                if self.bubble_cooldown == 0:
                    bubble = Bubble(self.xPos, self.yPos, self.bubble_speed,1, self.bubble_dmg, 30, 200)
                    self.bubbles.append(bubble)
                    GameLogic.enemyList[GameLogic.current_chunk].append(bubble)
                    self.bubble_cooldown = 30
            elif self.bubble_cooldown > 0:
                self.bubble_cooldown -= 1
            print(n)

            """
            if len(self.bubbles) > 0:
                for i in GameLogic.enemyList[GameLogic.current_chunk]:
                    self.bubbles[i].render(screen)
                    self.bubbles[i].shoot()
                    if type(i) == Bubble:
                        i.render(screen)
                        i.shoot()
            """

        def attack(self):
            GameLogic.playSound("fishsplash")
            return[0, self.damage]
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.dropKey = True
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class Bubble:
    def __init__(self, xPos, yPos, speed, health, damage,bubble_cooldown, range):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.bubble_cooldown = bubble_cooldown
        self.range = range
        self.image = pygame.image.load('images/bubble.png')
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 


    def attack(self):
        return[3, self.damage]
        

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
class demon(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.fire_dmg = random.choice([4, 5])
            self.burn_duration = random.choice([120, 240])
            self.dropKey = False
            self.itemcount = 10
            self.trident_dmg = random.choice([4, 5])
            self.trident_duration = random.choice([120, 240])
            self.tridents = []
            self.trident_speed = 8
            self.trident_cooldown  = 30
            self.melee_range = 100
            self.itemcount = 10
        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/demonboy.png'),(70, 90))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
             player_x, player_y = GameLogic.playerPos
             rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
             n = rel_x**2 + rel_y**2
 
             if n>0:
                n = math.sqrt(n)
                rel_x = rel_x/n
                rel_y = rel_y/n
             if n < self.range and n > self.melee_range:
                if self.trident_cooldown == 0:
                    x_dist = GameLogic.playerPos[0]-self.xPos
                    y_dist = GameLogic.playerPos[1]-self.yPos
                    angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
                    t = trident(self.xPos, self.yPos, self.trident_speed,1, self.trident_dmg, 30, 200, angle)
                    self.tridents.append(t)
                    GameLogic.enemyList[GameLogic.current_chunk].append(t)
                    self.trident_cooldown = 30
             elif self.trident_cooldown > 0:
                self.trident_cooldown -= 1
             print(n)
        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                return [2, self.fire_dmg, self.burn_duration]
            else:
                return [0, self.damage]
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.dropKey = True
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class trident:
    def __init__(self, xPos, yPos, speed, health, damage,throw_cooldown, range, angle):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.throw_cooldown = throw_cooldown
        self.range = range
        self.angle = angle
        self.image = pygame.image.load('images/trident (1).png')
        self.rect = self.image.get_rect(center = [self.xPos, self.yPos]) 
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
        image_rot = pygame.transform.rotate(self.image, self.angle-180)
        self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
        self.image = image_rot
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        

    def attack(self):
        return[3, self.damage]
        

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
class jellyfish(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.fire_dmg = random.choice([4, 5])
            self.burn_duration = random.choice([120, 240])
            self.dropKey = False
            self.itemcount = 10

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/jellyfish.png'),(70, 90))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))

        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                return [2, self.fire_dmg, self.burn_duration]
            else:
                return [0, self.damage]
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                self.dropKey = True
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class monkey(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.dropKey = False
            self.itemcount = 10
            self.banana_dmg = random.choice([4, 5])
            self.banana_dmg_duration = random.choice([120, 240])
            self.bananas = []
            self.banana_speed = 8
            self.banana_cooldown  = 60
            self.melee_range = 0
            self.itemcount = 10
        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/monkey.png'),(70, 90))
        
        def move(self):
            pass
        def render(self, screen):
            screen.blit(self.image, (self.xPos, self.yPos)) 
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
            pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
            player_x, player_y = GameLogic.playerPos
            rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
            n = rel_x**2 + rel_y**2

            if n>0:
                n = math.sqrt(n)
                rel_x = rel_x/n
                rel_y = rel_y/n
            if n < self.range and n > self.melee_range:
                if self.banana_cooldown == 0:
                    x_dist = GameLogic.playerPos[0]-self.xPos
                    y_dist = GameLogic.playerPos[1]-self.yPos
                    angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
                    t = Banana(self.xPos, self.yPos, self.banana_speed,1, self.banana_dmg, 30, 200, angle)
                    self.bananas.append(t)
                    GameLogic.enemyList[GameLogic.current_chunk].append(t)
                    self.banana_cooldown = 60
                elif self.banana_cooldown > 0:
                    self.banana_cooldown -= 1
                print(n)
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                GameLogic.junglekillsforkey +=1
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class Banana:
    def __init__(self, xPos, yPos, speed, health, damage,throw_cooldown, range, angle):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.throw_cooldown = throw_cooldown
        self.range = range
        self.angle = angle
        self.image = pygame.transform.scale(pygame.image.load('images/bananabullet.png'),(15, 50))
        self.rect = self.image.get_rect(center = [self.xPos, self.yPos]) 
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
        image_rot = pygame.transform.rotate(self.image, self.angle-180)
        self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
        self.image = image_rot
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        

    def attack(self):
        return[3, self.damage]
        

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
class snowman(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.dropKey = False
            self.itemcount = 10
            self.snowball_dmg = random.choice([4, 5])
            self.snowball_dmg_duration = random.choice([120, 240])
            self.snowballs = []
            self.snowball_speed = 8
            self.snowball_cooldown  = 60
            self.melee_range = 0
            self.itemcount = 10
        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/snowman.png'),(70, 90))
        
        def move(self):
            pass
        def render(self, screen):
            screen.blit(self.image, (self.xPos, self.yPos)) 
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
            pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
            player_x, player_y = GameLogic.playerPos
            rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
            n = rel_x**2 + rel_y**2

            if n>0:
                n = math.sqrt(n)
                rel_x = rel_x/n
                rel_y = rel_y/n
            if n < self.range and n > self.melee_range:
                if self.snowball_cooldown == 0:
                    x_dist = GameLogic.playerPos[0]-self.xPos
                    y_dist = GameLogic.playerPos[1]-self.yPos
                    angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
                    t = snowball(self.xPos, self.yPos, self.snowball_speed,1, self.snowball_dmg, 30, 200, angle)
                    self.snowballs.append(t)
                    GameLogic.enemyList[GameLogic.current_chunk].append(t)
                    self.snowball_cooldown = 60
                elif self.snowball_cooldown > 0:
                    self.snowball_cooldown -= 1
                print(n)
        def takeDamage(self, damage):
            self.health -= damage
            if self.health <= 0:
                GameLogic.snowkillsforkey +=1
                GameLogic.enemyList[GameLogic.current_chunk].remove(self)
            print("taken damage")
class snowball:
    def __init__(self, xPos, yPos, speed, health, damage,throw_cooldown, range, angle):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.throw_cooldown = throw_cooldown
        self.range = range
        self.angle = angle
        self.image = pygame.transform.scale(pygame.image.load('images/snowball.png'),(60, 60))
        self.rect = self.image.get_rect(center = [self.xPos, self.yPos]) 
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
        image_rot = pygame.transform.rotate(self.image, self.angle-180)
        self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
        self.image = image_rot
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        

    def attack(self):
        return[3, self.damage]
        

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
class bigsnowball(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.roll_dmg = random.choice([4, 5])
            self.freeze_duration = random.choice([120, 240])
            self.dropKey = False
            self.itemcount = 10
        def move(self):
            self.xPos += self.speed
        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/bigsnowball.png'),(70, 90))

        def render(self, screen):
            screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))

        def attack(self):
            GameLogic.playSound("freeze")
            self.health = 0
            return [5]
        def takeDamage():
            pass
class marker(enemy):
    def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):  
        super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
    
    def assignImage(self):
        return pygame.transform.scale(pygame.image.load('images/iciclearea.png'),(70, 90))        
    def move(self):
        pass
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
    def attack(self):
        self.image = pygame.image.load("images/iciclepierce.png")
        return[0,25]


class Scorpian(enemy):

    def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
        super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)

        self.damage_cooldown = 30
        self.move_cooldown = 30
    
        self.dropKey = False
        self.poison_dmg = random.choice([4, 5])
        self.poisoned_duration = random.choice([120, 240])
        self.poisondarts = []
        self.poison_speed = 12
        self.poison_cooldown  = 30
        self.poison_range = 50
        self.melee_range = 10
        self.changeangle = 180
        self.itemcount = 10



    def assignImage(self):
        return pygame.transform.scale(pygame.image.load('images/scorpian.png'),(70, 90))

    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
        pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
        player_x, player_y = GameLogic.playerPos
        rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
        n = rel_x**2 + rel_y**2

        if n>0:
            n = math.sqrt(n)
            rel_x = rel_x/n
            rel_y = rel_y/n
        if n < self.range and n > self.melee_range:
            if self.poison_cooldown == 0:
                x_dist = GameLogic.playerPos[0]-self.xPos
                y_dist = GameLogic.playerPos[1]-self.yPos
                angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
                t = Poison_Dart(self.xPos, self.yPos, self.poison_speed, self.poison_dmg, 30, 200, angle)
                #self.bananas.append(t)
                GameLogic.enemyList[GameLogic.current_chunk].append(t)
                self.poison_cooldown = 60
            elif self.poison_cooldown > 0:
                self.poison_cooldown -= 1
            print(n)

    def takeDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.dropKey = True
            GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)
        print("taken damage")

class Poison_Dart:
    def __init__(self, xPos, yPos, speed,damage,throw_cooldown, range, angle):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.damage = damage
        self.health = 1
        self.throw_cooldown = throw_cooldown
        self.range = range
        self.angle = angle
        self.image = pygame.transform.scale(pygame.image.load('images/poisondart.png'),(15, 50))
        self.rect = self.image.get_rect(center = [self.xPos, self.yPos]) 
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
        image_rot = pygame.transform.rotate(self.image, self.angle-180)
        self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
        self.image = image_rot

    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        

    def attack(self):
        self.health = 0
        return[3, self.damage]
      

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)

class Skeleton(enemy):
    def __init__(self, xPos, yPos, speed, health, damage):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.image = pygame.image.load("images/skeletonsideways.png")
        self.direction = Vector2(0)
        self.destroyed = False
    
    def attack(self, player):
        skelrect = self.image.get_bounding_rect(center = [self.xPos, self.yPos])
        if skelrect.collidedict(player.rect):
            player.health -= self.damage

    def render(self, screen, player):
        self.direction = Vector2(player.rect.centerx, player.rect.centery) - Vector2(self.xPos, self.yPos)
        up = Vector2(-1, 0)
        angle = up.angle_to(self.direction)-180
        image_rot = pygame.transform.rotate(self.image, -angle)
        image_rect = image_rot.get_rect(center = [self.xPos, self.yPos])
        screen.blit(image_rot, image_rect)
    
    def move(self):
        direction = self.direction.normalize()
        vel = direction * self.speed
        self.xPos += vel[0]
        self.yPos += vel[1]

    
    def gothit(self, player):
        rect = self.image.get_bounding_rect()
        rect.center = [self.xPos, self.yPos]
        if player.fist_rect.colliderect(rect):
            if player.attacking == True:
                self.destroyed = True


        
        

    def update(self, screen, player):
        self.render(screen, player)
        self.gothit(player)
        self.move()

class Bone:
    def __init__(self, xPos, yPos, speed, health, damage,throw_cooldown, range, angle):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.throw_cooldown = throw_cooldown
        self.range = range
        self.angle = angle
        self.image = pygame.image.load('images/bone.png')
        self.rect = self.image.get_rect(center = [self.xPos, self.yPos]) 
        self.pos = Vector2(self.xPos,self.yPos)
        self.ppos = Vector2(GameLogic.playerPos)
        self.vel = self.ppos - self.pos
        self.vel = self.vel.normalize()
        self.vel*= self.speed
        image_rot = pygame.transform.rotate(self.image, self.angle-180)
        self.rect = image_rot.get_rect(center = [self.xPos, self.yPos]) 
        self.image = image_rot
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos)) 
        

    def attack(self):
        return[3, self.damage]
        

    def shoot(self):
        self.xPos += self.vel[0]
        self.yPos += self.vel[1]

    def takeDamage(self,damage):
        pass
        
    def update(self,screen):
        self.render(screen)
        self.shoot()
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)


class spawner:
    def __init__(self, enemycount, spawn_cooldown, max_enemycount):
        self.enemycount = enemycount
        self.spawn_cooldown = spawn_cooldown
        self.life = self.spawn_cooldown
        self.max_enemycount = max_enemycount

    def spawn(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( zombie(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown        
                
    def spawn_magma(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( magma(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown         
    def spawn_fish(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append(fish(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown         
                
    def spawn_demon(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( demon(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown     

    def spawn_jellyfish(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( jellyfish(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown     
    def spawn_monkey(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                trees = GameLogic.objects["jungle"]
                x = random.choice(trees).xpos
                y = random.choice(trees).ypos
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( monkey(x, y, speed, health, damage, 30, 30, 300))
                self.enemycount += 1
                self.life = self.spawn_cooldown     
    def spawn_snowman(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50, 650)
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( snowman(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown     
    def spawn_snowball(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = 0
                y = random.randint(50, 650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( bigsnowball(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown     

    def spawn_marker(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x = random.randint(50,650)
                y = random.randint(50, 650)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( marker(x, y, 0, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown     
    def spawn_scorpian(self):
        if self.life > 0:
            self.life -= 1
        else:
          if self.enemycount <= self.max_enemycount:
            enemies = random.randint(2,3)
            if self.max_enemycount - self.enemycount < enemies:
                enemies = self.max_enemycount - self.enemycount
            for i in range(enemies):
                x= random.randint(50,650)
                y= random.randint(50,650)
                speed = random.randint(1,2)
                health =random.randint(100, 110)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( Scorpian(x, y, speed, health, damage, 30, 30, 300))
                self.enemycount += 1
                self.life = self.spawn_cooldown     
    def spawn_skeleton(self, enemieslist):
        if self.life > 0:
            self.life -= 1
        else:
            if self.enemycount <= self.max_enemycount:
                enemies = random.randint(2,3)
                if self.max_enemycount - self.enemycount < enemies:
                    enemies = self.max_enemycount - self.enemycount
                for i in range(enemies):
                    x= random.randint(50,650)
                    y= random.randint(50,650)
                    speed = random.randint(1,2)
                    health =random.randint(100, 110)
                    damage = random.randint(5, 6)
                    enemieslist.append( Skeleton(x, y, speed, health, damage))
                    self.enemycount += 1
                    self.life = self.spawn_cooldown
