import menu
import main 
import pygame


level = 0

while level != -1:
    if level == 0:
        level = menu.menu()
    if level == 1:
        level = main.main()