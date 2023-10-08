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
from tree import *
import random
def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/jungle.png')
    background = pygame.transform.scale(background, (750,750))
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    spawner4 = spawneritems(0,300,20)
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    trees = random.randint(4, 9)
    treespawner = objectspawner(trees)
    spawnmonkey = spawner(0, 600, 11)

    Spell = spell(320, 640, 115, 20)
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    oceanwarp = Warp(0,650, 35,100, (0, 0, 128), 650,0)
    portal = pygame.image.load('images/bossportal4.png')
    portal = pygame.transform.scale(portal, (150,200))
    junglekey = pygame.image.load('images/junglekey.png')
    junglekey = pygame.transform.scale(junglekey, (50,20))
    junglekey_rect = junglekey.get_bounding_rect()
    bossportal4 = Warp(625, 35,100,175,(0,0,0), 50,0)

    oceanpart = ParticleSystem(0,650,(0, 0, 128))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "jungle"
    if len(GameLogic.objects[GameLogic.current_chunk])==0:
        treespawner.spawntree()


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
            if  oceanwarp.Touched() == True:
                Player.MoveBy(oceanwarp.offset_x, oceanwarp.offset_y)
                GameLogic.spellList = []
                return 5
            if bossportal4.Touched() == True and haskey == True:
                Player.MoveBy(bossportal4.offset_x, bossportal4.offset_y)
                GameLogic.spellList = []
                return 10
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            
        screen.blit(background,[0,0])
        if haskey == False and droppedkey == True:
            if pygame.Rect(GameLogic.playerPos, [50, 55]).colliderect(pygame.Rect(keypos, [36, 15])):
                haskey = True
                droppedkey = False
        if haskey == True:
            bossportal4 = Warp(625, 35,100,175,(144, 238, 144), 50,0)
        oceanwarp.Update(screen)
        oceanpart.Update(screen)
        spawnmonkey.spawn_monkey()
        spawner4.spawnbandage()
        spawner4.spawncoin()
        bossportal4.Update(screen)
        screen.blit(portal, [600, 10])
        GameLogic.Update(screen)
        if Player.Update(screen) == True:
            return 3
        Spell.render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        if len(GameLogic.enemyList[GameLogic.current_chunk])<enemylength:
            if killsforkey >= 2 and haskey == False:
                droppedkey = True
                GameLogic.playSound("summon")
                keypos = [375, 375]
            else:
                killsforkey +=1
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        if droppedkey == True:
            screen.blit(junglekey, keypos)
            junglekey_rect.center = keypos
        print(enemylength)
        pygame.display.update()
        clock.tick(60)

    

