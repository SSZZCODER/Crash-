import pygame


def menu():
    pygame.init()
    screen = pygame.display.set_mode((750,750))


    font = pygame.font.Font('font/Elfboyclassic.ttf', 125)
    font2 = pygame.font.Font('font/zorque.ttf', 125)
    title = font2.render("Crash!", True, (0, 0,0))
    start = font.render("Play", True, (0, 0, 0))

    clock = pygame.time.Clock()

    exit = False
    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                pos = pygame.mouse.get_pos()
                if pygame.Rect((130, 210, 500, 100)).collidepoint(pos):
                    return 1
            if event.type == pygame.QUIT:
                return -1
        screen.fill((78, 135, 140))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(115, 195  , 530, 130))
        pygame.draw.rect(screen, (101, 184, 145), pygame.Rect(130, 210, 500, 100))
       # pygame.draw.rect(screen, (0,0,0), pygame.Rect(115, 15, 530, 130))
       # pygame.draw.rect(screen, (101, 184, 145), pygame.Rect(130, 30, 500, 100))
        screen.blit(title, (180, 30))
        screen.blit(start, (240, 200))
        pygame.display.flip()
        clock.tick(60)

