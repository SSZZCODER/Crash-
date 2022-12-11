import pygame
from player import Player

def menu():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    menu_image = pygame.image.load('images/menu_background.png')
    menu_image = pygame.transform.scale(menu_image, (750,750))

    font = pygame.font.Font('font/Elfboyclassic.ttf', 125)
    font2 = pygame.font.Font('font/zorque.ttf', 125)
    title = font2.render("You Died :(", True, (255, 60, 56))
    again = font2.render("Again?", True, (255, 60, 56))

    clock = pygame.time.Clock()

    exit = False
    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                pos = pygame.mouse.get_pos()
                if pygame.Rect((130, 210, 500, 100)).collidepoint(pos):
                    Player.reset_player()
                    return 1
            if event.type == pygame.QUIT:
                return -1

        screen.fill((255, 140, 66))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(115, 135  , 530, 130))
        pygame.draw.rect(screen, (101, 184, 145), pygame.Rect(130, 150, 500, 100))
       # pygame.draw.rect(screen, (0,0,0), pygame.Rect(115, 15, 530, 130))
       # pygame.draw.rect(screen, (101, 184, 145), pygame.Rect(130, 30, 500, 100))
        screen.blit(title, (70, 5))
        screen.blit(again, (180, 145))
        pygame.display.flip()
        clock.tick(60)

