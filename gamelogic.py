import pygame

class GameLogic:
    
    up = False
    enemyList = {"grass":[], "lava":[]}
    itemlist = {"grass":[], "lava":[]}
    current_chunk = "grass"
    playerPos = [0, 0]

    def clear_enemies():
        for enemies in GameLogic.enemyList:
            GameLogic.enemyList[enemies] = []
        for Items in GameLogic.itemlist:
            GameLogic.itemlist[Items] = []
    def Update(screen):
        for Item in GameLogic.itemlist[GameLogic.current_chunk]:
            
            Item.Render(screen)
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:

            enemy.update(screen)

        
