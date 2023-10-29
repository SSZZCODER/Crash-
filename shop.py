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
        self.image = pygame.image.load("images/shopnew (1).gif")
        self.image = pygame.transform.scale(self.image, (98 *7.75,73 * 7.75))
        self.rifle = pygame.image.load("images/rifle.png")
        self.rifle = pygame.transform.scale(self.rifle, (90*2,18*2))
        self.riflecost = 5
        self.bomb = pygame.image.load("images/bomb.png")
        self.bomb = pygame.transform.scale(self.bomb, (12*12,12*12))
        self.bombcost = 3
        self.sword = pygame.image.load("images/sword.png")
        self.sword = pygame.transform.scale(self.sword, (17*2 ,64*2))
        self.swordcost = 4
        self.buy1 = pygame.Rect([78,460], [195,65])
        self.buy2 = pygame.Rect([310, 460], [195,65])
        self.buy3 = pygame.Rect([543,460], [195,65])
        self.playercoins = 1000
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))
        screen.blit(self.rifle, (88, 305))
        #pygame.draw.rect(screen, [250,0,0], self.buy1)
        screen.blit(self.bomb, (340, 255))
        #pygame.draw.rect(screen, [250,0,0], self.buy2)
        screen.blit(self.sword, (613,255))
        #pygame.draw.rect(screen, [250,0,0], self.buy3)
    def buy(self, events):
        for i in range(Player.playerInventory.slots):
            if Player.playerInventory.items[i] != None:
                if Player.playerInventory.items[i].name == "Coin":
                    self.playercoins = Player.playerInventory.items[i].amount
                    break

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buy1.collidepoint(event.pos) and self.playercoins >= self.riflecost:
                    print("Bought Rifle")
                    Player.playerInventory.addObject(items.Rifle())
                    self.playercoins -= self.riflecost
                elif self.buy1.collidepoint(event.pos) and self.playercoins< self.riflecost:
                    print("not enough money")

                if self.buy2.collidepoint(event.pos) and self.playercoins >= self.bombcost:
                    print("Bought Bomb")
                
                    Player.playerInventory.addItem(items.Bomb())
                    
                    self.playercoins -= self.bombcost
                elif self.buy2.collidepoint(event.pos) and self.playercoins< self.bombcost:   
                    print("not enough money")

                if self.buy3.collidepoint(event.pos) and self.playercoins >= self.swordcost:
                    print("Bought Sword")
                    Player.playerInventory.addObject(items.Sword())
                    self.playercoins -= self.swordcost
                elif self.buy3.collidepoint(event.pos) and self.playercoins< self.swordcost:
                    print("not enough money")

        for i in range(Player.playerInventory.slots):
            if Player.playerInventory.items[i] != None:
                if Player.playerInventory.items[i].name == "Coin":
                    Player.playerInventory.items[i].amount = self.playercoins
                    break

        

    def update(self, screen, events):
        self.render(screen)
        self.buy(events)

class HalloweenShop:
    def __init__(self, xPos, yPos):
        self.xPos = xPos    
        self.yPos = yPos
        self.image = pygame.image.load("images/halloweenshopui.png")
        self.image = pygame.transform.scale(self.image, (98 *7.75, 73 * 7.75))
        self.launcher = pygame.image.load("images/pumpkinlauncher.png")
        self.launcher = pygame.transform.scale(self.launcher, (32*4.5 ,32*4.5))
        self.launchercost = 6
        self.buy2 = pygame.Rect([310, 460], [195,65])
        self.playercoins = 1000
    def render(self, screen):
        screen.blit(self.image, (self.xPos, self.yPos))

        #pygame.draw.rect(screen, [250,0,0], self.buy1)
        screen.blit(self.launcher, (340, 255))
        #pygame.draw.rect(screen, [250,0,0], self.buy2)

        #pygame.draw.rect(screen, [250,0,0], self.buy3)
    def buy(self, events):
        for i in range(Player.playerInventory.slots):
            if Player.playerInventory.items[i] != None:
                if Player.playerInventory.items[i].name == "Coin":
                    self.playercoins = Player.playerInventory.items[i].amount
                    break

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
            

                if self.buy2.collidepoint(event.pos) and self.playercoins >= self.launchercost:
                    print("Bought Launcher")
                
                    Player.playerInventory.addItem(items.Bomb())
                    
                    self.playercoins -= self.launchercost
                elif self.buy2.collidepoint(event.pos) and self.playercoins< self.launchercost:   
                    print("not enough money")


        for i in range(Player.playerInventory.slots):
            if Player.playerInventory.items[i] != None:
                if Player.playerInventory.items[i].name == "Coin":
                    Player.playerInventory.items[i].amount = self.playercoins
                    break

        

    def update(self, screen, events):
        self.render(screen)
        self.buy(events)


