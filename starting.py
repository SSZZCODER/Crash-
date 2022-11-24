
from cmath import rect
import pygame
from player import Player
from hotbar import Hotbar
from enemy import *
from bars import *
from enemy import zombie
from warp import Warp
import time
from gamelogic import GameLogic

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/Pixel_art_grass_image (2).png')
    background = pygame.transform.scale(background, (750,750))

    clock = pygame.time.Clock()
    exit = False
    
    enemy_z1 = zombie(250, 250, 2, 100, 5, 30, 30)
    GameLogic.enemyList.append(enemy_z1)

    StaminaBar = staminabar(0, 0, 115, 20)
    lavawarp = Warp(0,400,100,100,(255,5,10))

    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if  lavawarp.Touched() == True:
                return 2
            if event.type == pygame.QUIT:
                return -1
        screen.blit(background, (0,0))
        lavawarp.Update(screen)
        Player.Update()
        enemy_z1.update(screen)
        Player.Render(screen)
        StaminaBar.render(screen)
        pygame.display.flip()
        clock.tick(60)
