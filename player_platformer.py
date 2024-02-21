import pygame
from pygame.math import Vector2
import math
pygame.mixer.init()

class Player_Platformer:
    def __init__(self, x, y, speed, jumpheight, width, height, fist_width, fist_height, health):
        self.x = x
        self.y = y
        self.speed = speed
        #self.jumpheight = -jumpheight
        self.width = width
        self.height = height
        self.fist_width = fist_width
        self.fist_height = fist_height
        self.vel = Vector2(0)
        self.dx = 0
        self.dy = 0
        self.create_player()
        self.create_playerattack()
        self.health = health
        self.min_jump = -10
        self.max_jump = -jumpheight
        self.ground = pygame.Rect(0,0,0,0)



    def create_player(self):
        self.facing = 1
        self.image = pygame.image.load("images/playerbody_sideways.png") 
        self.image = pygame.transform.scale(self.image,[self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(self.x, self.y)
        self.fist_distance = 50
        self.fist_img = pygame.image.load("images/playerhand_sideways.png")
        self.fist_img = pygame.transform.scale(self.fist_img,[self.fist_width,self.fist_height])
        self.fist_rect = self.fist_img.get_rect()
        self.fist_rect.center = Vector2(self.rect.centerx+self.fist_distance * self.facing, self.rect.centery)
        self.fist_attack_img = pygame.image.load("images/playerhand_sideways_attack.png")
        self.fist_attack_img = pygame.transform.scale(self.fist_attack_img, (self.fist_width, self.fist_height))
        self.fist_attack_right_img = pygame.transform.flip(self.fist_attack_img, 1, 0)
        self.desiredjump = False
        self.ontheground = False

    def create_playerattack(self):
        self.attacking = False
        self.attackcooldown = 2.5
        self.attacktimer = 0
        self.attack_damage = 15
        self.fist_length = 17.5
        self.fist_attack_distance = 0
        self.fist_speed = 8.5
        self.fist_time = self.fist_length/self.fist_speed
        self.fist_timer = 0 
        self.attack_sound = pygame.mixer.Sound("sounds/punch-2-166695.wav")

        
    def move_x(self, keys):
        if keys[pygame.K_d]:
            self.vel[0] = self.speed
            self.facing = 1
        elif keys[pygame.K_a]:
            self.vel[0] = -self.speed
            self.facing = -1
        else:
            self.vel[0] = 0

    def move_y(self, keys, dt):
        gravity = 5
        self.vel[1] += gravity*dt
        jumpvelocity = 0
        if keys[pygame.K_w]:
            if self.ontheground:
                if self.rect.bottom - self.ground.rect.top > self.max_jump:
                    jumpvelocity = -1*math.sqrt(-2*gravity*self.min_jump)
                    self.vel[1] += jumpvelocity
                else:
                    jumpvelocity = 0
                    self.vel[1] += jumpvelocity
    def attack(self, keys, dt):
        if keys[pygame.K_SPACE]:
            if self.attacktimer >= self.attackcooldown:
                self.attack_sound.play()
                self.attacking = True
                self.attacktimer = 0
        if self.attacking:
            if self.fist_timer <= self.fist_time:
                self.fist_attack_distance = self.fist_speed * self.fist_timer * self.facing
                self.fist_timer += dt
            else:
                self.fist_timer = 0
                self.fist_attack_distance = 0
                self.attacking = False
        if self.attacking == False:
            if self.attacktimer < self.attackcooldown:
                self.attacktimer += dt
        self.fist_rect.centerx = self.rect.centerx + self.fist_distance * self.facing + self.fist_attack_distance
                
    def collisions(self, platforms):
        self.dx = self.vel[0]
        self.dy = self.vel[1]
        for platform in platforms:
            if platform.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height)):
                self.dy = platform.rect.top - self.rect.bottom
                if self.dy < 0:
                    self.dy = 0
                self.vel[1] = 0
                self.ontheground = True
                self.ground = platform
        if self.rect.centerx + self.dx >= 750:
            self.rect.right = 750
            self.dx = 0
        elif self.rect.centerx + self.dx<=0:
            self.rect.left = 0
            self.dx = 0
            
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        #self.fist_rect.centerx = self.rect.centerx + self.fist_distance * self.facing
        self.fist_rect.centery = self.rect.centery

    def render(self, screen):
        #pygame.draw.rect(screen, (255, 0, 0), self.rect)
        #pygame.draw.rect(screen, (255, 0, 0), self.fist_rect)
        screen.blit(self.image, self.rect)
        if self.attacking:
            if self.facing == -1:
                screen.blit(self.fist_attack_img, self.fist_rect)
            elif self.facing == 1:
                screen.blit(self.fist_attack_right_img, self.fist_rect)
                
        if self.attacking == False:
            screen.blit(self.fist_img, self.fist_rect)
            #pygame.draw.rect(screen, (255, 0, 0), self.fist_rect)
            pass
    def gothit(self, attackvalue, pushback):
        self.health -= attackvalue
        self.vel[0] += pushback
    def update(self, screen, keys, dt, platforms):
        self.collisions(platforms)
        self.move_x(keys)
        self.move_y(keys, dt)
        self.render(screen)
        self.attack(keys, dt)

