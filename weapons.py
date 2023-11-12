import pygame
from gamelogic import GameLogic
import math
from pygame.math import Vector2
from enemy import *

class weapon():
    def __init__(self, name, damage, range, hitbox_size, cooldown):
        self.name = name
        self.damage = damage
        self.range = range
        self.hitbox_size = hitbox_size
        self.cooldown = cooldown
        self.timer = self.cooldown

    def attack(self):
        player_x, player_y = GameLogic.playerPos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y
        n = rel_x**2 + rel_y**2
        if n>0:
            n = math.sqrt(n)
            if n > self.range:
                rel_x = rel_x/n
                rel_y = rel_y/n
                rel_x *= self.range
                rel_y *= self.range
        rel_x,rel_y = player_x+rel_x,player_y+rel_y
        hitbox = pygame.Rect(rel_x - self.hitbox_size//2, rel_y -self.hitbox_size//2, self.hitbox_size, self.hitbox_size)
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if hitbox.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos))):
                enemy.takeDamage(self.damage)
                return True
        return False

    def update(self, screen):
        pass

    def render():
        pass

class Rifleweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/New Piskel (23).png")
        self.image = pygame.transform.scale(self.image, (6*2,125*2))
        #self.image = pygame.transform.flip(self.image,False,True)
        self.rect = self.image.get_rect()

        self.name = "Rifle"
        self.bulletcapacity = 5
        self.bulletcount = self.bulletcapacity
        self.bullets = []
        self.bulletspeed = 20
        self.shoottimer = 0
        self.shootcooldown = 25
        self.reloading = False
        self.reloadtimer = 0 
        self.reloadcooldown = 80
        self.bulletimage = pygame.image.load("images/bulletimage.png")
        self.reloadcount = 0
        


    def render(self, screen,playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        screen.blit(self.image_rot,self.image_rot.get_rect(center = pcenter))

    def attack(self, screen, playercenter):
        mpos = pygame.mouse.get_pos() 
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        attackvector = Vector2(x_dist, y_dist).normalize()
        bulletpos = [self.rect.x, self.rect.y + self.rect.w]
        if angle < -90 and angle > -180:
            bulletpos = [self.rect.x, self.rect.y]
        if angle > 90 and angle < 180:
            bulletpos = [self.rect.x + self.rect.w, self.rect.y]
        if angle < 0 and angle > -90:
            bulletpos = [self.rect.x, self.rect.y + self.rect.h]
        if angle > 0 and angle < 90:
            bulletpos = [self.rect.x + self.rect.w, self.rect.y + self.rect.h]
        self.bullets.append(Bullet(self.bulletspeed, attackvector, bulletpos[0], bulletpos[1]))
        GameLogic.playSound("rifle")


    def update(self, screen, xpos, ypos,playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen,playercenter)
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.update(screen)
                if bullet.destroyed == True:
                    self.bullets.remove(bullet)

class Bullet:
    def __init__(self, speed, direction, xpos, ypos):
        self.speed = speed
        self.direction = direction
        self.velocity = self.direction.scale_to_length(self.speed)
        self.xpos = xpos
        self.ypos = ypos
        self.damage = 75
        self.rect = pygame.Rect(0,0,32,32)
        self.destroyed = False
    
    def move(self):
        self.xpos += self.direction[0]
        self.ypos += self.direction[1]
    
    def hit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.rect.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                enemy.takeDamage(self.damage)
                self.destroyed = True

    def render(self, screen):
        self.rect.center = (self.xpos, self.ypos)
        pygame.draw.circle(screen, (0,0,0), [self.xpos, self.ypos], 5)


    def update(self, screen):
        self.move()
        self.render(screen)
        self.hit()
        
class Swordweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image_idle = pygame.image.load("images/newswordv4.png")
        self.image_attack = pygame.image.load("swordanimation/sword-2.png (1) (4).png")
        self.image = self.image_idle
        #self.image = pygame.transform.scale(self.image, (18, 165))
        self.rect = self.image.get_rect()
        self.name = "Sword"
        self.swingtimer = 0
        self.swingcooldown = 25
        self.attacktimer = 0
        self.attackcooldown = 10
        self.attacking = False

    def render(self, screen, playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]        
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        screen.blit(self.image_rot,self.image_rot.get_rect(center = pcenter))

        #screen.blit(self.image,(self.xpos, self.ypos))
    def attack(self, screen, playercenter):
        if self.attacktimer < self.attackcooldown:
            mpos = pygame.mouse.get_pos() 
            x_dist = mpos[0] - playercenter[0]
            y_dist = mpos[1] - playercenter[1]
            angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
            if angle < -90 and angle > -180:
                swordpos = [self.rect.x, self.rect.y]
            if angle > 90 and angle < 180:
                swordpos = [self.rect.x + self.rect.w/2, self.rect.y]
            if angle < 0 and angle > -90:
                swordpos = [self.rect.x, self.rect.y + self.rect.h/2]
            if angle > 0 and angle < 90:
                swordpos = [self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2]
            hitbox = pygame.Rect(swordpos, [64,64])
            self.image = self.image_attack
            GameLogic.playSound("sword")
            self.attacktimer += 1
            #pygame.draw.rect(screen, (255,0,0), hitbox)
            for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
                if (hitbox.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                    GameLogic.playSound("swordhit")
                    enemy.takeDamage(self.damage)
                    self.attacktimer = 0
                    self.image = self.image_idle
                    self.attacking = False
                    break
            
        else:
            self.attacktimer = 0
            self.image = self.image_idle
            self.attacking = False
    


    def update(self, screen, xpos, ypos, playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen, playercenter)
        if self.attacking:
            self.attack(screen, playercenter)

class Bombweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/newbombv6.png")
        self.image = pygame.transform.scale(self.image, (12*4, 37.5*4.5))
        self.rect = self.image.get_rect()
        self.name = "Bomb"
        self.thrown = False
        self.speed = 3
        self.bombs = []
        self.throwtimer = 0
        self.throwcooldown = 50
        

    def hold_render(self, screen, playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        screen.blit(self.image_rot,self.image_rot.get_rect(center = pcenter))
        #pygame.draw.rect(screen, (255,0,0), self.rect)

    def attack(self, screen, playercenter):
        mpos = pygame.mouse.get_pos() 
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        attackvector = Vector2(x_dist, y_dist).normalize()  
        if angle < -90 and angle > -180:
            bombpos = [self.rect.x, self.rect.y]
        if angle > 90 and angle < 180:
            bombpos = [self.rect.x + self.rect.w, self.rect.y]
        if angle < 0 and angle > -90:
            bombpos = [self.rect.x, self.rect.y + self.rect.h]
        if angle > 0 and angle < 90:
            bombpos = [self.rect.x + self.rect.w, self.rect.y + self.rect.h]
        #pygame.draw.rect(screen, (255,0,0), self.rect)
        #bombpos = self.rect.center
        return Bomb(self.speed, attackvector, bombpos[0], bombpos[1])


    def render(self, screen, playercenter):
        #if not self.thrown:
        self.hold_render(screen, playercenter)



    def update(self, screen, xpos, ypos, playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen, playercenter)
        #if len(self.bombs) > 0:
         #   for bomb in self.bombs:
          #      bomb.update(screen)
           #     if bomb.destroyed == True:
            #        self.bombs.remove(bomb)
  




class Bomb:
    def __init__(self, speed, direction, xpos, ypos):
        self.speed = speed
        self.direction = direction
        self.velocity = self.direction.scale_to_length(self.speed)
        self.xpos = xpos
        self.ypos = ypos
        self.damage = 25
        self.image = pygame.image.load("images/newbombv5 (1).png")
        self.image = pygame.transform.scale(self.image, (24*2, 24*2))
        self.explosion = pygame.image.load("images/explosion.png")
        self.explosion = pygame.transform.scale(self.explosion, (32*3.5,32*3.5))
        self.rect = pygame.Rect(0,0,32,32)
        self.explodedrect = self.explosion.get_bounding_rect()
        self.destroyed = False
        self.range = 200
        self.disappear = 60
        self.explosiondmg = 5
        


    def move(self):
        self.xpos += self.direction[0]
        self.ypos += self.direction[1]
    
    def hit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.rect.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                self.exploded()
                return True
                break
        return False

    def explosionhit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.explodedrect.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                GameLogic.playSound("explosion")
                enemy.takeDamage(self.explosiondmg)


    def render(self, screen):
        self.rect.center = (self.xpos, self.ypos)
        self.explodedrect.center = (self.xpos, self.ypos)
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen, (255,0,0), self.rect)

    def exploded(self):
        self.image = self.explosion
        self.direction = [0,0]
        if self.disappear>0:
            self.disappear -=1
        
        if self.disappear <= 0:
            self.destroyed = True

    def update(self, screen):
        self.move()
        self.render(screen)
        self.hit()
        if self.hit() == False:
            if self.range <=0:
                self.exploded()
        if self.range >0:
            self.range -= 1
        self.explosionhit()

            
class pumpkinlauncher:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/pumplauncher.png")
        self.image = pygame.transform.scale(self.image, (12*4, 37.5*4))
        #self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.name = "Pumpkin_Launcher"
        self.thrown = False
        self.speed = 3
        self.pumpkins = []
        self.throwtimer = 0
        self.throwcooldown = 50
        

    def hold_render(self, screen, playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        screen.blit(self.image_rot,self.image_rot.get_rect(center = pcenter))
        #pygame.draw.rect(screen, (255,0,0), self.rect)

    def attack(self, screen, playercenter):
        mpos = pygame.mouse.get_pos() 
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        attackvector = Vector2(x_dist, y_dist).normalize()
        if angle < -90 and angle > -180:
            pumpkinpos = [self.rect.x, self.rect.y]
        if angle > 90 and angle < 180:
            pumpkinpos = [self.rect.x + self.rect.w, self.rect.y]
        if angle < 0 and angle > -90:
            pumpkinpos = [self.rect.x, self.rect.y + self.rect.h]
        if angle > 0 and angle < 90:
            pumpkinpos = [self.rect.x + self.rect.w, self.rect.y + self.rect.h]
        #pygame.draw.rect(screen, (255,0,0), self.rect)
        #pumpkinpos = self.rect.center
        GameLogic.playSound("pumpkinlauncher")
        return pumpkin(self.speed, attackvector, pumpkinpos[0], pumpkinpos[1])



    def render(self, screen, playercenter):
        #if not self.thrown:
        self.hold_render(screen, playercenter)



    def update(self, screen, xpos, ypos, playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen, playercenter)
        #if len(self.bombs) > 0:
         #   for bomb in self.bombs:
          #      bomb.update(screen)
           #     if bomb.destroyed == True:
            #        self.bombs.remove(bomb)
  




class pumpkin:
    def __init__(self, speed, direction, xpos, ypos):
        self.speed = speed
        self.direction = direction
        self.velocity = self.direction.scale_to_length(self.speed)
        self.xpos = xpos
        self.ypos = ypos
        self.damage = 25
        self.image = pygame.image.load("images/pumpkinammo.png")
        self.image = pygame.transform.scale(self.image, (24*2, 24*2))
        self.explosion = pygame.image.load("images/squashedpumpkin.png")
        self.explosion = pygame.transform.scale(self.explosion, (32*3.5,32*3.5))
        self.rect = pygame.Rect(0,0,32,32)
        self.explodedrect = self.explosion.get_bounding_rect()
        self.destroyed = False
        self.range = 200
        self.disappear = 60
        self.explosiondmg = 5
        


    def move(self):
        self.xpos += self.direction[0]
        self.ypos += self.direction[1]
    
    def hit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.rect.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                self.exploded()
                return True
                break
        return False

    def explosionhit(self):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            if (self.explodedrect.colliderect(enemy.image.get_rect(center=(enemy.xPos, enemy.yPos)))):
                GameLogic.playSound("splat")
                enemy.takeDamage(self.explosiondmg)


    def render(self, screen):
        self.rect.center = (self.xpos, self.ypos)
        self.explodedrect.center = (self.xpos, self.ypos)
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen, (255,0,0), self.rect)

    def exploded(self):
        self.image = self.explosion
        self.direction = [0,0]
        if self.disappear>0:
            self.disappear -=1
        
        if self.disappear <= 0:
            self.destroyed = True

    def update(self, screen):
        self.move()
        self.render(screen)
        self.hit()
        if self.hit() == False:
            if self.range <=0:
                self.exploded()
        if self.range >0:
            self.range -= 1
        self.explosionhit()

            

            


            

