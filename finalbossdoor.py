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
    finalbosswarp = Warp(250, 600, 100, 100, (255, 255, 0), 25, 25)
    clock = pygame.time.Clock()
    exit = False
     
    while not exit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
            if dooropened:
                if finalbosswarp.Touched() == True:
                    Player.MoveBy(finalbosswarp.offset_x, finalbosswarp.offset_y)
                    print("teleported")
                    return 17
        screen.fill((0,0,0))
        if not dooropened:
            screen.blit(background, (0, 0))
        else:
            screen.fill((255,0,0))
            screen.blit(openedbackground, (0, 0))       
        if dooropened:
            finalbosswarp.Render(screen)
        keys = 0
        for key in Player.bosskeys:
            if len(Player.bosskeys[key]) > 0:
                screen.blit(Player.bosskeys[key][0], Player.bosskeys[key][1])
                keys += 1
        if keys >= 1:
            dooropened = True
        Player.Update(screen,events)
        pygame.display.flip()
        clock.tick(60)