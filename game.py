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
import snow
import snowarena
import desertarena
from data import saveData
import snowarena
import desert
import desertarena
import pryamid
import finalbossdoor

level = 16

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
    if level == 11:
        level = snow.main()
    if level == 12:
        level = snowarena.main()
    if level == 13:
        level = desert.main()
    if level == 14:
        level = desertarena.main()
    if level == 15:
        level = pryamid.main()
    if level == 16:
        level == finalbossdoor.main()
    print("Level: " + str(level)) 