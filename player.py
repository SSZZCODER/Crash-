from email.mime import image
from telnetlib import GA
from turtle import title
import pygame
import math
from enemy import enemy
from inventory import Inventory
import random
from gamelogic import GameLogic
from hotbar import Hotbar
from weapons import Bombweapon, Swordweapon, weapon, Rifleweapon, pumpkinlauncher
from particle import *
from items import *
from spells import Fire

class Player:
    pygame.font.init()
    font = pygame.font.Font('font/arial.ttf', 45)  
    title = font.render(str(""), True, (244, 44, 4)) 

    timer = 120
    animations = pygame.image.load("animations/animation1.png"),pygame.image.load("animations/animation2.png"),pygame.image.load("animations/animation3.png"),pygame.image.load("animations/animation4.png"),pygame.image.load("animations/animation5.png"),pygame.image.load("animations/animation6.png"),pygame.image.load("animations/animation7.png"),pygame.image.load("animations/animation8.png"),pygame.image.load("animations/animation9.png"),pygame.image.load("animations/animation10.png")
    rainbowanimation = pygame.image.load("animations2/rainbow1.png"),pygame.image.load("animations2/rainbow2.png"),pygame.image.load("animations2/rainbow3.png"),pygame.image.load("animations2/rainbow4.png"),pygame.image.load("animations2/rainbow5.png"),pygame.image.load("animations2/rainbow6.png"),pygame.image.load("animations2/rainbow7.png"),pygame.image.load("animations2/rainbow8.png"),pygame.image.load("animations2/rainbow9.png"),pygame.image.load("animations2/rainbow10.png")
    direction = [0, 0]
    attacking = True
    animation_counter = 0
    dmg = random.randint(15, 20)
    dmgcounter = 0
    animation_reverse = False
    
    weapon_fist = weapon("Fist", dmg, 7, 40, 120)
    weapon_rifle = Rifleweapon(0, 0, 5, 50)
    weapon_sword = Swordweapon(0,0,2.5, 20)
    weapon_bomb = Bombweapon(0,0,10,100)
    weapon_pumpkinlauncher = pumpkinlauncher(0, 0, 10, 100)
    weapon = weapon_fist
    weapon_name = "Fist"
    attack_cooldown = 30
    dash_speed = 60
    damage_cooldown = 0
    regen_cooldown = 300
    speed = 3
    playsound = False
    health = 250
    newspell = False
    hunger = 100    
    player_x = 340
    player_y = 340
    dash_cooldown = 600
    playerimage = pygame.image.load('images/New Piskel (28).png')
    playerimage = pygame.transform.scale(playerimage,(50, 55))
    skinnew = pygame.image.load('images/holdingweapon.png')
    
    playercenter = [300, 300]
    playerInventory = Inventory(5)
    inventoryShow = False
    #playerhotbar = Hotbar()
    poison_cooldown = 0
    burn_cooldown = 0
    spellreset = 120
    bleed_cooldown = 0
    burn_dmg = 0
    bleed_dmg = 0
    poison_dmg = 0
    weaponcooldown = 30
    freezecooldown = 0
    particlesp = particlePlayer(player_x, player_y, (139, 0, 0))
    #particlesbleed = particlePlayer(player_x, player_y, (255, 0, 0))
    t = 180
    bcount = 0
    bosskeys = {
        "zombie":[],
        "magma": [],
        "magma": [],
        "shark": []
    }

    def attack():
        Player.attacking = True   
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

        if Player.bleed_cooldown != 0:
            Player.bleed_cooldown -= 1 
            if Player.bleed_cooldown % 60 == 0:
                Player.health -= Player.bleed_dmg
        else:
            Player.particlesp.showEffect = False
        if Player.freezecooldown != 0:
            Player.freezecooldown -= 1
            Player.speed = 0
        if Player.freezecooldown <= 0:
            Player.speed = 3
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
                     
                        Player.damage_cooldown = 60
                    if eattack[0] == 1:
                        Player.poison_dmg = eattack[1]
                        Player.poison_cooldown = eattack[2]
                    if eattack[0] == 2:
                        Player.burn_dmg = eattack[1]
                        Player.particlesp.showEffect = True
                        Player.burn_cooldown = eattack[2]
                    if eattack[0] == 3:
                        Player.health -= eattack[1]
                        e.health = 0
                        Player.damage_cooldown = 60
                    if eattack[0] == 4:
                        Player.bleed_dmg = eattack[1]
                        Player.particlesp.showEffect = True
                        Player.bleed_cooldown = eattack[2]
                    if eattack[0] == 5:
                        Player.freezecooldown = 60
    def itemCheck():
        for items in GameLogic.itemlist[GameLogic.current_chunk]:
            if items.image.get_rect(center = (items.xPos, items.yPos)).colliderect(Player.imageload.get_rect(center = Player.playercenter)):

                    print("Picked up item")
                    items.spawner.itemcount -= 1
                    GameLogic.itemlist[GameLogic.current_chunk].remove(items)
                    if items.name == "Coin":
                        amount = Player.playerInventory.addItem(items)
                        Player.title = Player.font.render(str(amount), True, (244, 44, 4))
                        Player.timer = 120 
                        print("picked up c")    
                        GameLogic.playSound("coin")
                    if items.name == "Bandages":
                    
                        if Player.health < 250:
                            Player.t = 180
                            Player.bcount +=1
                        else:
                            amount = Player.playerInventory.addItem(items)
                            Player.title = Player.font.render(str(amount), True, (244, 44, 4))
                            Player.timer = 120                         

                    

                    
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
            Player.dmgcounter = 0
            return True
        else:
            return False
    def reset_player():
        Player.health = 250
        Player.dash_cooldown = 600
        Player.playerInventory.clearInventory()
        Player.weapon_name = "Fist"
        Player.weapon = Player.weapon_fist

        Player.player_x = 340
        Player.player_y = 340

        Player.title = Player.font.render(str(""), True, (244, 44, 4))
    
        playerimage = pygame.image.load('images/New Piskel (28).png')
        playerimage = pygame.transform.scale(playerimage,(50, 55))
        Player.playerimage = playerimage
    def dash():
        if Player.dash_cooldown != 0:
            Player.dash_cooldown -= 1
        if pygame.key.get_pressed()[pygame.K_SPACE] and Player.dash_cooldown <= 0:
                    Player.player_x += Player.direction[0]*Player.dash_speed
                    Player.player_y += Player.direction[1]*Player.dash_speed
                    Player.dash_cooldown = 600
    def changeimage(newimage):
        Player.playerimage = pygame.transform.scale(pygame.image.load(newimage), (50, 55))
        Player.imageload = Player.playerimage
        if newimage == 'images/New_Piskel-3 (1).png':
            print("changed")
            Player.animations = Player.rainbowanimation


    def Update(screen):
        Player.Rotate()
        Player.Move()
        Player.Check()
        Player.dash()
        Player.damage_check()
        Player.particlesp.Update(screen)
        if Player.weapon_name == "Fist":
            Player.weapon = Player.weapon_fist
            Player.weapon.update(screen)
            playerimage = pygame.image.load('images/New Piskel (28).png')
            Player.playerimage = pygame.transform.scale(playerimage,(50, 55))
 
        elif Player.weapon_name == "Rifle":
            Player.weapon = Player.weapon_rifle
            Player.weapon.update(screen, Player.playercenter[0] , Player.playercenter[1],Player.playercenter)   
            Player.playerimage = Player.skinnew 
            if Player.weapon.reloading == True:
                    if Player.weapon.reloadtimer >= Player.weapon.reloadcooldown:
                        Player.weapon.bulletcount = Player.weapon.bulletcapacity
                        Player.weapon.reloading = False
                        Player.weapon.reloadtimer = 0
                    else:
                        Player.weapon.reloadtimer += 1
            
        elif Player.weapon_name == "Sword":
            Player.weapon = Player.weapon_sword
            Player.weapon.update(screen, Player.playercenter[0] , Player.playercenter[1],Player.playercenter)       
            Player.playerimage = Player.skinnew

        elif Player.weapon_name == "Bomb":
            Player.weapon = Player.weapon_bomb
            amount = 0
            for item in Player.playerInventory.items:
                if item != None:
                    if item.name == "Bomb":
                        amount = item.amount
            if amount <= 0:
                Player.weapon.name = "Fist"
                Player.weapon = Player.weapon_fist
                #Player.playerInventory.removeItemAll(Player.weapon_bomb)
            else:
                Player.weapon.update(screen, Player.playercenter[0] , Player.playercenter[1],Player.playercenter)
                Player.playerimage = Player.skinnew
                if Player.weapon.throwtimer < Player.weapon.throwcooldown:
                    Player.weapon.throwtimer += 1   
        if len(GameLogic.bomblist) > 0:
            for bomb in GameLogic.bomblist:
                bomb.update(screen)
                if bomb.destroyed == True:
                    GameLogic.bomblist.remove(bomb)
        elif Player.weapon_name == "Pumpkin_Launcher":
            Player.weapon = Player.weapon_pumpkinlauncher
            amount = 0
            for item in Player.playerInventory.items:
                if item != None:
                    if item.name == "Pumpkin_Launcher":
                        amount = item.amount
            if amount <= 0:
                Player.weapon.name = "Fist"
                Player.weapon = Player.weapon_fist
                #Player.playerInventory.removeItemAll(Player.weapon_bomb)
            else:
                Player.weapon.update(screen, Player.playercenter[0] , Player.playercenter[1],Player.playercenter)
                Player.playerimage = Player.skinnew
                if Player.weapon.throwtimer < Player.weapon.throwcooldown:
                    Player.weapon.throwtimer += 1   
        if len(GameLogic.pumpkinlist) > 0:
            for pumpkin in GameLogic.pumpkinlist:
                pumpkin.update(screen)
                if pumpkin.destroyed == True:
                    GameLogic.pumpkinlist.remove(pumpkin)
        Player.Render(screen)
        Player.spellangle()
        Player.itemCheck()
        if Player.weaponcooldown != 0:
                Player.weaponcooldown -= 1
        if pygame.mouse.get_pressed()[0]:
            if Player.weapon_name == "Fist":
                if Player.weaponcooldown <= 0:
                    Player.attack()
                    if Player.weapon.attack() == True:
                        Player.dmgcounter += Player.weapon.damage
                        if Player.dmgcounter >= 300:
                            if Player.playsound == False:
                                Player.playsound = True
                                GameLogic.playSound("achievement")
                            Player.dmgcounter = 300
                    Player.weaponcooldown = 30
            elif Player.weapon_name == "Rifle":
                if Player.weapon.reloading == False:               
                    if Player.weapon.shoottimer >= Player.weapon.shootcooldown:
                        Player.weapon.attack(screen, GameLogic.playerPos)
                        Player.weapon.shoottimer = 0
                        Player.weapon.bulletcount -=1
                    else: 
                        Player.weapon.shoottimer += 1
                    if Player.weapon.bulletcount <=0:
                        Player.weapon.reloading = True
                        GameLogic.playSound("reload")
                
                    
                
            elif Player.weapon_name == "Sword":
                Player.weapon.attacking = True

            elif Player.weapon_name == "Bomb":
                #Player.weapon.thrown = True
                amount = 0
                for item in Player.playerInventory.items:
                    if item != None:
                        if item.name == "Bomb":
                            amount = item.amount
                if amount <= 0:
                    Player.weapon_name = "Fist"
                    Player.weapon = Player.weapon_fist
                    #Player.playerInventory.removeItemAll(Player.weapon_bomb)
                else:
                    if Player.weapon.throwtimer >= Player.weapon.throwcooldown:
                        GameLogic.bomblist.append(Player.weapon.attack(screen,GameLogic.playerPos))
                        for item in Player.playerInventory.items:
                            if item != None:
                                if item.name == "Bomb":
                                    item.amount -= 1
                        Player.weapon.throwtimer = 0
            elif Player.weapon_name == "Pumpkin_Launcher":
                #GameLogic.playSound("pumpkinlauncher")
                #Player.weapon.thrown = True
                amount = 0
                for item in Player.playerInventory.items:
                    if item != None:
                        if item.name == "Pumpkin_Launcher":
                            amount = item.amount
                if amount <= 0:
                    Player.weapon_name = "Fist"
                    Player.weapon = Player.weapon_fist
                    #Player.playerInventory.removeItemAll(Player.weapon_bomb)
                else:
                    if Player.weapon.throwtimer >= Player.weapon.throwcooldown:
                        GameLogic.pumpkinlist.append(Player.weapon.attack(screen,GameLogic.playerPos))
                        for item in Player.playerInventory.items:
                            if item != None:
                                if item.name == "Pumpkin_Launcher":
                                    item.amount -= 1
                        Player.weapon.throwtimer = 0
        for i in range(len(Player.playerInventory.items)):
            item = Player.playerInventory.items[i]
            if item != None:
                if item.amount == 0:
                    Player.playerInventory.items[i] = None
                    break

        if Player.attacking == True:
            if Player.weapon_name == "Fist":
                if Player.animation_reverse == True:
                    Player.animation_counter -= 1
                elif Player.animation_reverse == False:
                    Player.animation_counter +=1
                    if Player.animation_counter >= len(Player.animations)-1:
                        Player.animation_reverse = True
                if Player.animation_counter < 0:
                    Player.attacking = False
                    Player.animation_reverse = False
                    Player.animation_counter = 0
            elif Player.weapon_name == "Rifle":
               pass
            elif Player.weapon_name == "Sword":
                pass            
            elif Player.weapon_name == "Bomb":
                pass      
        if Player.timer>0:
            Player.timer-=1
        else:
            Player.title = Player.font.render(str(""), True, (244, 44, 4))
        if Player.t>0:
            Player.t-=1
        elif Player.bcount > 0:
            if Player.health + 10 < 250:
                Player.health += 10
                GameLogic.playSound("heal")

            else:
                Player.health = 250
                GameLogic.playSound("heal")
            
            Player.bcount -=  1
            Player.t = 180
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

       Player.player_x += Player.direction[0] * Player.speed * GameLogic.playerspeedmulti
       Player.player_y += Player.direction[1] * Player.speed * GameLogic.playerspeedmulti
       hitbox = pygame.Rect(Player.player_x,Player.player_y, 50,55)
       for bush in GameLogic.objects[GameLogic.current_chunk]:
           if bush.rectangle.colliderect((hitbox)):
               Player.player_x -= Player.direction[0] * Player.speed * GameLogic.playerspeedmulti
               Player.player_y -= Player.direction[1] * Player.speed * GameLogic.playerspeedmulti
               break
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
    def spellangle():
        if Player.spellreset != 0 and Player.dmgcounter >= 300 and Player.newspell == True:
            
            Player.spellreset -= 1
        elif Player.spellreset <= 0 and Player.dmgcounter >= 300:
            Player.newspell = False
            Player.dmgcounter = 0
            Player.spellreset = 120
        if Player.dmgcounter >= 300:
            if pygame.key.get_pressed()[pygame.K_e]:
                if Player.spellreset >= 0:
                    Player.newspell = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    rel_x, rel_y = mouse_x - Player.playercenter[0], mouse_y - Player.playercenter[1]
                    angle = math.atan2(rel_x,rel_y) *(180/math.pi)
                    distance = math.sqrt(rel_x**2+rel_y**2)
                    if distance > 0:
                        rel_x /= distance
                        rel_y /= distance

                    GameLogic.spellList.append(Fire(angle - 90, 55, [rel_x, rel_y],Player.playercenter[0], Player.playercenter[1]))
    def Rotate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - Player.playercenter[0], mouse_y - Player.playercenter[1]
        angle = math.atan2(rel_x, rel_y)   * (180/math.pi) 
        if Player.attacking == False:
            Player.imageload = pygame.transform.rotate(Player.playerimage, angle-90)
        else:
            Player.imageload = pygame.transform.rotate(pygame.transform.scale(Player.animations[Player.animation_counter], (50+Player.animation_counter*2,55) ), angle-90)
    
    def showingInventory(screen):
        Player.playerInventory.Draw(screen)
        clickedpos = [0,0]
        clicked = False

        if pygame.mouse.get_pressed()[0]:
            clicked = True
        if clicked == True:
            clickedpos = pygame.mouse.get_pos()
            for item in Player.playerInventory.items:
                if item != None:
                    if item.inventoryrect.collidepoint(clickedpos):
                        print("clicked on " + item.name)
                        if item.name == "Rifle":
                            Player.weapon_name = "Rifle"    
                            Player.weapon = Player.weapon_rifle
                        elif item.name == "Sword":
                            Player.weapon_name = "Sword"
                            Player.weapon = Player.weapon_sword
                        elif item.name == "Bomb":
                            Player.weapon_name = "Bomb"
                            Player.weapon = Player.weapon_bomb
                        elif item.name == "Pumpkin_Launcher":
                            Player.weapon_name = "Pumpkin_Launcher"
                            Player.weapon = Player.weapon_pumpkinlauncher
                        clicked = False
                        break



    def Render(screen):
        screen.blit(Player.imageload,Player.imageload.get_rect(center = Player.playercenter)) 

        if Player.inventoryShow:
            Player.showingInventory(screen)
        #Player.playerhotbar.Render(screen)
        screen.blit(Player.title, (250,250))
        
        if Player.weapon_name == "Rifle": 
            if Player.weapon.reloading == False: 
                #bulletcount = Player.font.render(str(Player.weapon.bulletcount), True, (255,0,0))    
                #screen.blit(bulletcount, (350,600))
                for i in range(Player.weapon.bulletcount):
                    x = 21
                    screen.blit(Player.weapon.bulletimage, [0+x*i, 675])                
            elif Player.weapon.reloading == True:

                if Player.weapon.reloadcount < Player.weapon.bulletcapacity:
                    if Player.weapon.reloadtimer %(Player.weapon.reloadcooldown/Player.weapon.bulletcapacity)==0:
                        Player.weapon.reloadcount += 1
                    else:
                        pass
                screen.blit(Player.weapon.bulletimage, [0*21*Player.weapon.reloadcount, 675])
                        
                

        
