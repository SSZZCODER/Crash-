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
from coral import *
from warp import *
import random
def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/17.png')
    background = pygame.transform.scale(background, (750,750))
    corals = random.randint(4, 9)
    coralspawner = objectspawner(corals)
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    spawner3 = spawner(0, 600, 11)
    spawner5 = spawner(0, 600, 11)
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    spawner4 = spawneritems(0,300,20)
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    portal = pygame.image.load('images/bossportal3.png')
    portal = pygame.transform.scale(portal, (150,200))
    oceankey = pygame.image.load('images/oceankey.png')
    oceankey_rect = oceankey.get_bounding_rect()
    bossportal3 = Warp(625, 35,100,175,(0,0,0), 50,0)

    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    warp2 = Warp(0,650, 35,100, (128, 0, 128), -50,0)
    oceanpart = ParticleSystem(725,700,(128, 0, 128))
    warp3 = Warp(715,650, 35,100, (0, 100, 0), -50,0)
    junglepart = ParticleSystem(0,650,(0, 100, 0))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "ocean"
    if len(GameLogic.objects[GameLogic.current_chunk])==0:
    #    GameLogic.objects[GameLogic.current_chunk] = []
        coralspawner.spawncoral()


    clock = pygame.time.Clock()
    exit = False

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
            if  warp2.Touched() == True:
                Player.MoveBy(warp2.offset_x, warp2.offset_y)
                GameLogic.spellList = []
                return 2
            if  warp3.Touched() == True:
                Player.MoveBy(warp3.offset_x, warp3.offset_y)
                GameLogic.spellList = []
                return 9
            if bossportal3.Touched() == True and haskey == True:
                Player.MoveBy(bossportal3.offset_x, bossportal3.offset_y)
                GameLogic.spellList = []
                return 8
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            
        screen.blit(background,[0,0])
        warp2.Update(screen)
        warp3.Update(screen)
        junglepart.Update(screen)
        bossportal3.Update(screen)
        screen.blit(portal, [600, 10])
        if haskey == False and droppedkey == True:
            if pygame.Rect(GameLogic.playerPos, [50, 55]).colliderect(pygame.Rect(keypos, [36, 15])):
                haskey = True
                droppedkey = False
        if haskey == True:
            bossportal3 = Warp(625, 35,100,175,(144, 238, 144), 50,0)
        oceanpart.Update(screen)
        GameLogic.Update(screen)
        spawner4.spawnbandage()
        spawner4.spawncoin()
        if Player.Update(screen) == True:
            return 3
        Spell.render(screen)
        spawner3.spawn_fish()
        spawner5.spawn_jellyfish()
        StaminaBar.render(screen)
        HealthBar.render(screen)
        if len(GameLogic.enemyList[GameLogic.current_chunk])<enemylength:
            if killsforkey >= 2 and haskey == False:
                droppedkey = True
                keypos = [375, 375]
            else:
                killsforkey +=1
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        if droppedkey == True:
            screen.blit(oceankey, keypos)
            oceankey_rect.center = keypos
        pygame.display.update()
        clock.tick(60)

    

