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
        self.bulletcapacity = 10
        self.bulletcount = self.bulletcapacity
        self.bullets = []
        self.bulletspeed = 10
        self.shoottimer = 0
        self.shootcooldown = 35
        self.reloading = False
        self.reloadtimer = 0 
        self.reloadcooldown = 150



    def render(self, screen,playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        print(angle)
       
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


    def update(self, screen, xpos, ypos,playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen,playercenter)
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.update(screen)

class Bullet:
    def __init__(self, speed, direction, xpos, ypos):
        self.speed = speed
        self.direction = direction
        self.velocity = self.direction.scale_to_length(self.speed)
        self.xpos = xpos
        self.ypos = ypos
    
    def move(self):
        self.xpos += self.direction[0]
        self.ypos += self.direction[1]

    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), [self.xpos, self.ypos], 5)


    def update(self, screen):
        self.move()
        self.render(screen)
        
class Swordweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/newswordv4.png")
        self.image = pygame.transform.scale(self.image, (18, 165))
        self.rect = self.image.get_rect()
        self.name = "Sword"

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

    def update(self, screen, xpos, ypos, playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen, playercenter)

class Bombweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/newbombv6.png")
        self.image = pygame.transform.scale(self.image, (12*4, 37.5*4))
        self.rect = self.image.get_rect()
        self.name = "Bomb"

    def render(self, screen, playercenter):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - playercenter[0]
        y_dist = mpos[1] - playercenter[1]
        angle = math.atan2(x_dist, y_dist)   * (180/math.pi)
        pcenter = [playercenter[0],playercenter[1]]
        self.image_rot = pygame.transform.rotate(self.image, angle)
        self.rect = self.image_rot.get_rect(center = pcenter)
        screen.blit(self.image_rot,self.image_rot.get_rect(center = pcenter))


    def update(self, screen, xpos, ypos, playercenter):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen, playercenter)





            

