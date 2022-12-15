import pygame
import random 
from gamelogic import GameLogic
import math

class enemy():
    def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.damage_cooldown = 0
        self.move_cooldown = 0
        self.original_image = self.assignImage()
        self.image = self.original_image
        self.range = range
        self.max_health = health
    
    def assignImage(self):
        pass
    def render(self, screen):   
        screen.blit(self.image, (self.xPos, self.yPos))
        
        #pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos,self.yPos-20, int((self.health/100)*57), 10))

    def move(self): 
        player_x, player_y = GameLogic.playerPos
        rel_x, rel_y = player_x - self.xPos, player_y - self.yPos 
        n = rel_x**2 + rel_y**2
        if n>0:
            n = math.sqrt(n)
            rel_x = rel_x/n
            rel_y = rel_y/n
        if n<=self.range:
            self.xPos += rel_x * self.speed
            self.yPos += rel_y * self.speed
            angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
            self.image = pygame.transform.rotate(self.original_image, angle-90)


    def update(self, screen):
        self.move()
        self.render(screen)
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            GameLogic.enemyList[GameLogic.current_chunk].remove(self)

        print("taken damage")
    def attack(self):
        pass

class zombie(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            # self.move_leftright= random.choice([1, 2])
            # self.move_updown = random.choice([1, 2])

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/zombie.png'),(57, 40))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos))
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
class magma(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            # self.move_leftright= random.choice([1, 2])
            # self.move_updown = random.choice([1, 2])

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/New Piskel (34) (1).png'),(57, 40))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
        #def move(self):
            # if self.move_cooldown != 0:
            #      self.move_cooldown -= 1 

            # if self.move_cooldown == 0:
            #    self.move_cooldown = 30
            #    self.move_leftright= random.choice([1, 2])
            #    self.move_updown = random.choice([1, 2])
                
            # if self.move_leftright == 1:
            #         self.xPos -= self.speed
            #         if self.xPos < -85:
            #                 self.move_cooldown = 30
            #                 self.move_leftright = 2
            # if self.move_leftright == 2:
            #        self.xPos += self.speed
            #        if self.xPos > 621:
            #                 self.move_cooldown = 30
            #                 self.move_leftright = 1

            # if self.move_updown == 1:
            #         self.yPos -= self.speed
            #         if self.yPos < 0:
            #             self.move_cooldown = 30
            #             self.move_updown = 2 

            # if self.move_updown == 2:
            #         self.yPos += self.speed
            #         if self.yPos > 650:
            #                 self.move_cooldown = 30
            #                 self.move_updown = 1
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
                health =random.randint(100, 150)
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
                health =random.randint(100, 150)
                damage = random.randint(5, 6)
                GameLogic.enemyList[GameLogic.current_chunk].append( magma(x, y, speed, health, damage, 30, 30, 200))
                self.enemycount += 1
                self.life = self.spawn_cooldown         
