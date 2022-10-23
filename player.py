import pygame
import math
from inventory import Inventory
from enemy import zombie
from hotbar import Hotbar
class Player:

    attack_cooldown = 30
    speed = 3
    health = 100
    hunger = 100 
    player_x = 250
    player_y = 250

    
    playerimage = pygame.image.load('images/New Piskel (28).png')
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    imageload = playerimage
    playercenter = [50, 50]
    playerInventory = Inventory()
    inventoryShow = False
    playerhotbar = Hotbar()



    def attack():
        zombie.getdamage(Player.player_x, Player.player_y)
        Player.health -= 5

    def Update():
        Player.Rotate()
        Player.Move()
        Player.Check()
        if Player.attack_cooldown >= 0:
                        Player.attack_cooldown -= 1
    def Check():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Player.inventoryShow = not Player.inventoryShow

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Player.attack_cooldown < 0:
                        Player.attack()
                        Player.attack_cooldown = 30

                 

                
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

       if Player.player_x > 425:
                Player.player_x = 425
       if Player.player_x < -275:
                Player.player_x = -275
       if Player.player_y < -275:
               Player.player_y = -275
       if Player.player_y > 425:
                Player.player_y = 425
    
    
    playercenter = [player_x +50, player_y +50]

    def Rotate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - Player.playercenter[0], mouse_y - Player.playercenter[1]
        angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
        Player.imageload = pygame.transform.rotate(Player.playerimage, angle-90)
        #Player.player_x, Player.player_y = Player.imageload.get_rect(center = Player.playercenter).topleft
    
    def Render(screen):
        screen.blit(Player.imageload,(Player.player_x + Player.imageload.get_rect(center = Player.playercenter).topleft[0], Player.player_y + Player.imageload.get_rect(center = Player.playercenter).topleft[1])) 
        if Player.inventoryShow:
            Player.playerInventory.Draw(screen)
        Player.playerhotbar.Render(screen)
        
