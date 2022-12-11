from random import random
from turtle import width
import pygame
import random
import math
class ParticleSystem:
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.particles = []
        self.cooldown = 0
        self.timer = self.cooldown
        
    def Spawn(self):
        self.particles.append(Particle(self.xpos, self.ypos, self.color, 5, 5, [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]))
    def Update(self, screen):
        if self.timer > 0:
            self.timer -= 1
        else: 
            self.Spawn()
            self.timer = self.cooldown

        for particle in self.particles:
            if particle.Update(screen) == False:
                self.particles.remove(particle)
            
class Particle:
    def __init__(self, xpos, ypos, color, width, height, direction):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction
        self.lifetime = random.randint(15,25)
        self.color = color

        self.speed = random.uniform(2.5,3.5)         
        self.width = width
        self.height = height
    def Update(self, screen):
        if self.lifetime > 0:  
            self.lifetime -= 1
            self.Move()
            self.Render(screen)
            return True
        else:
            return False

    def Move(self):
        c = self.direction[0]**2 + self.direction[1]**2
        if c>0:
            c = math.sqrt(c)
            self.direction = [self.direction[0]/c, self.direction[1]/c]
        self.xpos += self.direction[0]*self.speed
        self.ypos += self.direction[1]*self.speed

    def Render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.width, self.height))


