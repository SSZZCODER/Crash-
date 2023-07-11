from re import S
from turtle import Screen, update
import pygame
import pygame.font
pygame.font.init


class Inventory:
    def __init__(self, slots):
        self.slots = slots
        self.items = [None]*slots
        self.positions = [(175,295),(315,295),(455,295),(595, 295), (735, 295)]
        self.amount = 0
        self.font = pygame.font.Font(None, 32)
    def Draw(self, screen):

        pygame.draw.rect(screen, (0,0,0), (160,286.5, 430,90))
        pygame.draw.rect(screen, (135, 135, 135),   (165,290, 420, 82))
#        pygame.draw.rect(screen, (0,0,0), (175,295, 125,80))
 #       pygame.draw.rect(screen, (0,0,0), (315,295, 125,80))
  #      pygame.draw.rect(screen, (0,0,0), (455,295, 125,80))
        for i in range(len(self.items)):
            if self.items[i] == None:
                continue
            screen.blit(self.items[i].inventoryimage,self.positions[i])
            itemtext = self.font.render(str(self.items[i].amount), True, (0, 0, 0))
            screen.blit(itemtext, self.positions[i])
    
    def addItem(self, thing):
        for i in range(len(self.items)):
            if self.items[i] == None:
                self.items[i] = thing
                self.amount += 1
                return 1
            if self.items[i].name == thing.name:    
                self.items[i].amount += thing.amount
                return self.items[i].amount
            
    def addObject(self, thing):
        for i in range(len(self.items)):
            if self.items[i]== None:
                self.items[i] = thing
                return 1
            elif self.items[i].name == thing.name:
                print("item already in inventory")
                break
        



    def removeItem(self, thing):
        for i in range(len(self.items)):
            if self.items[i].name == thing.name:
                item = self.items[i]
                self.items.remove(item)
                return item

    def removeItem(self, thing, amount):
        for i in range(len(self.items)):
            if self.items[i].name == thing.name:
                item = self.items[i]
                item.amount -= amount
                self.amount -= 1
                if item.amount <= 0:
                    self.items.remove(item)
                return item
    def clearInventory(self):
        self.items= [None]* self.slots
        self.amount = 0 
            
