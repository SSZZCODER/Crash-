import pygame
from warp import Warp
from gamelogic import GameLogic
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((750, 750))
    background = pygame.image.load("images/finalbossdoor.png")
    background = pygame.transform.scale(background, [750, 750]) 
    openedbackground = pygame.image.load("images/finalbossdooropen.png")
    openedbackground = pygame.transform.scale(openedbackground, [750, 750]) 
    dooropened = False
    clock = pygame.time.Clock()
    exit = False
     
    while not exit:
        keys = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
        screen.fill((0,0,0))
        if not dooropened:
            screen.blit(background, (0, 0))
        else:
            screen.fill((255,0,0))
            screen.blit(openedbackground, (0, 0))
        Player.Update(screen,events)
        for key in Player.bosskeys:
            if len(Player.bosskeys[key]) > 0:
                screen.blit(Player.bosskeys[key][0], Player.bosskeys[key][1])
                keys += 1
        if keys >= 4:
            dooropened = True
        pygame.display.flip()
        clock.tick(60)