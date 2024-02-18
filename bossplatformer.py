import pygame

class Skarmy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.damage = damage
        self.attack_width = 50 
        self.attack_height = self.height
        self.speed = 2
        self.health = 500
        self.img_left = pygame.image.load("images/skeletonarmy.png")
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.x, self.y]
        self.img_left = pygame.transform.scale(self.img_left, [self.width, self.height])
        self.state = "Left"
        self.img_right = pygame.transform.flip(self.img_left, 1, 0)
        self.hit_left = pygame.image.load("images/skeletonarmy (3).png")
        self.hit_left = pygame.transform.scale(self.hit_left, [self.width, self.height])
        self.hit_right = pygame.image.load("images/skeletonarmy (4).png")
        self.hit_right = pygame.transform.scale(self.hit_right, [self.width, self.height])
        self.hit_sound = pygame.mixer.Sound("sounds/skeletonhit.wav")
        self.attack_rect_left = pygame.Rect(0, 0, self.attack_width, self.attack_height)
        self.attack_rect_right = pygame.Rect(0, 0, self.attack_width, self.attack_height)
        self.washit = False
        self.washitcooldown = 5
        self.washitimer = self.washitcooldown
        self.vel_x = 0
        self.pushback = 3
        self.paddedstop = 100
        self.attack_state = "idle"

    def render(self, screen):
        self.rect.center = [self.x, self.y]
        pygame.draw.rect(screen, [0, 0, 0], self.rect)
        if self.state == "Left":
            screen.blit(self.img_left, self.rect)
        if self.state == "Right":
            screen.blit(self.img_right, self.rect)
        if self.state == "hit_left":
            screen.blit(self.hit_left, self.rect)
        if self.state == "hit_right":
            screen.blit(self.hit_right, self.rect)
    def movetoplayer(self, player):
        if player.rect.left > self.rect.right:
            self.state = "Right"
            self.vel_x = self.speed
        elif player.rect.right < self.rect.left:
            self.state = "Left"
            self.vel_x = -self.speed

        self.x += int(self.vel_x)

    def distancefromplayer(self, player):
        return abs(self.rect.centerx - player.rect.centerx)

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
                self.hit_sound.play()



        if self.washit:
            if self.washittimer >= self.washitcooldown:
                self.washit = False
            else:
                self.washittimer += dt 
    def gothit_move(self):
        if self.state == "hit_left":
            self.vel_x = self.pushback

        elif self.state == "hit_right":
            self.vel_x = -self.pushback
    def move(self, player):
        if self.distancefromplayer(player) >= self.paddedstop and self.washit == False:
            self.movetoplayer(player)
        if self.washit:
            self.gothit_move()
        self.x += int(self.vel_x)
    def update(self, screen, player, dt):
        self.render(screen)
        self.gothit(player, dt)
        self.move(player)   
        self.healthbar(screen)
        
