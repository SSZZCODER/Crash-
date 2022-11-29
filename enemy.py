import pygame
import random 
from gamelogic import GameLogic
class enemy():
    def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.health = health
        self.damage = damage
        self.damage_cooldown = 0
        self.move_cooldown = 0
        self.original_image = self.assignImage()
        self.image = self.original_image

    def assignImage(self):
        pass
    def render(self, screen):   
        screen.blit(self.image, (self.xPos, self.yPos))
    def move(self):
        pass
    def update(self, screen):
        self.move()
        self.render(screen)
    def takeDamage(self):
        pass
    def attack(self):
        pass

class zombie(enemy):
        def __init__(self, xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown):
            super().__init__(xPos, yPos, speed, health, damage, damage_cooldown, move_cooldown)
            self.damage_cooldown = 30
            self.move_cooldown = 30
            self.move_leftright= random.choice([1, 2])
            self.move_updown = random.choice([1, 2])

        def assignImage(self):
            return pygame.transform.scale(pygame.image.load('images/zombie.png'),(200, 200))

        def render(self, screen):
             screen.blit(self.image, (self.xPos, self.yPos)) 

        def move(self):
            if self.move_cooldown != 0:
                 self.move_cooldown -= 1 

            if self.move_cooldown == 0:
               self.move_cooldown = 30
               self.move_leftright= random.choice([1, 2])
               self.move_updown = random.choice([1, 2])
                
            if self.move_leftright == 1:
                    self.xPos -= self.speed
                    if self.xPos < -85:
                            self.move_cooldown = 30
                            self.move_leftright = 2
            if self.move_leftright == 2:
                   self.xPos += self.speed
                   if self.xPos > 621:
                            self.move_cooldown = 30
                            self.move_leftright = 1

            if self.move_updown == 1:
                    self.yPos -= self.speed
                    if self.yPos < 0:
                        self.move_cooldown = 30
                        self.move_updown = 2 

            if self.move_updown == 2:
                    self.yPos += self.speed
                    if self.yPos > 650:
                            self.move_cooldown = 30
                            self.move_updown = 1
class spawner:
    def __init__(self, enemycount):
        self.enemycount = enemycount   
    def spawn(self):
        for i in range(self.enemycount):
            x = random.randint(50, 650)
            y = random.randint(50, 650)
            speed = random.randint(5, 30)
            health =random.randint(100, 150)
            damage = random.randint(5, 7)
            GameLogic.enemyList.append( zombie(x, y, speed, health, damage, 30, 30))