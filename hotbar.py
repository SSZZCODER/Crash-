from cmath import rect
from sys import _xoptions
from turtle import position
import pygame

class Hotbar:

    def __init__(self):
        self.rect = pygame.Rect(324, 671.5, 110,72.5)
        self.rectcolor = (135,135,135)
        self.item = None
        self.stack = 0

    def Rectangle(self, screen):   
        pygame.draw.rect(screen, (0,0,0), (320, 668.5, 118.75,79.5))
        pygame.draw.rect(screen,self.rectcolor, self.rect)
    def Hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rectcolor = (89, 89, 89)
        else:
            self.rectcolor = (135,135,135) 
    def setItem(self, prop, amount):
        self.item = prop
        self.stack = amount

    def popItem(self):
        amount = self.stack
        self.stack = 0
        prop = self.item
        self.item = None
        return prop, amount


class Item:
    def __init__(self, amount, xPos, yPos, name):
        self.amount = amount
        self.xPos = xPos
        self.yPos = yPos
        self.image = self.assignImage()
        self.name = name
       

    def assignImage(self):
        pass
    def Render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))

class Club(Item):
    def __init__(self, amount, xPos, yPos):
        Item.__init__(self, amount, xPos, yPos, "Club")

    def assignImage(self):
        return pygame.image.load('images/New Piskel (29).png')

class Bandages(Item):
    def __init__(self, amount, xPos, yPos):
        Item.__init__(self, amount, xPos, yPos, "Bandages")

    def assignImage(self):
        return pygame.image.load('images/New Piskel (30).png')



def Render(self,screen):
        self.Hover()
        self.Rectangle(screen)