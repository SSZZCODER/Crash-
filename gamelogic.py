import pygame

class GameLogic:
    enemyList = []

    playerPos = [0, 0]

    def Update(screen):
        for enemy in GameLogic.enemyList:
            enemy.update(screen)