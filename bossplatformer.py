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
        self.vel_x = 0
        self.pushback = 50

    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        if self.facing == "Left":
            screen.blit(self.img_left, self.rect)
        if self.facing == "Right":
            screen.blit(self.img_right, self.rect)
    def move(self, player):
        if player.rect.left > self.rect.right:
            self.facing = "Right"
            self.vel_x = self.speed
            if abs(player.rect.left - self.rect.right) < self.speed:
                print("stop")
                self.vel_x = player.rect.left - self.rect.right
                self.rect.right = player.rect.left
        elif player.rect.right < self.rect.left:
            self.facing = "Left"
            self.vel_x = -self.speed
            if abs(player.rect.right - self.rect.left) < self.speed:
                print("stop")
                self.vel_x = player.rect.right - self.rect.left
                self.rect.left = player.rect.right
        else:
            if self.washit == False:
                self.vel_x = 0
        self.x += int(self.vel_x)

    def healthbar(self, screen):
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.x-40, self.y-90, int((self.health/500)*80), 10))

    def gothit(self, player, dt):
        if player.fist_rect.colliderect(self.rect):
            if player.attacking and self.washit == False:
                self.washit = True
                self.health -= player.attack_damage
                self.washittimer = 0
                print("player attacked boss")
                if self.facing == "Left":
                    self.vel_x += self.pushback
                if self.facing == "Right":
                    self.vel_x -= self.pushback
            print(self.health)

        if self.washit:
            if self.washittimer >= self.washitcooldown:
                self.washit = False
            else:
                self.washittimer += dt 

    def update(self, screen, player, dt):
        self.render(screen)
        self.gothit(player, dt)
        self.move(player)   
        self.healthbar(screen)
        
