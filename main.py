# Main File
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))

exit = False
while not exit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            exit=True

    