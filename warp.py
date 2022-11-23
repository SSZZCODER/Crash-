from enum import auto
import pygame
import player
from player import Player


class Warp:
    def __init__(self, xpos, ypos, width, height, auto):
        self.rect = pygame.Rect(xpos, ypos, width,height)
        self.auto = auto

    def lavaWarp(self):
        self.rect = pygame.Rect(0,0,100,100)
        self.auto = auto
        
        if self.rect.colliderect(Player.imageload.get_rect(center =(player.player_x, player.player_y))):
            print("Touched")
