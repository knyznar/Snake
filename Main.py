import pygame
from Renderer import *
from MatrixBuilder import *
from Snake import *

pygame.init()

clock = pygame.time.Clock()

matrix = buildSquareMatrix(19)
snake = Snake(matrix)


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # przechwyć zamknięcie okna
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            snake.setDirection(event.key)

    snake.move()

    screen.fill(WINDOW_COLOR)
    msElapsed = clock.tick(5)
    rysuj_macierz(matrix)
    pygame.display.flip()