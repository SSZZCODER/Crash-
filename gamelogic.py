import pygame

class GameLogic:
    
    enemyList = {"grass":[], "lava":[]}
    current_chunk = "grass"
    playerPos = [0, 0]

    def clear_enemies():
        for enemies in GameLogic.enemyList:
            GameLogic.enemyList[enemies] = []

    def Update(screen):
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:

            enemy.update(screen)