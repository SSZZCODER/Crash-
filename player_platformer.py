import pygame
from pygame.math import Vector2

class Player_Platformer:
    def __init__(self, x, y, speed, jumpheight, width, height, fist_width, fist_height):
        self.x = x
        self.y = y
        self.speed = speed
        self.jumpheight = jumpheight
        self.width = width
        self.height = height
        self.fist_width = fist_width
        self.fist_height = fist_height
        self.vel = Vector2(0)
        self.dx = 0
        self.dy = 0
        self.create_player()

    def create_player(self):
        self.facing = "right"
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = Vector2(self.x, self.y)
        self.fist_distance = 50
        self.fist_rect = pygame.Rect(0, 0, self.fist_width, self.fist_height)
        self.fist_rect.center = Vector2(self.rect.centerx+self.fist_distance, self.rect.centery)
        
    def move_x(self, keys):
        if keys[pygame.K_d]:
            self.vel[0] = self.speed
        elif keys[pygame.K_a]:
            self.vel[0] = -self.speed
        else:
            self.vel[0] = 0

    def move_y(self, keys, dt):
        gravity = 9
        self.vel[1] += gravity*dt

    def collisions(self, platforms):
        self.dx = self.vel[0]
        self.dy = self.vel[1]
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        self.fist_rect.centerx = self.rect.centerx + self.fist_distance
        self.fist_rect.centery = self.rect.centery

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.fist_rect)
    def update(self, screen, keys, dt, platforms):
        self.move_x(keys)
        self.move_y(keys, dt)
        self.collisions(platforms)
        self.render(screen)


