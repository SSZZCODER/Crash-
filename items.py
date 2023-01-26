import pygame
from gamelogic import GameLogic
from player import Player
import random
import starting

class Item:
    def __init__(self, amount, xPos, yPos, name):
        self.amount = amount
        self.xPos = xPos
        self.yPos = yPos
        self.image = self.assignImage()
        self.name = name
        self.list = []
    def assignImage(self):
        pass
    def Render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))

class Coin(Item):
    def __init__(self, amount, xPos, yPos):
        Item.__init__(self, amount, xPos, yPos, "Coin")

    def assignImage(self):
        coinimage = pygame.image.load('images/New Piskel (37) (1).png')
        return pygame.transform.scale(coinimage, (25,30))
    def  Render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))

class Bandages(Item):
    def __init__(self, amount, xPos, yPos):
        Item.__init__(self, amount, xPos, yPos, "Bandages")

    def assignImage(self):
        healimage = pygame.image.load('images/New Piskel (30) (1).png')
        return pygame.transform.scale(healimage, (60,40))        
    def  Render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))

class spawneritems:
    def __init__(self, itemcount, spawn_cooldown, maxitemcount):
        self.itemcount = itemcount
        self.spawn_cooldown = spawn_cooldown
        self.life = self.spawn_cooldown
        self.maxitemcount = maxitemcount

    def spawncoin(self):
        if self.life > 0:
            self.life -= 1
        else:
         if self.itemcount <= self.maxitemcount:
            Items = random.randint(1,3)
            if self.maxitemcount - self.itemcount < Items:
                Items = self.maxitemcount - self.itemcount
            for i in range(Items):
                self.xPos = random.randint(50, 650)
                self.yPos = random.randint(50, 650)
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(20, self.xPos, self.yPos))
                self.itemcount += 1
                self.life = self.spawn_cooldown
                

    def spawnbandage(self):
        if self.life > 0:
            self.life -= 1
        else:
         if self.itemcount <= self.maxitemcount:
            Items = random.randint(0,1)
            if self.maxitemcount - self.itemcount < Items:
                Items = self.maxitemcount - self.itemcount
            for i in range(Items):
                self.xPos = random.randint(50, 650)
                self.yPos = random.randint(50, 650)
                GameLogic.itemlist[GameLogic.current_chunk].append( Bandages(3,self.xPos, self.yPos))
                self.itemcount += 1
                self.life = self.spawn_cooldown

