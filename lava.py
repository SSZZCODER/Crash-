import pygame
from inventory import Inventory
from particle import ParticleSystem
from player import Player
from hotbar import Hotbar
from enemy import *
from bars import *
from enemy import zombie
import time
from gamelogic import GameLogic
from warp import Warp
from items import spawneritems
from magmarock import *
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    lavaImage = pygame.image.load('images/Eqsa5wtXAAEvH01.png')
    lavaImage = pygame.transform.scale(lavaImage, (750,750))
    clock = pygame.time.Clock()
    exit = False
    portal = pygame.image.load('images/bossportal2.png')
    portal = pygame.transform.scale(portal, (150,200))
    
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    magmakey = pygame.image.load('images/magmakey.png')
    magmakey_rect = magmakey.get_bounding_rect()
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    
    #enemy_z1 = zombie(250, 250, 1, 100, 5, 30, 30, 200)
    #GameLogic.enemyList.append(enemy_z1)
    magmarocks = random.randint(4,9)
    spawner5 = spawneritems(0,300,20)
    spawner6 = spawneritems(0,300,1)
    spawner2 = spawner(0, 600, 11)
    spawner7 = spawner(0, 600, 11)
    startingwarp = Warp(0,650, 35,100, (5,5,255), 50,0)
    oceanwarp = Warp(715,650, 35,100, (0, 128, 0), -50 , 0)
    bossportal2 = Warp(625, 35,100,175,(0,0,0), 50,0)

    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)

    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "lava"
    magmaspawner = objectspawner(magmarocks)
    particlelava = ParticleSystem(10,700,(5,5,250))
    particleocean = ParticleSystem(725, 700, (0, 128, 0))
    if len(GameLogic.objects[GameLogic.current_chunk])==0:
        GameLogic.objects[GameLogic.current_chunk] = []
        magmaspawner.spawnmagmarock()

    droppedkey = False
    global keypos 
    keypos = [0,0]
    killsforkey = 0
    haskey = False

    while not exit:
        enemylength = len(GameLogic.enemyList[GameLogic.current_chunk])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            
            if  startingwarp.Touched() == True:
                Player.MoveBy(startingwarp.offset_x, startingwarp.offset_y)
                GameLogic.spellList = []
                return 1
            if oceanwarp.Touched() == True:
                Player.MoveBy(oceanwarp.offset_x, oceanwarp.offset_y)
                GameLogic.spellList = []
                return 5
            if bossportal2.Touched() == True and haskey == True:
                Player.MoveBy(bossportal2.offset_x, bossportal2.offset_y)
                GameLogic.spellList = []
                return 7
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
      #  for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
          #  if enemy.dropKey == True and droppedkey == False:
           #     print("drop key")
            #    keypos = [enemy.xPos, enemy.yPos]
          #      droppedkey = True
        screen.blit(lavaImage, (0,0))
        particlelava.Update(screen)
        particleocean.Update(screen)
        startingwarp.Update(screen)
        oceanwarp.Update(screen)
        bossportal2.Update(screen)
        screen.blit(portal, [600, 10])
        if haskey == False and droppedkey == True:
            if pygame.Rect(GameLogic.playerPos, [50, 55]).colliderect(pygame.Rect(keypos, [36, 15])):
                haskey = True
                droppedkey = False

        
        if haskey == True:
            bossportal2 = Warp(625, 35,100,175,(255,0,0), 50,0)

        spawner2.spawn_magma()
        spawner7.spawn_demon()
        spawner5.spawncoin()
        spawner5.spawnbandage()
        GameLogic.Update(screen)
        if Player.Update(screen) == True:
            return 3
        if len(GameLogic.enemyList[GameLogic.current_chunk])<enemylength:
            if killsforkey >= 2 and haskey == False:
                droppedkey = True
                GameLogic.playSound("summon")
                keypos = [375, 375]
            else:
                killsforkey +=1

       # enemy_z1.update(screen)
        Spell.render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        if droppedkey == True:
            screen.blit(magmakey, keypos)
            magmakey_rect.center = keypos
        pygame.display.flip()
        clock.tick(60)
        print(enemylength)


