import pygame
import math
from inventory import Inventory
from enemy import zombie
from hotbar import Hotbar
class Player:

    direction = [0, 0]
    attack_cooldown = 30
    dash_speed = 60
    speed = 3
    health = 100
    hunger = 100 
    player_x = 250
    player_y = 250
    dash_cooldown = 1200
    playerimage = pygame.image.load('images/New Piskel (28).png')
    playerimage = pygame.transform.scale(playerimage,(200, 200))
    imageload = playerimage
    playercenter = [50, 50]
    playerInventory = Inventory()
    inventoryShow = False
    playerhotbar = Hotbar()
    
    def dash():
        if Player.dash_cooldown != 0:
            Player.dash_cooldown -= 1
        if pygame.key.get_pressed()[pygame.K_SPACE] and Player.dash_cooldown <= 0:
                    Player.player_x += Player.direction[0]*Player.dash_speed
                    Player.player_y += Player.direction[1]*Player.dash_speed
                    print("dashing")
                    Player.dash_cooldown = 1200

    def Update():
        Player.Rotate()
        Player.Move()
        Player.Check()
        Player.dash()

    def Check():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Player.inventoryShow = not Player.inventoryShow
    
    def Move():
       Player.direction = [0, 0]
       if pygame.key.get_pressed()[pygame.K_s]:
           Player.direction[1] = 1
           
       if pygame.key.get_pressed()[pygame.K_w]:
            Player.direction[1] = -1

       if pygame.key.get_pressed()[pygame.K_a]:
            Player.direction[0] = -1

       if pygame.key.get_pressed()[pygame.K_d]:
            Player.direction[0] = 1
        
       #normalize the direction
       c = Player.direction[0]*Player.direction[0] + Player.direction[1]*Player.direction[1]
       if c>0:
            c = math.sqrt(c)
            Player.direction = [Player.direction[0]/c, Player.direction[1]/c]

       Player.player_x += Player.direction[0] * Player.speed
       Player.player_y += Player.direction[1] * Player.speed

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
        
