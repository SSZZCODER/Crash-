import pygame
from pygame.math import Vector2
import math

class Player_Platformer:
    def __init__(self, x, y, speed, jumpheight, width, height, fist_width, fist_height):
        self.x = x
        self.y = y
        self.speed = speed
        self.jumpheight = -jumpheight
        self.width = width
        self.height = height
        self.fist_width = fist_width
        self.fist_height = fist_height
        self.vel = Vector2(0)
        self.dx = 0
        self.dy = 0
        self.create_player()

    def create_player(self):
        self.facing = 1
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = Vector2(self.x, self.y)
        self.fist_distance = 50
        self.fist_rect = pygame.Rect(0, 0, self.fist_width, self.fist_height)
        self.fist_rect.center = Vector2(self.rect.centerx+self.fist_distance * self.facing, self.rect.centery)
        self.desiredjump = False
        self.ontheground = False

        
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
        if keys[pygame.K_w]:
            if self.ontheground:
                jumpvelocity = math.sqrt(-2*gravity*self.jumpheight)
    def collisions(self, platforms):
        self.dx = self.vel[0]
        self.dy = self.vel[1]
        for platform in platforms:
            if platform.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height)):
                self.dy = platform.rect.top - self.rect.bottom
                #self.dy = 0
                self.vel[1] = 0 
                self.ontheground = True
                break
            else:
                self.ontheground = False
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        self.fist_rect.centerx = self.rect.centerx + self.fist_distance * self.facing
        self.fist_rect.centery = self.rect.centery

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.fist_rect)
    def update(self, screen, keys, dt, platforms):
        self.move_x(keys)
        self.move_y(keys, dt)
        self.collisions(platforms)
        self.render(screen)


