from re import S
from turtle import Screen, update
import pygame

class Inventory:
    def __init__(self, slots):
        self.items = [None]*slots


    def Draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), (160,286.5, 430,90))
        pygame.draw.rect(screen, (135, 135, 135), (165,290, 420, 82))

    def addItem(self, items, thing):
        for i in range(len(self.items)):
            if items[i] == None:
                items[i] = thing
                return
   
    def removeItem(self, thing):
        for i in range(len(self.items)):
            if self.items[i].name == thing.name:
                item = self.items[i]
                self.items.remove(item)
                return item
