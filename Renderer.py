import pygame
from MatrixBuilder import MapState

def rysuj_macierz(macierz):
    smaller_dimension = min(WINDOW_WIDTH, WINDOW_HEIGHT)
    box_size = (smaller_dimension - 100)//len(macierz)
    for i in range (len(macierz)):
        for j in range (len(macierz[i])):
            box = pygame.Rect(j * box_size + 50, i * box_size + 50, box_size-1, box_size-1)

            if macierz[i][j] == MapState.EMPTY:
                color = (200, 100, 10)
            elif macierz[i][j] == MapState.WALL:
                color = (10, 200, 100)
            elif macierz[i][j] == MapState.APPLE:
                color = (50, 255, 10)
            else:
                color = (0, 150, 255)

            pygame.draw.rect(screen, color, box)


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_COLOR = (255, 131, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
