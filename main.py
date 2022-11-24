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

    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))

    clock = pygame.time.Clock()
    exit = False
    
    enemy_z1 = zombie(250, 250, 2, 100, 5, 30, 30)
    GameLogic.enemyList.append(enemy_z1)

    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)

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
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        pygame.display.flip()
        clock.tick(60)