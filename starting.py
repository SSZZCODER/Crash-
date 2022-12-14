
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

from particle import ParticleSystem
def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/Pixel_art_grass_image (2).png')
    background = pygame.transform.scale(background, (750,750))

    clock = pygame.time.Clock()
    exit = False
    
    #enemy_z1 = zombie(250, 250, 1, 100, 5, 30, 30, 200)
    #GameLogic.enemyList.append(enemy_z1)

    spawner1 = spawner(0, 600, 10)
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)

    lavawarp = Warp(0,650,35,100,(255,5,10), 50,0)

    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))

    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "grass"

    particles = ParticleSystem(10,700, (250,5,5))

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if  lavawarp.Touched() == True:
                Player.MoveBy(lavawarp.offset_x, lavawarp.offset_y)
                return 2   
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0

        screen.blit(background, (0,0))
        particles.Update(screen)
        lavawarp.Update(screen)
        spawner1.spawn()
        GameLogic.Update(screen)
        if Player.Update(screen) == True:
            return 3
        #enemy_z1.update(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10))
        pygame.display.flip()
        clock.tick(60)

