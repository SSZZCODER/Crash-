import pygame


class Player:

    
    health = 100
    hunger = 100 
    player_x = 250
    player_y = 250

    playerimage = pygame.image.load('images/New Piskel (24).png')

    def Move(self):
        
       if pygame.key.get_pressed()[pygame.K_s]:
            Player.player_y += 1
            if Player.player_y > 630:
                Player.player_y = 630

       if pygame.key.get_pressed()[pygame.K_w]:
            Player.player_y -= 1
            if Player.player_y < -81.5:
                Player.player_y = -81.5
        
       if pygame.key.get_pressed()[pygame.K_a]:
            Player.player_x -= 1
            if Player.player_x < -85:
                Player.player_x = -85
       if pygame.key.get_pressed()[pygame.K_d]:
            Player.player_x += 1
            if Player.player_x > 627:
                Player.player_x = 627


        

    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))

