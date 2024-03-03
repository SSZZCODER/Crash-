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
        self.attack_dist = 25
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
        self.attacking = False
        self.attack_length = 8
        self.attack_timer = 0
        self.getattackimages()
        self.cooldown = 10
        self.cooldown_timer = 0
        self.attackvalue = 25
        self.hit_player = False
        self.destroyed = False
    
    def getattackimages(self):
        self.numberofattackimg = 4
        self.attackframe = 0
        self.attackrendertimer = 0
        self.attackimagesright = []
        for i in range(self.numberofattackimg):
            image = pygame.image.load(f"images/skeletonbossattackframes/frame{i}.png")
            image = pygame.transform.scale(image, [self.width, self.height])
            self.attackimagesright.append(image)
        self.attackimagesleft =[]
        for image in self.attackimagesright:
            self.attackimagesleft.append(pygame.transform.flip(image, True, False))

    def idlerender(self,screen):
        if self.state == "Left":
            screen.blit(self.img_left, self.rect)
        if self.state == "Right":
            screen.blit(self.img_right, self.rect)
    def hitrender(self, screen):
        if self.state == "hit_left":
            screen.blit(self.hit_left, self.rect)
        if self.state == "hit_right":
            screen.blit(self.hit_right, self.rect)
    def attackrender(self, screen, direction, dt):
        animation_time = self.attack_length/self.numberofattackimg
        if self.attackrendertimer >= animation_time:
            self.attackframe += 1
            self.attackrendertimer = 0
        else:
            self.attackrendertimer += dt
        if self.attackframe > self.numberofattackimg-1:
            if self.hit_player == True:
                self.hit_player = False
            self.attackframe = self.numberofattackimg-1
        if direction == "right":
            screen.blit(self.attackimagesright[self.attackframe], self.rect)
        if direction == "left":
            screen.blit(self.attackimagesleft[self.attackframe], self.rect)
    def render(self, screen, dt):
        if self.attack_state == "idle" or self.attack_state == "cooldown":
            self.rect.center = [self.x, self.y]
            #pygame.draw.rect(screen, [0, 0, 0], self.rect)
            self.idlerender(screen)
            self.hitrender(screen)
        elif self.attack_state == "attackingright":
            self.attackrender(screen, "right", dt)
        elif self.attack_state == "attackingleft":
            self.attackrender(screen, "left", dt)
    def movetoplayer(self, player):
        if self.attack_state == "idle" or self.attack_state == "cooldown":
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
                if self.attack_state == "idle" or self.attack_state == "cooldown":
                    self.washit = True
                    self.washittimer = 0
                    if self.state == "Left":
                        self.state = "hit_left"
                    if self.state == "Right":
                        self.state = "hit_right"
                else:
                    self.washit = True
                    self.washittimer = 0
                self.hit_sound.play()
                self.health -= player.attack_damage
                
                print("player attacked boss")
                



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
        elif self.distancefromplayer(player) < self.paddedstop:
            self.vel_x = 0
        if self.washit:
            self.gothit_move()
        self.x += int(self.vel_x)
    def can_attack(self, player, dt):
        if self.distancefromplayer(player) < self.paddedstop:
            if self.attack_state == "idle" and self.state == "Left":
                self.attack_state = "attackingleft"
            if self.attack_state == "idle" and self.state == "Right":
                self.attack_state = "attackingright"
        if self.attack_state == "cooldown":
            if self.cooldown_timer < self.cooldown:
                self.cooldown_timer += dt
            elif self.cooldown_timer >= self.cooldown:
                self.cooldown_timer = 0
                self.attack_state = "idle"
    def attack(self, player, screen, dt):
        pushback = 20
        if self.attack_state == "attackingleft":
            if self.attack_timer <= self.attack_length:
                self.attack_rect_left.topleft = [self.rect.topleft[0] - self.attack_dist,self.rect.topleft[1]]
                self.attack_timer += dt
            if self.attack_timer > self.attack_length:
                self.attack_state = "cooldown"                
                self.attack_timer = 0
                self.attackframe = 0
            if self.attack_rect_left.colliderect(player.rect) and self.hit_player == False:
                if self.attackframe > 1:
                    pygame.draw.rect(screen, (255,0,0), self.attack_rect_left)
                    player.gothit(self.attackvalue, -pushback)
                    self.hit_player = True
                #self.attackframe = 0
                #self.attack_timer = 0
                #self.attack_state = "cooldown"

        if self.attack_state == "attackingright":
            if self.attack_timer <= self.attack_length:
                self.attack_rect_right.topright = [self.rect.topright[0] + self.attack_dist,self.rect.topright[1]]

                self.attack_timer += dt
            if self.attack_timer > self.attack_length:
                self.attack_state = "cooldown"                
                self.attack_timer = 0
                self.attackframe = 0
            if self.attack_rect_right.colliderect(player.rect) and self.hit_player == False:
                if self.attackframe > 1:
                    pygame.draw.rect(screen, (255,0,0), self.attack_rect_right)
                    player.gothit(self.attackvalue, pushback)
                    self.hit_player = True                
                #self.attackframe = 0
                #self.attack_timer = 0
                #self.attack_state = "cooldown"

               
                   

                
    def update(self, screen, player, dt):
        self.render(screen, dt)
        self.gothit(player, dt)
        self.move(player)   
        self.can_attack(player, dt)
        self.attack(player, screen, dt)
        self.healthbar(screen)
        if self.health <= 0:
            self.destroyed = True
        
