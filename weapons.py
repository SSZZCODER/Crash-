import pygame
from gamelogic import GameLogic
import math

class weapon():
    def __init__(self, damage, range, attack_cooldown):
        self.damage = damage
        self.range = range
        self.attack_cooldown = attack_cooldown

    def attack(self):
        player_x, player_y = GameLogic.playerPos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y
        math.atan2(rel_x, rel_y)   * (180/math.pi) 
        n = rel_x**2 + rel_y**2
        if n>0:
            n = math.sqrt(n)
            rel_x = rel_x/n
            rel_y = rel_y/n
        rel_x *= self.range
        rel_y *= self.range
    def render():
        pass

            

