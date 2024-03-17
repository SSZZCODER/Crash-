import pygame
from inventory import Inventory
from particle import ParticleSystem
from player import Player
from hotbar import Hotbar

from bars import *
from enemy import *
import time
from gamelogic import GameLogic
from items import spawneritems
from boss import Boss7
import random
from warp import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((750,750))
    background = pygame.image.load('images/sandarena.png')
    background = pygame.transform.scale(background, (750,750))
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    slowedimg = pygame.image.load('images/turtle.png')
    slowedimg = pygame.transform.scale(slowedimg, (200, 120))    
    StaminaBar = staminabar(30, 30, 115, 20)
    HealthBar = healthbar(30, 0, 115, 20)
    Spell = spell(320, 640, 115, 20)
    slowedbar = slowed(30, 60, 115, 20)

    
    spawner3 = spawneritems(0,300,20)
    spawner4 = spawneritems(0,300,1)
    portal = pygame.image.load('images/desertportal.png')
    portal = pygame.transform.scale(portal, (150,200))
    desertkey = pygame.image.load('images/desertkey.png')
    desertkey = pygame.transform.scale(desertkey, (50,20))
    desertkey_rect = desertkey.get_bounding_rect()
    heart = pygame.image.load('images/heart.png')
    heart = pygame.transform.scale(heart, (120, 120))
    energy = pygame.image.load('images/energy.png')
    energy = pygame.transform.scale(energy, (65, 65))
    GameLogic.current_chunk = "Boss7"
    GameLogic.enemyList[GameLogic.current_chunk].append(Boss7(7, 350 ,95))
    bossportal6 = Warp(625, 35,100,175,(0,0,0), 50,0) 


    clock = pygame.time.Clock()
    exit = False
    droppedkey = False
    global keypos 
    keypos = [0,0]

    haskey = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                exit=True
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return 0
            if bossportal6.Touched() == True and haskey == True:
                Player.MoveBy(bossportal6.offset_x, bossportal6.offset_y)
                GameLogic.spellList = []
                return 15
                
        screen.blit(background,[0,0])
        GameLogic.Update(screen)
        droppedkey = GameLogic.desertbossdroppedkey
        if haskey == False and droppedkey == True:
            if pygame.Rect(GameLogic.playerPos, [50, 55]).colliderect(pygame.Rect(keypos, [36, 15])):
                haskey = True
                droppedkey = False
        if haskey == True:
            bossportal6 = Warp(625, 35,100,175,(153,76,0), 50,0) 
            droppedkey = False
        bossportal6.Update(screen)        
        screen.blit(portal, [600, 10])
        spawner3.spawncoin()
        spawner4.spawnbandage()
        if Player.Update(screen) == True:
            return 3
        print(GameLogic.desertbossdroppedkey)
        Spell.render(screen)
        StaminaBar.render(screen)
        HealthBar.render(screen)
        if droppedkey == True:
            keypos = [300,300]
            screen.blit(desertkey, keypos)
            desertkey_rect.center = keypos
        if Player.freezecooldown != 0:
            slowedbar.render(screen)
            screen.blit(slowedimg, (11, 45))
        screen.blit(heart, (-29, -45))
        screen.blit(energy, (-9, 10)) 
        pygame.display.update()
        clock.tick(60)

    

