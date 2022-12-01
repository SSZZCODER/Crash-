import pygame
from inventory import Inventory
from player import Player
from hotbar import Hotbar
from enemy import *
from bars import *
from enemy import zombie
import time
from gamelogic import GameLogic
from warp import Warp






def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    lavaImage = pygame.image.load('images/Eqsa5wtXAAEvH01.png')
    lavaImage = pygame.transform.scale(lavaImage, (750,750))
    clock = pygame.time.Clock()
    exit = False
    
    
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))

    enemy_z1 = zombie(250, 250, 1, 100, 5, 30, 30, 200)
    GameLogic.enemyList.append(enemy_z1)

    spawner1 = spawner(0, 600, 11)
    startingwarp = Warp(0,650, 35,100, (5,5,255), 50,0)

    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)


    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))

    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            
            if  startingwarp.Touched() == True:
                Player.MoveBy(startingwarp.offset_x, startingwarp.offset_y)
                return 1
            if event.type == pygame.QUIT:
                return -1

        screen.blit(lavaImage, (0,0))
        startingwarp.Update(screen)
        spawner1.spawn()
        GameLogic.Update(screen)
        Player.Update()
        enemy_z1.update(screen)
        Player.Render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        pygame.display.flip()
        clock.tick(60)
#inventory not showing