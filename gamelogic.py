import pygame

class GameLogic:

    pygame.mixer.init()
    up = False
    enemyList = {"grass":[], "lava":[]}
    itemlist = {"grass":[], "lava":[]}
    soundlist = {"zombie": pygame.mixer.Sound("sounds/Zombie Sound.wav")}
    current_chunk = "grass"
    playerPos = [0, 0]
    pygame.mixer.Sound.set_volume(soundlist["zombie"], .05)

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
    
    def playSound(name):
        pygame.mixer.Sound.play(GameLogic.soundlist[name])