import pygame



class Boss:
    def __init__(self, damage, xpos, ypos, cooldown, timer):
        self.health = 1000
        self.damage = damage
        self.xpos = xpos
        self.ypos = ypos
        self.cooldown = cooldown
        self.timer = timer
        self.image = pygame.image.load('images/New Piskel (5) (1).png')
    def render(self, screen):
        screen.blit(self.image, self.image.get_rect(center = (self.xpos, self.ypos)))
    def update(self, screen):
        self.render(screen)
class Acid:
    def __init__(self, angle, direction, xPos, yPos):
        self.image = pygame.image.load("images/New Piskel (6) (1).png")
        self.image2 = pygame.image.load("images/New Piskel (7) (1).png")
        self.angle = angle
        self.damage = 5
        self.speed = 2
        self.direction = direction
        self.xPos = xPos 
        self.yPos = yPos

