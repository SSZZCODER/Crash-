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
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))

    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    warp2 = Warp(715,650, 35,100, (128, 0, 128), -50,0)
    oceanpart = ParticleSystem(725,700,(128, 0, 128))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "ocean"
    if len(GameLogic.objects[GameLogic.current_chunk])==0:
    #    GameLogic.objects[GameLogic.current_chunk] = []
        coralspawner.spawncoral()


    clock = pygame.time.Clock()
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if  warp2.Touched() == True:
                Player.MoveBy(warp2.offset_x, warp2.offset_y)
                GameLogic.spellList = []
                return 2
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            
        screen.blit(background,[0,0])
        warp2.Update(screen)
        oceanpart.Update(screen)
        GameLogic.Update(screen)
        if Player.Update(screen) == True:
            return 3
        Spell.render(screen)
        spawner3.spawn_fish()
        StaminaBar.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        pygame.display.update()
        clock.tick(60)

    

