import pygame
from inventory import Inventory
from player import Player
from hotbar import Hotbar
from enemy import zombie
import time


class lavaChunk():

    def lavaLevel():
        pygame.init()
        screen = pygame.display.set_mode((750,750))
        lavaImage = pygame.image.load('images/Eqsa5wtXAAEvH01.png')
        lavaImage = pygame.transform.scale(lavaImage, (750,750))
        clock = pygame.time.Clock()
        exit = False
    
        while not exit:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    exit=True

            if event.type == pygame.QUIT:
                return -1

            screen.blit(lavaImage, (0,0))
            Player.Update()
            zombie.update()
            zombie.Render(screen)
            Player.Render(screen)
            pygame.display.flip()
            clock.tick(60)