import pygame
from MatrixBuilder import MapState

def render(matrix):
    smaller_dimension = min(WINDOW_WIDTH, WINDOW_HEIGHT)
    box_size = (smaller_dimension - 100)//len(matrix)
    matrix_size = box_size * len(matrix)

    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            box = pygame.Rect(j * box_size + (smaller_dimension - matrix_size)/2, i * box_size + (smaller_dimension - matrix_size)/2, box_size-1, box_size-1)

            if matrix[i][j] == MapState.EMPTY:
                color = (200, 100, 10)
            elif matrix[i][j] == MapState.WALL:
                color = (10, 200, 100)
            elif matrix[i][j] == MapState.APPLE:
                color = (50, 255, 10)
            else:
                color = (0, 150, 255)

            pygame.draw.rect(screen, color, box)


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_COLOR = (255, 131, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
