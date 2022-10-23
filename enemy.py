import pygame
import random 
class zombie():
        damage_cooldown = 30
        speed = 2
        health = 150
        zombie_x = 250
        zombie_y = 250

        zombieimage = pygame.image.load('images/New Piskel (21).png')
        zombieimage = pygame.transform.scale(zombieimage,(200, 200))
        imageload = zombieimage

        def damagesprite():
            damageimage = pygame.image.load('images/New Piskel (21)damaged 1.png')
            damageimage = pygame.transform.scale(damageimage,(200, 200))
            zombie.imageload = damageimage
            #zombie.imageload = zombie.zombieimage
        def getdamage(player_x, player_y):
            #if player_x == zombie.zombie_x and  player_y == zombie.zombie_y:
                zombie.damagesprite()
                zombie.health -= 10
                print("attacked")
                print(zombie.health)
        def Render(screen):
            screen.blit(zombie.imageload, (zombie.zombie_x, zombie.zombie_y)) 
            if zombie.imageload !=  zombie.zombieimage:
                zombie.damage_cooldown -= 1
                if zombie.damage_cooldown <= 0:
                    zombie.imageload = zombie.zombieimage
                    zombie.damage_cooldown = 30
        def update():
            zombie.move()
        def move():
                move_leftright= random.choice([1, 2])
                move_updown= random.choice([1, 2])
                if move_leftright == 1:
                        zombie.zombie_x -= 1
                        if zombie.zombie_x < -275:
                                zombie.zombie_x += 1
                if move_leftright == 2:
                        zombie.zombie_x += 1
                        if zombie.zombie_x > 425:
                                zombie.zombie_x -= 1
                if move_updown == 1:
                        zombie.zombie_y -= 1
                        if zombie.zombie_y > 425:
                                zombie.zombie_y += 1
                if move_leftright == 2:
                        zombie.zombie_y += 1
                        if zombie.zombie_y < - 275:
                                zombie.zombie_y -= 1
          