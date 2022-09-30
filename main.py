# Main File
import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((750,750))

exit = False
while not exit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            exit=True

    screen.fill((0,0,0))
    Player.Render(screen)
    Player.Move(event)
   
    pygame.display.flip()