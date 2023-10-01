import pygame

class GameLogic:

    pygame.mixer.init()
    up = False
    enemyList = {"grass":[], "lava":[], "ocean":[], "Boss1":[], "Boss2":[], "Boss3":[], "Boss4":[], "jungle":[]}
    itemlist = {"grass":[], "lava":[], "ocean":[],"Boss1":[],"Boss2":[], "Boss3":[],"Boss4":[], "jungle":[]}
    objects = {"grass":[], "lava":[], "ocean":[], "Boss1":[],"Boss2":[], "Boss3":[], "Boss4":[], "jungle":[]}
    soundlist = {"zombie": pygame.mixer.Sound("sounds/hurt.wav"), 
                "achievement": pygame.mixer.Sound("sounds/power.wav"), 
                "coin": pygame.mixer.Sound("sounds/coin.wav"), 
                "heal": pygame.mixer.Sound("sounds/heal.wav"),
                "slowed": pygame.mixer.Sound("sounds/slip.wav")
                }
    soundlistboss = {"bossdmg": pygame.mixer.Sound("sounds/bossdmg.wav"),
                      "curse": pygame.mixer.Sound("sounds/curse.wav"),
                      "acid": pygame.mixer.Sound("sounds/acid.wav"),
                      "monkey": pygame.mixer.Sound("sounds/monkeysound.wav")
    }
    spellList = []
    bulletlist = []
    current_chunk = "grass"
    playerPos = [0, 0]
    playerspeedmulti = 1
    pygame.mixer.Sound.set_volume(soundlist["zombie"], .05)
    pygame.mixer.Sound.set_volume(soundlist["achievement"],.05)
    pygame.mixer.Sound.set_volume(soundlist["coin"],.9)
    pygame.mixer.Sound.set_volume(soundlist["heal"],.6)    
    pygame.mixer.Sound.set_volume(soundlistboss["bossdmg"],.6)  
    pygame.mixer.Sound.set_volume(soundlistboss["curse"],.02)  
    pygame.mixer.Sound.set_volume(soundlistboss["acid"],.6)  
    #pygame.mixer.music.load(soundlist[""])
    #pygame.mixer.music.set_volume(soundlist[""],.05)
    def clear_enemies():
        for enemies in GameLogic.enemyList:
            GameLogic.enemyList[enemies] = []
        for Items in GameLogic.itemlist:
            GameLogic.itemlist[Items] = []
    def Update(screen):
        for object in GameLogic.objects[GameLogic.current_chunk]:
            object.update(screen)
        for Item in GameLogic.itemlist[GameLogic.current_chunk]:
            Item.Render(screen)
        for enemy in GameLogic.enemyList[GameLogic.current_chunk]:
            enemy.update(screen)
        for spell in GameLogic.spellList:
            spell.update(screen)
    def playSound(name):
        pygame.mixer.Sound.play(GameLogic.soundlist[name])

    def playSoundBoss(name):
          pygame.mixer.Sound.play(GameLogic.soundlistboss[name])