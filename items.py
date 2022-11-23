import pygame

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
