import menu
import starting
import pygame
import lava
import deathscreen

level = 0

while level != -1:
    if level == 0:
        level = deathscreen.menu()#menu.menu()
    if level == 1:
        level = starting.main()    
    if level == 2:
        level = lava.main()
    if level == 3:
        level = deathscreen.menu()
    print(level)    