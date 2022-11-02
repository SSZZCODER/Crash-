import pygame
import random 
class enemy():
    pass
class zombie():
        damage_cooldown = 30
        move_cooldown = 30
        speed = 2
        health = 150
        zombie_x = 250
        zombie_y = 250
        transparent = (0, 0, 0, 0)
        zombieimage = pygame.image.load('images/zombie.png')
        zombieimage = pygame.transform.scale(zombieimage,(200, 200))
        imageload = zombieimage
        move_leftright= random.choice([1, 2])
        move_updown = random.choice([1, 2])
        speed = .25

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
                if zombie.health == 0:
                    print("dead")
                    zombie.death_message
        def death_message():
            pass
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
            if zombie.move_cooldown != 0:
                 zombie.move_cooldown -= 1 
            if zombie.move_cooldown == 0:
               zombie.move_cooldown = 30
               zombie.move_leftright= random.choice([1, 2])
               zombie.move_updown = random.choice([1, 2])
                
            if zombie.move_leftright == 1:
                    zombie.zombie_x -= 10 * zombie.speed
                    if zombie.zombie_x < -85:
                            zombie.move_cooldown = 30
                            zombie.move_leftright = 2
            if zombie.move_leftright == 2:
                    zombie.zombie_x += 10  * zombie.speed
                    if zombie.zombie_x > 621:
                            zombie.move_cooldown = 30
                            zombie.move_leftright = 1
            if zombie.move_updown == 1:
                    zombie.zombie_y -= 10  * zombie.speed
                    if zombie.zombie_y < 0:
                        zombie.move_cooldown = 30
                        zombie.move_updown = 2 
            if zombie.move_updown == 2:
                    zombie.zombie_y += 10 * zombie.speed
                    if zombie.zombie_y > 650:
                            zombie.move_cooldown = 30
                            zombie.move_updown = 1
          