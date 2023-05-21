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
            self.image = pygame.transform.rotate(self.original_image, angle-90)
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

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/zombie.png'),(57, 40))
    
        def render(self, screen):
             screen.blit(self.image, self.image.get_rect(center = (self.xPos, self.yPos)))
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 2 , 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
             pygame.draw.rect(screen, (0,255,0), self.rect1)
             pygame.draw.rect(screen, (0,255,0), self.rect2)
             pygame.draw.rect(screen, (0,255,0), self.rect3)
             pygame.draw.rect(screen, (0,255,0), self.rect4)    
        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                GameLogic.playSound("zombie")
                return [1, self.poison_dmg, self.poison_duration]
            else:
                GameLogic.playSound("zombie")
                return [0, self.damage]
class magma(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.fire_dmg = random.choice([4, 5])
            self.burn_duration = random.choice([120, 240])

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

class fish(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown, range)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.bubble_dmg = random.choice([4, 5])
            self.bubble_duration = random.choice([120, 240])
            self.bubbles = {"image":[],"pos": [],"player_pos": []}

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/fish.png'),(57, 40))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 
             pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.xPos+15,self.yPos-20, 40, 10))
             pygame.draw.rect(screen, (250, 28, 0), pygame.Rect(self.xPos+15,self.yPos-20, int((self.health/self.max_health)*40), 10))
             attack_choice = random.randint(1,10)
             if attack_choice == 3:
                self.bubbles["image"].append(pygame.image.load("images/bubble.png"))
                self.bubbles["pos"].append([self.xPos,self.yPos])
                self.bubbles["player_pos"].append(GameLogic.playerPos)
             if len(self.bubbles["image"]) > 0:
                for i in range(len(self.bubbles["image"])):
                    screen.blit(self.bubbles["image"][i],self.bubbles["pos"][i])
                    if self.bubbles["pos"][i][0] > self.bubbles["player_pos"][i][0]:
                        self.bubbles["pos"][i][0] -= 1
                    if self.bubbles["pos"][i][0] < self.bubbles["player_pos"][i][0]:
                        self.bubbles["pos"][i][0] += 1
                    if self.bubbles["pos"][i][1] > self.bubbles["player_pos"][i][1]:
                        self.bubbles["pos"][i][1] -= 1
                    if self.bubbles["pos"][i][1] < self.bubbles["player_pos"][i][1]:
                        self.bubbles["pos"][i][1] += 1
                self.bubbles["pos"][i][0] += (self.bubbles["player_pos"][i][0] - self.bubbles["pos"][i][0])/10
                self.bubbles["pos"][i][1] += (self.bubbles["player_pos"][i][1] - self.bubbles["pos"][i][1])/10
                

        def attack(self):
            attack_choice = random.randint(1,5)
            if attack_choice == 3:
                return[3, self.bubble_dmg, self.bubble_duration]
            else:
                return [0, self.damage]

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
