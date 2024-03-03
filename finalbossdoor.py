import pygame
from warp import Warp
from gamelogic import GameLogic
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((750, 750))
    background = pygame.image.load("images/finalbossdoor.png")
    background = pygame.transform.scale(background, [750, 750]) 

    clock = pygame.time.Clock()
    exit = False
     
    while not exit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
    
        screen.blit(background, (0, 0))
        Player.Update(screen)
        pygame.display.flip()
        clock.tick(60)