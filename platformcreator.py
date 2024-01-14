import pygame


class Platform:
    def __init__(self, x, y, height, width, color):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        



