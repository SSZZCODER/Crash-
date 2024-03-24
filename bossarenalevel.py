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
from boss import Boss
import random


class BossArena:
    def __init__(self, backgroundimage, current_chunk, boss, original_level, key, keyimage, keypos, enemyspawner = None):
        self.screen = pygame.display.set_mode((750, 750))
        self.background = pygame.image.load(backgroundimage)
        self.background = pygame.transform.scale(self.background, [750, 750])
        self.heart = pygame.image.load('images/heart.png')
        self.heart = pygame.transform.scale(self.heart, (120, 120))
        self.energy = pygame.image.load('images/energy.png')
        self.energy = pygame.transform.scale(self.energy, (65, 65))
        self.StaminaBar = staminabar(30, 30, 115, 20)
        self.HealthBar = healthbar(30, 0, 115, 20)
        self.Spell = spell(320, 640, 115, 20)
        self.coinspawner= spawneritems(0,300,20)
        self.bandagespawner= spawneritems(0,300,1)
        if enemyspawner != None:
            self.enemyspawner = enemyspawner
        else:
            self.enemyspawner = None    
        self.current_chunk = current_chunk
        GameLogic.current_chunk = current_chunk
        self.boss = boss
        GameLogic.enemyList[GameLogic.current_chunk].append(self.boss)

        self.clock = pygame.time.Clock()
        self.exit = False

        self.level = None
        self.original_level = original_level
        self.key = key
        self.keyimage = keyimage
        self.keypos = keypos

    def gameloop(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:   
                self.exit=True
            if event.type == pygame.QUIT:
                self.level = -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.level = 0
            
        self.screen.blit(self.background,[0,0])
        GameLogic.Update(self.screen)
        self.coinspawner.spawncoin()
        self.bandagespawner.spawnbandage()
        if self.enemyspawner != None:
            self.enemyspawner.spawn()

        if Player.Update(self.screen,events) == True:
            self.level = 3
        if self.boss not in GameLogic.enemyList[GameLogic.current_chunk]:
            Player.bosskeys[self.key].append(pygame.image.load(self.keyimage))
            Player.bosskeys[self.key].append(self.keypos)
            self.level = self.original_level
   
        self.Spell.render(self.screen)
        self.StaminaBar.render(self.screen)
        self.HealthBar.render(self.screen)
        self.screen.blit(self.heart, (-29, -45))
        self.screen.blit(self.energy, (-9, 10))
        pygame.display.update()
        self.clock.tick(60)

