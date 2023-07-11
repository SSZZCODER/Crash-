from email.mime import image
from sys import _xoptions
import pygame
import inventory
import items
from player import Player
class Shop:
    def __init__(self, xPos, yPos):
        self.xPos = xPos    
        self.yPos = yPos
        self.image = pygame.image.load("images/shop.png")
        self.image = pygame.transform.scale(self.image, (98 *7.75,73 * 7.75))
        self.rifle = pygame.image.load("images/rifle.png")
        self.rifle = pygame.transform.scale(self.rifle, (90*2,18*2))
        self.bomb = pygame.image.load("images/bomb.png")
        self.bomb = pygame.transform.scale(self.bomb, (12*12,12*12))
        self.sword = pygame.image.load("images/sword.png")
        self.sword = pygame.transform.scale(self.sword, (17*2 ,64*2))
        self.buy1 = pygame.Rect([78,460], [195,65])
        self.buy2 = pygame.Rect([310, 460], [195,65])
        self.buy3 = pygame.Rect([543,460], [195,65])
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))
        screen.blit(self.rifle, (88, 305))
        #pygame.draw.rect(screen, [250,0,0], self.buy1)
        screen.blit(self.bomb, (340, 255))
        #pygame.draw.rect(screen, [250,0,0], self.buy2)
        screen.blit(self.sword, (613,255))
        #pygame.draw.rect(screen, [250,0,0], self.buy3)
    def buy(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buy1.collidepoint(event.pos):
                    print("Bought Rifle")
                    Player.playerInventory.addObject(items.Rifle())
                elif self.buy2.collidepoint(event.pos):
                    print("Bought Bomb")
                else: 
                    print("Bought Sword")
        

    def update(self, screen, events):
        self.render(screen)
        self.buy(events)


