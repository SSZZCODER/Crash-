# Main File
import pygame
from inventory import Inventory
from player import Player
from hotbar import Hotbar
from enemy import *
from bars import *
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

    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True

        if event.type == pygame.QUIT:
            return -1
    
        screen.blit(background, (0,0))
        Player.Update()
        enemy_z1.update(screen)
        Player.Render(screen)
        StaminaBar.render(screen)
        pygame.display.flip()
        clock.tick(60)