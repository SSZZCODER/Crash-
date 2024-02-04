import pygame


class Platform:
    def __init__(self, x, y, height, width, color):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("images/platformimage.png")
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

    def update(self, screen):
        screen.blit(self.image, self.rect)

        



