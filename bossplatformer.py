import pygame

class Skarmy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.damage = damage
        self.speed = 2
        self.health = 500
        self.img_left = pygame.image.load("images/skeletonarmy.png")
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.x, self.y]
        self.img_left = pygame.transform.scale(self.img_left, [self.width, self.height])
        self.facing = "Left"
        self.img_right = pygame.transform.flip(self.img_left, 1, 0)
        self.washit = False
        self.washitcooldown = 5
        self.washitimer = self.washitcooldown

    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        if self.facing == "Left":
            screen.blit(self.img_left, self.rect)
        if self.facing == "Right":
            screen.blit(self.img_right, self.rect)
    def move(self, player):
        vel_x = 0 
        if player.rect.left > self.rect.right:
            self.facing = "Right"
            vel_x = self.speed
            if player.rect.left - self.rect.right < self.speed:
                vel_x = player.rect.left - self.rect.right
        if player.rect.right < self.rect.left:
            self.facing = "Left"
            vel_x = -self.speed
            if abs(player.rect.right - self.rect.left) < self.speed:
                vel_x = player.rect.right - self.rect.left
        self.x += int(vel_x)
    def healthbar(self, screen):
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.x-40, self.y-90, int((self.health/500)*80), 10))
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
        self.healthbar(screen)
        self.gothit(player, dt)
