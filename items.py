import pygame
from gamelogic import GameLogic

import random

class Item:
    def __init__(self, amount, xPos, yPos, name, spawner):
        self.amount = amount
        self.xPos = xPos
        self.yPos = yPos
        self.image = self.assignImage()
        self.name = name
        self.inventoryimage = self.image
        self.inventoryrect = self.inventoryimage.get_bounding_rect()
        self.spawner = spawner
    def assignImage(self):
        pass
    def Render(self, screen):
        screen.blit(self.image,self.image.get_rect(center = (self.xPos, self.yPos)))

class Coin(Item):
    def __init__(self, amount, xPos, yPos, spawner):
        Item.__init__(self, amount, xPos, yPos, "Coin", spawner)
        self.inventoryimage = pygame.transform.scale(self.image, (50,60))
    def assignImage(self):
        coinimage = pygame.image.load('images/New Piskel (37) (1).png')
        return pygame.transform.scale(coinimage, (25,30))
#    def  Render(self, screen):
 #       screen.blit(self.image, (self.xPos, self.yPos))

class Bandages(Item):
    def __init__(self, amount, xPos, yPos, spawner):
        Item.__init__(self, amount, xPos, yPos, "Bandages", spawner )
        self.inventoryimage = pygame.transform.scale(self.image, (90,60))
    def assignImage(self):
        healimage = pygame.image.load('images/New Piskel (30) (1).png')
        return pygame.transform.scale(healimage, (60,40))        
#    def  Render(self, screen):
 #       screen.blit(self.image, (self.xPos, self.yPos))

class spawneritems:
    def __init__(self, itemcount, spawn_cooldown, maxitemcount):
        self.itemcount = itemcount
        self.spawn_cooldown = spawn_cooldown
        self.life = self.spawn_cooldown
        self.maxitemcount = maxitemcount

    def spawncoin(self):
        
        """
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
                GameLogic.itemlist[GameLogic.current_chunk].append( Coin(1, self.xPos, self.yPos,self))
                self.itemcount += 1
                self.life = self.spawn_cooldown
        """
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
                GameLogic.itemlist[GameLogic.current_chunk].append( Bandages(1,self.xPos, self.yPos, self))
                self.itemcount += 1
                self.life = self.spawn_cooldown

    #def use(self):

class inventoryItem():
    def __init__(self, amount, name, image):
         self.amount = amount
         self.name =  name
         self.image = image

class Rifle():
    def __init__(self):
        self.amount = 1
        self.name = "Rifle"
        self.inventoryimage = pygame.image.load("images/rifle.png")
        self.inventoryrect = self.inventoryimage.get_bounding_rect()

class Sword():
    def __init__(self):
        self.amount = 1
        self.name = "Sword"
        self.inventoryimage = pygame.image.load("images/sword.png")
        self.inventoryrect = self.inventoryimage.get_bounding_rect()
class Bomb():
    def __init__(self):
        self.amount = 1
        self.name = "Bomb"
        self.image = pygame.image.load("images/bomb.png")
        self.inventoryimage = pygame.transform.scale(self.image, (60,70))