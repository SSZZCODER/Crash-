
from cmath import rect
import pygame
from items import spawneritems
from player import Player
from hotbar import Hotbar
from enemy import *
from bars import *
from enemy import zombie
from spells import Fire
from warp import Warp
import time
from gamelogic import GameLogic
from data import saveData
from boss import Boss
from particle import ParticleSystem, particlePlayer
from bushspawner import *
import random
from shop import Shop
from textbar import *
import pygame.font

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/Pixel_art_grass_image (2).png')
    background = pygame.transform.scale(background, (750,750))
    portal = pygame.image.load('images/transparent portal.png')
    portal = pygame.transform.scale(portal, (150,200))
    key = pygame.image.load('images/key.png')
    key_rect = key.get_bounding_rect()
    shopkeeper = pygame.image.load('images/shopkeeper.png')
    shopkeeper = pygame.transform.scale(shopkeeper, (100,100))
    shopkeeperrect= pygame.Rect([650,0], [100,100])
    droppedkey = False
    global keypos 
    keypos = [0,0]
    killsforkey = 0
    haskey = False

    clock = pygame.time.Clock()
    exit = False
    
    #enemy_z1 = zombie(250, 250, 1, 100, 5, 30, 30, 200)
    #GameLogic.enemyList.append(enemy_z1)
    bushes = random.randint(4, 9)
    spawner3 = spawneritems(0,300,20)
    spawner4 = spawneritems(0,300,1)
    spawner1 = spawner(0, 600, 10)
    textBar = textbar()
    textBaron = True
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    
    lavawarp = Warp(0,650,35,100,(255,5,10), 50,0)
    bossportal = Warp(625,625,100,175,(0,0,0), 50,0)

    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "grass"
    bushspawner = objectspawner(bushes)
    particles = ParticleSystem(10,700, (250,5,5))
    shopui = Shop(0,50)
 
    while not exit:
        enemylength = len(GameLogic.enemyList[GameLogic.current_chunk])
        mousepos = pygame.mouse.get_pos()
     
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:   
                exit=True
            if  lavawarp.Touched() == True:
                Player.MoveBy(lavawarp.offset_x, lavawarp.offset_y)
                GameLogic.spellList = []
                return 2   
            if bossportal.Touched() == True and haskey == True:
                Player.MoveBy(bossportal.offset_x, bossportal.offset_y)
                GameLogic.spellList = []
                return 6
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: 
                    return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textBar.rect.collidepoint(event.pos):
                    textBaron = False
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if enemy.dropKey == True and droppedkey == False:
                print("drop key")
                keypos = [enemy.xPos, enemy.yPos]
                droppedkey = True
        screen.blit(background, (0,0))
        particles.Update(screen)
        lavawarp.Update(screen)
        bossportal.Update(screen)

        screen.blit(portal, [600,600])
        screen.blit(shopkeeper, [650,0])

        spawner3.spawncoin()
        spawner4.spawnbandage()
        spawner1.spawn()
        GameLogic.Update(screen)
        if Player.Update(screen) == True:
            return 3
        if textBaron == True:
            textBar.render(screen)
           
        if len(GameLogic.enemyList[GameLogic.current_chunk])<enemylength:
            if killsforkey >= 2 and haskey == False:
                droppedkey = True
                keypos = [375, 375]
            else:
                killsforkey +=1
        if haskey == False:
            if pygame.Rect(GameLogic.playerPos, [50, 55]).colliderect(pygame.Rect(keypos, [36, 15])):
                haskey = True
                droppedkey = False

        if droppedkey == True:
            screen.blit(key, keypos)
            key_rect.center = keypos
        if haskey == True:
            bossportal = Warp(625,625,100,175,(0, 0, 108), 50,0)

          
            print("picked up key")
        #enemy_z1.update(screen)
        if shopkeeperrect.collidepoint(Player.player_x, Player.player_y):
            shopui.update(screen, events)
        StaminaBar.render(screen)
        Spell.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        saveData.save()
        pygame.display.flip()
        clock.tick(60)

