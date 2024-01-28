import pygame

class Skarmy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.damage = damage
        self.speed = 3
        self.img = pygame.image.load("images/skeletonarmy.png")
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.x, self.y]
        self.img = pygame.transform.scale(self.img, [self.width, self.height])
    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        screen.blit(self.img, self.rect)
    def move(self, player):
        vel_x = 0 
        if player.x > self.x:
            vel_x = self.speed
        if player.x < self.x:
            vel_x = -self.speed
        print(vel_x)
        self.x += vel_x
    def update(self, screen, player):
        self.render(screen)
        self.move(player)
