import pygame
import math

class Player:

    speed = 2
    health = 100
    hunger = 100 
    player_x = 250
    player_y = 250

    playerimage = pygame.image.load('images/New Piskel (24).png')

    def Move(self):
       direction = [0, 0]
       if pygame.key.get_pressed()[pygame.K_s]:
           direction[1] = 1
          #  Player.player_y += 1
          #  if Player.player_y > 630:
                #Player.player_y = 630

       if pygame.key.get_pressed()[pygame.K_w]:
            direction[1] = -1
            #Player.player_y -= 1
            #if Player.player_y < -81.5:
               # Player.player_y = -81.5
        
       if pygame.key.get_pressed()[pygame.K_a]:
            direction[0] = -1
            #Player.player_x -= 1
            #if Player.player_x < -85:
             #   Player.player_x = -85
       if pygame.key.get_pressed()[pygame.K_d]:
            direction[0] = 1
            #Player.player_x += 1
            #if Player.player_x > 621:
               # Player.player_x = 621
        
       #normalize the direction
       c = direction[0]^2 + direction[1]^2
       if c>0:
            c = math.sqrt(c)
            direction = [direction[0]/c, direction[1]/c]

       Player.player_x += direction[0] * Player.speed
       Player.player_y += direction[1] * Player.speed

       if Player.player_x > 627:
                Player.player_x = 627
       if Player.player_x < -85:
                Player.player_x = -85
       if Player.player_y < -81.5:
               Player.player_y = -81.5
       if Player.player_y > 630:
                Player.player_y = 630
    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    def Render(screen):
        screen.blit(Player.playerimage,(Player.player_x, Player.player_y))

