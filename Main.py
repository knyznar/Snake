import pygame
from Renderer import *
from MatrixBuilder import *
from Snake import *
from Apple import *

pygame.init()

clock = pygame.time.Clock()

def game():
    matrix = buildSquareMatrix(19)
    snake = Snake(matrix)
    putApple(matrix)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # przechwyć zamknięcie okna
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                snake.setDirection(event.key)

        moveResult = snake.move()

        if moveResult == MoveResult.isDead:
            print("Przegrołeś")
            pygame.quit()
            return

        if moveResult == MoveResult.appleEaten:
            putApple(matrix)

        screen.fill(WINDOW_COLOR)
        rysuj_macierz(matrix)
        pygame.display.flip()

        clock.tick(10)

game()