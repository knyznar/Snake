import pygame
from Renderer import printText

class Button:
    def __init__(self, x, y, width, height, title):
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen):
        button = pygame.Rect(self.x, self.y, self.width, self.height)

        mousePosition = pygame.mouse.get_pos()

        if self.isInside(mousePosition):
            color = (0, 200, 0)
        else:
            color = (0, 100, 0)

        pygame.draw.rect(screen, color, button)
        printText(self.title, self, screen, 15)

    def isInside(self, mousePosition):
        return self.x + self.width > mousePosition[0] > self.x and self.y + self.height > mousePosition[1] > self.y