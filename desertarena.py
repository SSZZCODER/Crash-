import pygame
from inventory import Inventory
from particle import ParticleSystem
from player import Player
from hotbar import Hotbar

from bars import *
from enemy import *
import time
from gamelogic import GameLogic
from items import spawneritems
from boss import Boss7
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/sandarena.png')
    background = pygame.transform.scale(background, (750,750))
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    slowedimg = pygame.image.load('images/turtle.png')
    slowedimg = pygame.transform.scale(slowedimg, (200, 120))    
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    slowedbar = slowed(30, 60, 115, 20)

    
    spawner3 = spawneritems(0,300,20)
    spawner4 = spawneritems(0,300,1)
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "Boss7"
    GameLogic.enemyList[GameLogic.current_chunk].append(Boss7(7, 350 ,95))


    clock = pygame.time.Clock()
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            
        screen.blit(background,[0,0])
        GameLogic.Update(screen)
        spawner3.spawncoin()
        spawner4.spawnbandage()
        if Player.Update(screen) == True:
            return 3
        
        Spell.render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        if Player.freezecooldown != 0:
            slowedbar.render(screen)
            screen.blit(slowedimg, (11, 45))
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10)) 
        pygame.display.update()
        clock.tick(60)

    

