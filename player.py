import pygame
import math

class Player:

    speed = 3
    health = 100
    hunger = 100 
    player_x = 250
    player_y = 250

    
    playerimage = pygame.image.load('images/New Piskel (24).png')
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    imageload = playerimage
    playercenter = [50, 50]

    def Update():
        Player.Rotate()
        Player.Move()
        


        
    def Move():
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
    
    
    playercenter = [player_x +50, player_y +50]

    def Rotate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - Player.playercenter[0], mouse_y - Player.playercenter[1]
        angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
        Player.imageload = pygame.transform.rotate(Player.playerimage, angle)
        #Player.player_x, Player.player_y = Player.imageload.get_rect(center = Player.playercenter).topleft
        
    def Render(screen):
        screen.blit(Player.imageload,(Player.player_x + Player.imageload.get_rect(center = Player.playercenter).topleft[0], Player.player_y + Player.imageload.get_rect(center = Player.playercenter).topleft[1])) 
      