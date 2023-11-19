import pygame

class GameLogic:
    #pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.init()
    up = False
    enemyList = {"grass":[], "lava":[], "ocean":[], "Boss1":[], "Boss2":[], "Boss3":[], "Boss4":[], "Boss5": [], "Boss6": [],"jungle":[], "snow":[]}
    itemlist = {"grass":[], "lava":[], "ocean":[],"Boss1":[],"Boss2":[], "Boss3":[],"Boss4":[],"Boss5": [],"Boss6": [], "jungle":[], "snow":[]}
    objects = {"grass":[], "lava":[], "ocean":[], "Boss1":[],"Boss2":[], "Boss3":[], "Boss4":[], "Boss5": [],"Boss6": [],"jungle":[], "snow":[]}
    soundlist = {"zombie": pygame.mixer.Sound("sounds/hurt.wav"), 
                "achievement": pygame.mixer.Sound("sounds/power.wav"), 
                "coin": pygame.mixer.Sound("sounds/coin.wav"), 
                "heal": pygame.mixer.Sound("sounds/heal.wav"),
                "slip": pygame.mixer.Sound("sounds/slip.wav"),
                "summon": pygame.mixer.Sound("sounds/summonkey.wav"),
                "rifle": pygame.mixer.Sound("sounds/rifle.wav"),
                "sword": pygame.mixer.Sound("sounds/swordslash.wav"),
                "swordhit": pygame.mixer.Sound("sounds/swordhit.wav"),
                "bomb": pygame.mixer.Sound("sounds/explosion.wav"),
                "reload": pygame.mixer.Sound("sounds/reload.wav"),
                "explosion": pygame.mixer.Sound("sounds/explosion.wav"),
                "fishsplash": pygame.mixer.Sound("sounds/splash.wav"),
                "monkeyattack": pygame.mixer.Sound("sounds/monki.wav"),
                "zombiea": pygame.mixer.Sound("sounds/zombieattack.wav"),
                "pumpkinlauncher": pygame.mixer.Sound("sounds/rpg.wav"),
                "splat": pygame.mixer.Sound("sounds/splat.wav"),
                "freeze": pygame.mixer.Sound("sounds/freeze.wav")
                }
    soundlistboss = {"bossdmg": pygame.mixer.Sound("sounds/bossdmg.wav"),
                      "curse": pygame.mixer.Sound("sounds/curse.wav"),
                      "acid": pygame.mixer.Sound("sounds/acid.wav"),
                      "monkey": pygame.mixer.Sound("sounds/monkeysound.wav"),
                        "roar": pygame.mixer.Sound("sounds/yetiroar.wav")
    }
    spellList = []
    bulletlist = []
    bomblist = []
    pumpkinlist = []
    current_chunk = "grass"
    playerPos = [0, 0]
    playerspeedmulti = 1
    pygame.mixer.Sound.set_volume(soundlist["zombie"], .05)
    pygame.mixer.Sound.set_volume(soundlist["bomb"],.05)
    pygame.mixer.Sound.set_volume(soundlist["achievement"],.05)
    pygame.mixer.Sound.set_volume(soundlist["coin"],.9)
    pygame.mixer.Sound.set_volume(soundlist["heal"],.6)    
    pygame.mixer.Sound.set_volume(soundlist["summon"], .5)
    pygame.mixer.Sound.set_volume(soundlist["swordhit"],.5)
    pygame.mixer.Sound.set_volume(soundlist["sword"],.9)
    pygame.mixer.Sound.set_volume(soundlistboss["bossdmg"],.6)  
    pygame.mixer.Sound.set_volume(soundlistboss["curse"],.02)  
    pygame.mixer.Sound.set_volume(soundlistboss["acid"],.6)  
    junglekillsforkey = 0
    snowkillsforkey = 0

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