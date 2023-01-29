import pygame
import math
from inventory import Inventory
import random
from gamelogic import GameLogic
from hotbar import Hotbar
from weapons import weapon
from particle import *

class Player:
    direction = [0, 0]
    dmg = random.randint(2,6)
    weapon = weapon("Fist", dmg, 7, 40, 30)
    attack_cooldown = 30
    dash_speed = 60
    damage_cooldown = 0
    regen_cooldown = 300
    speed = 3
    health = 100
    hunger = 100 
    player_x = 340
    player_y = 340
    dash_cooldown = 600
    playerimage = pygame.image.load('images/New Piskel (28).png')
    playerimage = pygame.transform.scale(playerimage,(50, 55))
    imageload = playerimage
    playercenter = [300, 300]
    playerInventory = Inventory(3)
    inventoryShow = False
    playerhotbar = Hotbar()
    poison_cooldown = 0
    burn_cooldown = 0
    burn_dmg = 0
    poison_dmg = 0
    particlesp = particlePlayer(player_x, player_y, (255, 165, 0))
    
    
    def attack():
        pass
    def damage_check():
        if Player.poison_cooldown != 0:
            Player.poison_cooldown -= 1 
            if Player.poison_cooldown % 60 == 0:
                Player.health -= Player.poison_dmg
        
        if Player.burn_cooldown != 0:
            Player.burn_cooldown -= 1 
            if Player.burn_cooldown % 60 == 0:
                Player.health -= Player.burn_dmg
        else:
             Player.particlesp.showEffect = False

        if Player.damage_cooldown != 0:
            Player.damage_cooldown -= 1
        if Player.damage_cooldown <= 0:
            for e in GameLogic.enemyList[GameLogic.current_chunk]:
                pygame.Rect(e.xPos, e.yPos, 30, 30)
                pygame.Rect(Player.player_x, Player.player_y, 70, 70)
                e.image.get_rect().colliderect(Player.imageload.get_rect(center = Player.playercenter))
                e.damage
                
                if  pygame.Rect(e.xPos, e.yPos, 30, 30).colliderect(pygame.Rect(Player.player_x, Player.player_y, 70, 70)):
                #if Player.imageload.get_rect(center = Player.playercenter).colliderect(e.image.get_rect()):
                    eattack = e.attack()
                    if eattack[0] == 0:
                        Player.health  -= eattack[1]
                        print(Player.health)
                        Player.damage_cooldown = 60
                    if eattack[0] == 1:
                        Player.poison_dmg = eattack[1]
                        Player.poison_cooldown = eattack[2]
                    if eattack[0] == 2:
                        Player.burn_dmg = eattack[1]
                        Player.particlesp.showEffect = True
                        Player.burn_cooldown = eattack[2]
                        

    def MoveBy(x, y):
        Player.player_x += x
        Player.player_y += y
        Player.playercenter = [Player.player_x +25, Player.player_y +27]
        GameLogic.playerPos = [Player.player_x, Player.player_y]
    
    def zero():
        if Player.health <= 0:
            GameLogic.clear_enemies() 
            Player.poison_cooldown = 0
            Player.burn_cooldown = 0
            return True
        else:
            return False
    def reset_player():
        Player.health = 100
        Player.dash_cooldown = 600
        

        Player.player_x = 340
        Player.player_y = 340

    def dash():
        if Player.dash_cooldown != 0:
            Player.dash_cooldown -= 1
        if pygame.key.get_pressed()[pygame.K_SPACE] and Player.dash_cooldown <= 0:
                    Player.player_x += Player.direction[0]*Player.dash_speed
                    Player.player_y += Player.direction[1]*Player.dash_speed
                    Player.dash_cooldown = 600
    def changeimage(newimage):
        Player.playerimage = newimage
        Player.playerimage = pygame.transform.scale(newimage, (50, 55))
        Player.imageload = Player.playerimage


    def Update(screen):
        Player.Rotate()
        Player.Move()
        Player.Check()
        Player.dash()
        Player.damage_check()
        Player.particlesp.Update(screen)
        Player.weapon.update(screen)
        Player.Render(screen)

        return Player.zero()
        
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

       if Player.player_x > 695:
                Player.player_x = 695
       if Player.player_x < 0:
                Player.player_x = 0
       if Player.player_y < 0:
               Player.player_y = 0
       if Player.player_y > 695:
                Player.player_y = 695
    
    
       Player.playercenter = [Player.player_x +25, Player.player_y +27]
       
       GameLogic.playerPos = [Player.player_x, Player.player_y]

    def Rotate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - Player.playercenter[0], mouse_y - Player.playercenter[1]
        angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
        Player.imageload = pygame.transform.rotate(Player.playerimage, angle-90)
    
    def Render(screen):
        screen.blit(Player.imageload,Player.imageload.get_rect(center = Player.playercenter)) 
        if Player.inventoryShow:
            Player.playerInventory.Draw(screen)
        Player.playerhotbar.Render(screen)
        
        
