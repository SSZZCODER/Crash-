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
        self.state = "Left"
        self.img_right = pygame.transform.flip(self.img_left, 1, 0)
        self.hit_left = pygame.image.load("images/skeletonarmy (3).png")
        self.hit_right = pygame.image.load("images/skeletonarmy (4).png")
        self.washit = False
        self.washitcooldown = 5
        self.washitimer = self.washitcooldown
        self.vel_x = 0
        self.pushback = 50

    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        if self.state == "Left":
            screen.blit(self.img_left, self.rect)
        if self.state == "Right":
            screen.blit(self.img_right, self.rect)
    def move(self, player):
        if not self.washit:
            if player.rect.left > self.rect.right:
                self.state = "Right"
                self.vel_x = self.speed
                if abs(player.rect.left - self.rect.right) < self.speed:
                    print("stop")
                    self.vel_x = player.rect.left - self.rect.right
                    self.rect.right = player.rect.left
            elif player.rect.right < self.rect.left:
                self.state = "Left"
                self.vel_x = -self.speed
                if abs(player.rect.right - self.rect.left) < self.speed:
                    print("stop")
                    self.vel_x = player.rect.right - self.rect.left
                    self.rect.left = player.rect.right
        else:
            pass
        self.x += int(self.vel_x)

    def healthbar(self, screen):
        pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(self.x-40, self.y-90, 80, 10))
        pygame.draw.rect(screen, [255, 0, 0], pygame.Rect(self.x-40, self.y-90, int((self.health/500)*80), 10))

    def gothit(self, player, dt):
        if player.fist_rect.colliderect(self.rect):
            if player.attacking and self.washit == False:
                self.washit = True
                self.health -= player.attack_damage
                self.washittimer = 0
                print("player attacked boss")
                if self.state == "Left":
                    self.state = "hit_left"
                if self.state == "Right":
                    self.state = "hit_right"



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
        
