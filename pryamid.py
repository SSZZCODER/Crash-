import pygame
from player_platformer import Player_Platformer
from platformcreator import Platform
from bossplatformer import Skarmy
from enemy import Skeleton, spawner
from healthbarplatformer import HealthBar

def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/pryamid.png')
    background = pygame.transform.scale(background, (750,750))
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    healthbar = HealthBar(30, 0, 115, 20)
    player = Player_Platformer(25, 25, 5, 50, 50, 50, 15, 15, 250)
    platforms = [Platform(0, 600, 150, 750, (0,0,0))]
    enemies = [Skarmy(400, 0, 100, 150, 10)]
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    enemies[0].y = platforms[0].rect.top - enemies[0].height/2
    clock = pygame.time.Clock()
    exit = False
    skeletonspawner = spawner(0, 300, 3)
    mousedown = False

    while not exit:
        dt = clock.get_time()/100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
        
        keys = pygame.key.get_pressed()
        screen.blit(background,[0,0])
        for platform in platforms:
            platform.update(screen)
        for enemy in enemies:
            if type(enemy) == Skarmy:
                enemy.update(screen, player, dt)        
            else:
                enemy.update(screen, player)
            if enemy.destroyed:
                enemies.remove(enemy)
        if len(enemies) == 0:
            return 13
        if player.health <= 0:
            return 3
        healthbar.render(screen, player)
        skeletonspawner.spawn_skeleton(enemies)
        player.update(screen, keys, dt, platforms, mousedown)
        pygame.display.update()
        clock.tick(60)

    

