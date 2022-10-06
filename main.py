# Main File
import pygame
from player import Player
import time

pygame.init()
screen = pygame.display.set_mode((750,750))

clock = pygame.time.Clock()
exit = False
while not exit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            exit=True

    
    screen.fill((0,0,0))
    Player.Update()
    Player.Render(screen)

    pygame.display.flip()
    clock.tick(60)