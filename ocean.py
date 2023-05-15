import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/17.png')
    background = pygame.transform.scale(background, (750,750))

    clock = pygame.time.Clock()
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
                return -1
        screen.blit(background,[0,0])
        pygame.display.update()
        clock.tick(60)
    

