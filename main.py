# Main File
import pygame
from player import Player
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/Pixel_art_grass_image (2).png')
    background = pygame.transform.scale(background, (750,750))

    clock = pygame.time.Clock()
    exit = False
    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True

        if event.type == pygame.QUIT:
            return -1
        
        screen.blit(background, (0,0))
        Player.Update()
        Player.Render(screen)

        pygame.display.flip()
        clock.tick(60)