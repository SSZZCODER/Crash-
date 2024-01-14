import pygame
from player_platformer import Player_Platformer



def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/pryamid.png')
    background = pygame.transform.scale(background, (750,750))
    player = Player_Platformer(25, 25, 5, 10, 50, 50, 15, 15)


    clock = pygame.time.Clock()
    exit = False

    while not exit:
        dt = clock.get_time()/100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
        keys = pygame.key.get_pressed()
        screen.blit(background,[0,0])
        player.update(screen, keys, dt, None)
        pygame.display.update()
        clock.tick(60)

    

