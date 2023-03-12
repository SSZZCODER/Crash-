import pygame

class GameLogic:

    pygame.mixer.init()
    up = False
    enemyList = {"grass":[], "lava":[]}
    itemlist = {"grass":[], "lava":[]}
    soundlist = {"zombie": pygame.mixer.Sound("sounds/Zombie Sound.wav"), "achievement": pygame.mixer.Sound("sounds/Achievement Sound Effect.mp3"), "coin": pygame.mixer.Sound("sounds/(mp3juice.blog) - Mario Coin Sound - Sound Effect (HD).mp3")}
    spellList = []
    current_chunk = "grass"
    playerPos = [0, 0]
    pygame.mixer.Sound.set_volume(soundlist["zombie"], .05)
    pygame.mixer.Sound.set_volume(soundlist["achievement"],.05)
    pygame.mixer.Sound.set_volume(soundlist["coin"],.9)
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
        for spell in GameLogic.spellList:
            spell.update(screen)
    def playSound(name):
        pygame.mixer.Sound.play(GameLogic.soundlist[name])