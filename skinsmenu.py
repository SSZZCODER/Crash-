from operator import truediv
import pygame
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    clock = pygame.time.Clock()
    exit = False
    font = pygame.font.Font('font/Elfboyclassic.ttf', 50)
    font2 = pygame.font.Font('font/zorque.ttf', 125)   
    font3 = pygame.font.Font('font/arial.ttf', 35)
    #skin = pygame.image.load("images/New_Piskel-3 (1).png")
    #skin = pygame.transform.scale(skin, (120, 120))  
    skin = "images/New_Piskel-3 (1).png"

    playerimage = pygame.image.load('images/New Piskel (28).png')
    playerimage = pygame.transform.scale(playerimage,(50, 55))
    back = font.render("Back", True, (0,0,0))
    title = font2.render("Skins", True, (0, 0,0))
    equipped = font3.render("Equipped", True, (255,5,5))
    showequipped = False

    while not exit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                pos = pygame.mouse.get_pos()
                if pygame.Rect((0, 150 , 140, 140)).collidepoint(pos):
                    Player.changeimage(skin)
                    showequipped = True
           
              

                if pygame.Rect((10, 685 , 150,50)).collidepoint(pos):
                    return 0    

        screen.fill((128,128,128))
        pygame.draw.rect(screen, (105,105,105), pygame.Rect(0, 150 , 140, 140))
        pygame.draw.rect(screen, (105,105,105), pygame.Rect(10, 685 , 150,50))
        screen.blit(pygame.transform.scale(pygame.image.load(skin), (120, 120)), (10,160))
        screen.blit(back, (35,690))
        screen.blit(title, (225, 5))
        if showequipped == True:
            screen.blit(equipped, (0,185))
        
        pygame.display.flip()
        clock.tick(60)
