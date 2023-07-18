import pygame
from gamelogic import GameLogic
import math
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
        self.image = pygame.image.load("images/topdownrifle.png")
        self.image = pygame.transform.scale(self.image, (5*2,55*2))
        self.rect = self.image.get_rect()

        self.name = "Rifle"
        self.bulletcount = 5

    def render(self, screen):
        mpos = pygame.mouse.get_pos()
        x_dist = mpos[0] - self.xpos
        y_dist = -(mpos[1] - self.ypos)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        self.image_rot = pygame.transform.rotate(self.image, angle-90)
        self.rect = self.image_rot.get_rect(center = (self.xpos, self.ypos))
        screen.blit(self.image_rot,(self.xpos, self.ypos))

    def update(self, screen, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen)

class Swordweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/sword.png")
        self.name = "Sword"

    def render(self, screen):
        screen.blit(self.image,(self.xpos, self.ypos))

    def update(self, screen, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen)

class Bombweapon:
    def __init__(self, xpos, ypos, cooldown, damage):
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.damage = damage
        self.image = pygame.image.load("images/bomb.png")
        self.name = "Bomb"

    def render(self, screen):
        screen.blit(self.image,(self.xpos, self.ypos))

    def update(self, screen, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.render(screen)





            

