import pygame

class Player:
    health = 100
    hunger = 100 
    
    player_x = 275
    player_y = 275

    playerimage = pygame.image.load('images/New Piskel (5).png')
    def Move(self):
       if pygame.key.get_pressed()[pygame.K_LEFT]:
            Player.player_x -= 1
       if pygame.key.get_pressed()[pygame.K_RIGHT]:
            Player.player_x += 1
    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))
