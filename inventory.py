from turtle import Screen
import pygame
class Inventory:
    def __init__(self):
        self.size = []


    def Draw(self, screen):
        pygame.draw.rect(screen, (135, 135, 135), (175,330, 400, 65))
