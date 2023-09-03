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
    background = pygame.image.load('images/jungle.png')
    background = pygame.transform.scale(background, (750,750))
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    spawner4 = spawneritems(0,300,20)
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    oceanwarp = Warp(0,650, 35,100, (0, 0, 128), 650,0)
    
    oceanpart = ParticleSystem(0,650,(0, 0, 128))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "jungle"



    clock = pygame.time.Clock()
    exit = False



    while not exit:
        enemylength = len(GameLogic.enemyList[GameLogic.current_chunk])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if  oceanwarp.Touched() == True:
                Player.MoveBy(oceanwarp.offset_x, oceanwarp.offset_y)
                GameLogic.spellList = []
                return 5
            
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            
        screen.blit(background,[0,0])
        oceanwarp.Update(screen)
        oceanpart.Update(screen)
        GameLogic.Update(screen)
        spawner4.spawnbandage()
        spawner4.spawncoin()
        if Player.Update(screen) == True:
            return 3
        Spell.render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        pygame.display.update()
        clock.tick(60)

    

