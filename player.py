import pygame

class Player:
    health = 100
    hunger = 100 

    playerimage = pygame.image.load('images/New Piskel (5).png')
    playerimage = pygame.transform.scale(playerimage,(200,200))
    def Render(screen):
        screen.blit(Player.playerimage,(275,275))