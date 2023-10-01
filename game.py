import menu
import starting
import pygame
import lava
import ocean    
import deathscreen  
import skinsmenu
import bossarena
import magmaarena
import sharkarena
import jungle
import monkeyarena
from data import saveData

level = 5



while level != -1:
    if level == 0:
        level = menu.menu()
    if level == 1:  
        level = starting.main()      
    if level == 2:
        level = lava.main()
    if level == 3: 
        level = deathscreen.menu()
    if level == 4:
        level = skinsmenu.main()
    if level == 5:
        level = ocean.main()
    if level == 6:
        level = bossarena.main()
    if level == 7:
        level = magmaarena.main()
    if level == 8:
        level = sharkarena.main()
    if level == 9: 
        level = jungle.main()
    if level == 10:
        level = monkeyarena.main()
    print(level) 

        