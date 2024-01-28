import pygame

class Skarmy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.damage = damage
        self.speed = 2
        self.img = pygame.image.load("images/skeletonarmy.png")
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.x, self.y]
        self.img = pygame.transform.scale(self.img, [self.width, self.height])
        self.washit = False
        self.washitcooldown = 100
        self.washitimer = self.washitcooldown

    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        screen.blit(self.img, self.rect)
    def move(self, player):
        vel_x = 0 
        if player.rect.left > self.rect.right:
            vel_x = self.speed
            if player.rect.left - self.rect.right < self.speed:
                vel_x = player.rect.left - self.rect.right
        if player.rect.right < self.rect.left:
            vel_x = -self.speed
            if abs(player.rect.right - self.rect.left) < self.speed:
                vel_x = player.rect.right - self.rect.left
        self.x += int(vel_x)
    def gothit(self, player, dt):
        if player.fist_rect.colliderect(self.rect):
            if player.attacking and self.washit == False:
                self.washit = True
                self.washittimer = 0
                print("player attacked boss")
        if self.washit:
            if self.washittimer >= self.washitcooldown:
                self.washit = False
            else:
                self.washittimer += dt 

    def update(self, screen, player, dt):
        self.render(screen)
        self.move(player)   
        self.gothit(player, dt)
