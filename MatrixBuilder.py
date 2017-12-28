from enum import Enum

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

class MapState(Enum):
    EMPTY = 0
    SNAKE = 1
    WALL = 2
    APPLE = 3