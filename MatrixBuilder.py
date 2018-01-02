from enum import Enum
import math

def buildSquareMatrix(size):
    tab = []
    for i in range(size):
        row = []
        for j in range(size):
            if j==0 or j==size-1 or i==0 or i==size-1:
                row.append(MapState.WALL)
            else:
                row.append(MapState.EMPTY)
        tab.append(row)
    return tab

def buildSquareMatrixLevel1(size):
    tab = buildSquareMatrix(size)
    for i in range((size-2)//3):
        tab[i+1][(size-2)//2] = MapState.WALL
        tab[i+1][(size-2)//2+1] = MapState.WALL
    for i in range(math.ceil(((size-2)/3)*2), size-1):
        tab[i+1][(size-2)//2] = MapState.WALL
        tab[i+1][(size-2)//2+1] = MapState.WALL
    return tab

def buildSquareMatrixLevel2(size):
    tab = buildSquareMatrix(size)
    for i in range((size-2)//2-1):
        tab[i][5] = MapState.WALL
        tab[i][6] = MapState.WALL
        tab[i][size-11] = MapState.WALL
        tab[i][size-12] = MapState.WALL
    for i in range((size-2)//2+2, size-1):
        tab[i][10] = MapState.WALL
        tab[i][11] = MapState.WALL
        tab[i][size-6] = MapState.WALL
        tab[i][size-7] = MapState.WALL
    return tab

class MapState(Enum):
    EMPTY = 0
    SNAKE = 1
    WALL = 2
    APPLE = 3