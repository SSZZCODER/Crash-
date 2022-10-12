import pygame


def menu():
    pygame.init()
    screen = pygame.display.set_mode((750,750))


    font = pygame.font.Font('font/Pixelboy.ttf', 125)
    title = font.render("Crash!", True, (92, 122, 255))
    start = font.render("Start", True, (92, 122, 255))

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
        screen.fill((13,2,33))
        pygame.draw.rect(screen, (15,8,75), pygame.Rect(130, 210, 500, 100))
        screen.blit(title, (230, 30))
        screen.blit(start, (230, 220))
        pygame.display.flip()
        clock.tick(60)

